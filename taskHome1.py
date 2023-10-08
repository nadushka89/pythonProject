# Задание 1.
#
# Условие:
# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False
# в противном случае. Передаваться должна только одна строка, разбиение вывода использовать не нужно.


import subprocess
import string

def check_text(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    command = 'cat /etc/os-release'
    text = '22.04.1'
    result = check_text(command, text)
    if result:
        print(f"Text '{text}' found in command '{command}'.")
    else:
        print(f"Text '{text}' not found in command '{command}'.")
