"""Серверная часть"""

import socket
import sys
import json
import logging
import logs.config_server_log
from errors import IncorrectDataReceivedError, NonDictInputError
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT
from common.utils import get_message, send_message, validate_ip, validate_port

# Инициализация логирования сервера.
SERVER_LOGGER = logging.getLogger('server')


class Server:

    def __init__(self):
        # Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию.
        try:
            if '-p' in sys.argv:
                self.listen_port = int(sys.argv[sys.argv.index('-p') + 1])
            else:
                self.listen_port = DEFAULT_PORT
            if self.listen_port < 1024 or self.listen_port > 65535:
                SERVER_LOGGER.critical('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
                raise ValueError
        except IndexError:
            SERVER_LOGGER.critical('После параметра -\'p\' необходимо указать номер порта.')
            sys.exit(1)
        except ValueError:
            SERVER_LOGGER.critical('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
            sys.exit(1)

        # Загружаем какой адрес слушать
        try:
            if '-a' in sys.argv:
                self.listen_address = sys.argv[sys.argv.index('-a') + 1]
            else:
                self.listen_address = ''

        except IndexError:
            SERVER_LOGGER.critical('После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
            sys.exit(1)

        # Готовим сокет
        self.transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.transport.bind((self.listen_address, self.listen_port))

        # Слушаем порт
        self.transport.listen(MAX_CONNECTIONS)

    @staticmethod
    def process_client_message(message):
        # Обработчик сообщений от клиентов
        SERVER_LOGGER.debug(f'Разбор сообщения от клиента : {message}')
        if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
                and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
            return {RESPONSE: 200}
        return {
            RESPONSE: 400,
            ERROR: 'Bad Request'
        }

    def main(self):

        print ('Server is running...')
        while True:
            client, client_address = self.transport.accept()
            try:
                message_from_client = get_message(client)
                print(f'Установлено соединение с ПК {client_address}')
                SERVER_LOGGER.info(f'Установлено соедение с ПК {client_address}')
                response = self.process_client_message(message_from_client)
                SERVER_LOGGER.info(f'Cформирован ответ клиенту {response}')
                send_message(client, response)
                client.close()
                print(f'Разорвано соединение с ПК {client_address}')
            except (ValueError, json.JSONDecodeError):
                SERVER_LOGGER.error(f'Не удалось декодировать JSON строку, полученную от '
                                    f'клиента {client_address}. Соединение закрывается.')
                print('Принято некорретное сообщение от клиента.')
                client.close()
            except IncorrectDataReceivedError:
                SERVER_LOGGER.error(f'От клиента {client_address} приняты некорректные данные. '
                                    f'Соединение закрывается.')
                client.close()
            except NonDictInputError:
                SERVER_LOGGER.error(f'Аргумент функции должен быть словарем!')
                client.close()


if __name__ == '__main__':
    server_obj = Server()
    Server.main(server_obj)
