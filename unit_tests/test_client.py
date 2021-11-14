"""Unit-тесты клиента"""
import sys
import os
import unittest
import time

sys.path.append(os.path.join(os.getcwd(), '..'))  # нужно чтобы импортировать другие файлы проекта
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client import Client


class TestClass(unittest.TestCase):
    """
    Класс с тестами
    """
    time_now = time.time()
    test = Client.create_presence()
    test[TIME] = time_now
    test_out = {
        ACTION: PRESENCE,
        TIME: time_now,
        USER: {
            ACCOUNT_NAME: 'Guest'
        }
    }

    def test_def_presence(self):
        """Тест коректного запроса"""
        self.assertEqual(self.test, self.test_out)

    def test_200_ans(self):
        """Тест корректного разбора ответа 200"""
        self.assertEqual(Client.process_ans({RESPONSE: 200}), '200 : OK')

    def test_400_ans(self):
        """Тест корректного разбора 400"""
        self.assertEqual(Client.process_ans({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        """Тест исключения без поля RESPONSE"""
        self.assertRaises(ValueError, Client.process_ans, {})


if __name__ == '__main__':
    unittest.main()
