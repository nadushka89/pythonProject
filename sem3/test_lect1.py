from checkout import checkout
import yaml
import pytest

with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)
class TestPositive:
    def test_testing1(self):
        assert checkout("cat /etc/os-release", "Jammy"), "test1 FAIL"


    #@pytest.mark.run_this
    def test_testing2(self):
        assert checkout("cat /etc/os-release", "22.04.1"), "test2 FAIL"

    def test_step3(self):
        assert checkout("cat /etc/os-release", "NAME"), "test3 FAIL"

    def test_step4(self, make_folder, make_file, write_stat):

        assert checkout(f"cd {data.get('folder_in')}; 7z a -t{data.get('archive_type')} "
                        f"{data.get('folder_out')}archive.7z", "Everything is Ok"), "test4 FAIL"
        write_stat()
    def test_step5(self, make_folder, make_file,write_stat):
        assert checkout(f"cd {data.get('folder_out')}; 7z d -t{data.get('archive_type')} ./archive.7z file1.txt", "Everything is Ok"), "test5 FAIL"
        write_stat()
    # Условие:
    # Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).
    def test_step6(self, make_folder,make_file,write_stat):
        assert checkout(f"cd {data.get('folder_out')}; 7z l -t{data.get('archive_type')} ./archive.7z", "Listing archive"), "test6 FAIL"
        write_stat()

    def test_step7(self,make_folder,make_file,write_stat):
        assert checkout(f"cd {data.get('folder_out')}; 7z x -t{data.get('archive_type')} ./archive.7z", "Everything is Ok"), "test7 FAIL"
        write_stat()

    # *Задание 2. *
    # • Установить пакет для расчёта crc32
    # sudo apt install libarchive-zip-perl
    # • Доработать проект, добавив тест команды расчёта хеша (h). Проверить, что хеш совпадает
    # с рассчитанным командой crc32.
    def test_step8(self, make_folder,make_file,write_stat):
            result_7z = checkout(f"cd {data.get('folder_out')}; 7z h -t{data.get('archive_type')} ./archive.7z", "Everything is Ok")
            if result_7z:
                hash_7z = result_7z.stdout.splitlines()[15].split(":")[1].strip()
            else:
                pytest.fail("7z command failed")

            result_crc32 = checkout(f"crc32 {data.get('folder_out')}archive.7z", "")
            if result_crc32:
                hash_crc32 = result_crc32.stdout.strip()
            else:
                pytest.fail("crc32 command failed")
            assert hash_7z.lower() == hash_crc32.lower(), f"Hash mismatch: 7z={hash_7z}, crc32={hash_crc32}"

            write_stat()


if __name__ == '__main__':
    pytest.main(["-vv"])







# запуск из терминала: pytest test_lec1.py
# или с ключом -v для более информативного вывода: pytest test_lec1.py -v
# если не работает: python3 -m pytest test_lec1.py -v
