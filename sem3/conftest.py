import os
from datetime import datetime

import pytest
import yaml
from checkout import checkout

with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def make_folder():
    yield checkout(f'mkdir -p {data.get("folder_in")} {data.get("folder_out")} {data.get("folder_ext")}', '')
    # checkout(f'rm -r {data.get("folder_in")} {data.get("folder_out")} {data.get("folder_ext")}', '')
@pytest.fixture()
def make_file():
    return checkout(f'cd {data.get("folder_in")}; touch file1.txt file2.txt file3.txt', '')


@pytest.fixture()
def write_stat():
    def _write_stat():
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_count = len(os.listdir(data.get("folder_in")))
        file_size = os.path.getsize(f"{data.get('folder_out')}archive.7z")

        with open("/proc/loadavg", "r") as f:
            loadavg = f.read().strip()

        with open('stat.txt', 'a', encoding='UTF-8') as stat_file:
            stat_file.write(f"{current_time}, {file_count}, {file_size}, {loadavg}\n")

    return _write_stat