import pytest
import yaml
import requests
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdrivermanager import ChromeDriverManager
from webdrivermanager import GeckoDriverManager

with open("./testdata.yaml") as f:
    data = yaml.safe_load(f)
    selected_browser = data["browser"]

chrome_driver_path = "/home/user/PycharmProjects/pythonProject/itog/chromedriver"


@pytest.fixture(scope="session")
def browser():
    if selected_browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        # ChromeDriverManager().download_and_install()
        # service = Service(executable_path=ChromeDriverManager().install())
        # options = webdriver.ChromeOptions()
        service = Service(executable_path=chrome_driver_path)
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()


S = requests.Session()


@pytest.fixture()
def user_login():
    try:
        result = S.post(url=data['url'], data={'username': data['login'], 'password': data['pswd']})
        response_json = result.json()
        token = response_json.get('token')
    except:
        logging.exception("Get token exception")
        token = None
    logging.debug(f"Return token success")
    return token
