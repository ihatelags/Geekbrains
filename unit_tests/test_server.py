"""Unit-тесты сервера"""

import sys
import os
import unittest
import time
sys.path.append(os.path.join(os.getcwd(), '..'))  # нужно чтобы импортировать другие файлы проекта
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from server import Server


class TestServer(unittest.TestCase):
    """
    В сервере только 1 функция для тестирования
    """
    response_ok = {RESPONSE: 200}

    response_err = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    message_to_server = {
        'ok': {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: 'Guest'
            }},
        'no_action': {
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: 'Guest'
            }},
        'action_no_presence': {
            ACTION: 'no presence',
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: 'Guest'
            }},
        'no_time': {
            ACTION: PRESENCE,
            USER: {
                ACCOUNT_NAME: 'Guest'
            }},
        'no_user': {
            ACTION: PRESENCE,
            TIME: time.time(),
        },
        'account_name_not_Guest': {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: 'Not Guest'
            }},
    }

    def test_process_client_message_ok(self):
        self.assertEqual(Server.process_client_message(self.message_to_server['ok']), self.response_ok)

    def test_process_client_message_not_action(self):
        self.assertEqual(Server.process_client_message(self.message_to_server['no_action']), self.response_err)

    def test_process_client_message_action_not_presence(self):
        self.assertEqual(Server.process_client_message(self.message_to_server['action_no_presence']), self.response_err)

    def test_process_client_message_not_time(self):
        self.assertEqual(Server.process_client_message(self.message_to_server['no_time']), self.response_err)

    def test_process_client_message_not_user(self):
        self.assertEqual(Server.process_client_message(self.message_to_server['no_user']), self.response_err)

    def test_process_client_message_account_name_not_guest(self):
        self.assertEqual(Server.process_client_message(self.message_to_server['account_name_not_Guest']),
                         self.response_err)


if __name__ == '__main__':
    unittest.main()
