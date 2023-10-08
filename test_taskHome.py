# Задание 1.
#
# Условие:
# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False
# в противном случае. Передаваться должна только одна строка, разбиение вывода использовать не нужно.
# Задание 2. (повышенной сложности). Доработать функцию из предыдущего задания таким образом,
# чтобы у нее появился дополнительный режим работы, в котором вывод разбивается на слова
# с удалением всех знаков пунктуации (их можно взять из списка string.punctuation модуля string).
# В этом режиме должно проверяться наличие слова в выводе.

import subprocess
import string

# def check_text(command, text, split_mode=False):
#     result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='UTF-8')
#     out = result.stdout
#     if split_mode:
#         words = out.split()
#         print(words)
#         return any(text in word for word in words)
#     else:
#         return result.returncode == 0 and text in out

# if __name__ == '__main__':
#     command = 'cat /etc/os-release'
#     text = '22.04.1'
#     result = check_text(command, text, split_mode=True)
#     if result:
#         print(f"Text '{text}' found in command '{command}'.")
#     else:
#         print(f"Text '{text}' not found in command '{command}'.")

import subprocess
import pytest


def check_text(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False
def test_testing1():
    assert check_text("cat /etc/os-release", "jammy"), "test1 FAIL"

#@pytest.mark.run_this
def test_testing2():
    assert check_text("cat /etc/os-release", "22.04.1"), "test2 FAIL"


def test_testing3():
    assert check_text("cat /etc/os-release", "NAME"), "test3 FAIL"

# запуск из терминала: pytest test_taskHome.py
# или с ключом -v для более информативного вывода: pytest test_taskHome.py -v
