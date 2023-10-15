from sshcheckers import ssh_checkout, upload_files
import pytest
import yaml
import datetime
import subprocess

with open("config.yaml", encoding="UTF-8") as f:
    config = yaml.safe_load(f)

@pytest.fixture()
def start_time():
    return  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def save_journal_log(start, end, filename):
    cmd = f'journalctl --since="{start}" --until="{end}" > {filename}'
    subprocess.run(cmd, shell=True, check=True)
def test_deploy(start_time):
    res = []
    # Загрузка пакета p7zip
    upload_files(config['ssh_host'], config['username'], config['ssh_password'],
                 config['p7zip_deb_local_path'], config['p7zip_deb_remote_path'])

    # Установка пакета
    cmd_install = f"echo '{config['ssh_password']}' | sudo -S dpkg -i {config['p7zip_deb_remote_path']}"
    res.append(ssh_checkout(config['ssh_host'], config['username'], config['ssh_password'], cmd_install,
                            "Настраивается пакет"))

    # Проверка установки
    cmd_check_install = f"echo '{config['ssh_password']}' | sudo -S dpkg -s p7zip-full"
    res.append(ssh_checkout(config['ssh_host'], config['username'], config['ssh_password'], cmd_check_install,
                            "Status: install ok installed"))

    assert all(res)
    end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    save_journal_log(start_time, end_time, 'log_test_deploy.txt')

if __name__ == '__main__':
    pytest.main(['-vv'])