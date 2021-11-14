"""Клиентская часть"""

import sys
import json
import socket
import time
import logging
import logs.config_client_log
from errors import ReqFieldMissingError, NonDictInputError
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT
from common.utils import get_message, send_message, validate_ip, validate_port

# Инициализация клиентского логера
CLIENT_LOGGER = logging.getLogger('client')


class Client:

    def __init__(self):
        # Загружаем параметы коммандной строки
        try:
            self.server_address = sys.argv[1]
            self.server_port = int(sys.argv[2])
            if self.server_port < 1024 or self.server_port > 65535:
                CLIENT_LOGGER.critical(
                    f'Попытка запуска клиента с неподходящим номером порта: {server_port}.'
                    f' Допустимы адреса с 1024 до 65535. Клиент завершается.')
                raise ValueError
            CLIENT_LOGGER.info(f'Запущен клиент с параметрами: '
                               f'адрес сервера: {server_address}, порт: {server_port}')
        except IndexError:
            self.server_address = DEFAULT_IP_ADDRESS
            self.server_port = DEFAULT_PORT
        except ValueError:
            CLIENT_LOGGER.error('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
            print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
            sys.exit(1)

    @staticmethod
    def create_presence(account_name='Guest'):
        # Функция генерирует запрос о присутствии клиента
        CLIENT_LOGGER.debug(f'Сформировано {PRESENCE} сообщение для пользователя {account_name}')
        out = {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: account_name
            }
        }
        return out

    @staticmethod
    def process_ans(message):
        # Функция разбирает ответ сервера
        CLIENT_LOGGER.debug(f'Разбор сообщения от сервера: {message}')
        if RESPONSE in message:
            if message[RESPONSE] == 200:
                return '200 : OK'
            return f'400 : {message[ERROR]}'
        raise ValueError

    def main(self):
        # Инициализация сокета и обмен
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.connect((self.server_address, self.server_port))
        message_to_server = self.create_presence()
        send_message(transport, message_to_server)
        try:
            answer = self.process_ans(get_message(transport))
            CLIENT_LOGGER.info(f'Принят ответ от сервера {answer}')
            print(answer)
        except (ValueError, json.JSONDecodeError):
            CLIENT_LOGGER.error('Не удалось декодировать полученную Json строку.')
            print('Не удалось декодировать сообщение сервера.')
        except NonDictInputError:
            CLIENT_LOGGER.error(f'Аргумент функции должен быть словарем!')
        except ReqFieldMissingError as missing_error:
            CLIENT_LOGGER.error(f'В ответе сервера отсутствует необходимое поле '
                                f'{missing_error.missing_field}')
        except ConnectionRefusedError:
            CLIENT_LOGGER.critical(f'Не удалось подключиться к серверу {server_address}:{server_port}, '
                                   f'конечный компьютер отверг запрос на подключение.')
        except TimeoutError:
            CLIENT_LOGGER.error('Попытка установить соединение была безуспешной, '
                                'т.к. от другого компьютера за требуемое время не получен нужный отклик.')
            print('Попытка установить соединение была безуспешной, '
                  'т.к. от другого компьютера за требуемое время не получен нужный отклик.')


if __name__ == '__main__':
    client_obj = Client()
    Client.main(client_obj)
