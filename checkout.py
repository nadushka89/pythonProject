import subprocess
import pytest


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return result
    else:
        return False


# def checkout(cmd, text, return_output=False):
#     result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
#     if return_output:
#         return text in result.stdout and result.returncode == 0, result.stdout
#
#     else:
#         return text in result.stdout and result.returncode == 0

