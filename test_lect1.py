import subprocess

import pytest
from checkout import checkout

folder_in = '/home/user/folder_in/'
folder_out = '/home/user/folder_out/'
folder_ext= '/home/user/folder_ext/'

def test_testing1():
    assert checkout("cat /etc/os-release", "Jammy"), "test1 FAIL"

#@pytest.mark.run_this
def test_testing2():
    assert checkout("cat /etc/os-release", "22.04.1"), "test2 FAIL"

def test_step3():
    assert checkout("cat /etc/os-release", "NAME"), "test3 FAIL"

def test_step4():
    assert checkout(f"cd {folder_in}; 7z a {folder_out}archive.7z", "Everything is Ok"), "test4 FAIL"

def test_step5():
    assert checkout(f"cd {folder_out}; 7z d ./archive.7z file1.txt", "Everything is Ok"), "test5 FAIL"

# Условие:
# Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).
def test_step6():
    assert checkout(f"cd {folder_out}; 7z l ./archive.7z", "Listing archive"), "test6 FAIL"

def test_step7():
    assert checkout(f"cd {folder_out}; 7z x ./archive.7z", "Everything is Ok"), "test7 FAIL"

# *Задание 2. *
# • Установить пакет для расчёта crc32
# sudo apt install libarchive-zip-perl
# • Доработать проект, добавив тест команды расчёта хеша (h). Проверить, что хеш совпадает
# с рассчитанным командой crc32.
def test_step8():
        result_7z = checkout(f"cd {folder_out}; 7z h ./archive.7z", "Everything is Ok")
        if result_7z:
            hash_7z = result_7z.stdout.splitlines()[15].split(":")[1].strip()
        else:
            pytest.fail("7z command failed")

        result_crc32 = checkout(f"crc32 {folder_out}archive.7z", "")
        if result_crc32:
            hash_crc32 = result_crc32.stdout.strip()
        else:
            pytest.fail("crc32 command failed")
        assert hash_7z.lower() == hash_crc32.lower(), f"Hash mismatch: 7z={hash_7z}, crc32={hash_crc32}"



    # result_7z = checkout(f"cd {folder_out}; 7z h ./archive.7z", "Everything is Ok")
    # hash_7z = result_7z.stdout.splitlines()[7].split(":")[1].strip()
    # result_crc32 = checkout(f"crc32 {folder_out}archive.7z", " ")
    # hash_crc32 = result_crc32.stdout.strip()
    # assert hash_7z == hash_crc32, f"Hash mismatch: 7z={hash_7z}, crc32={hash_crc32}"







# запуск из терминала: pytest test_lec1.py
# или с ключом -v для более информативного вывода: pytest test_lec1.py -v
# если не работает: python3 -m pytest test_lec1.py -v
