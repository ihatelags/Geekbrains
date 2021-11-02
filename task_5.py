"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

from subprocess import Popen, PIPE
from chardet import detect


def ping(url):
    args = ['ping', '-n', '1', url]
    ping = Popen(args, stdout=PIPE)
    for line in ping.stdout:
        detect_chars = detect(line)['encoding']
        line = line.decode(detect_chars).encode('utf-8')
        print(line.decode('utf-8'))


ping('yandex.ru')
ping('youtube.com')
