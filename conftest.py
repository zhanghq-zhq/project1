from selenium import webdriver
from time import sleep
import pytest

import requests


@pytest.fixture(scope='session')
def driver():
    driver=webdriver.Chrome()
    sleep(1)
    driver.maximize_window()
    sleep(1)
    # driver.get('https://mail.qq.com/')
    driver.get('http://newecshop.longtest.cn/admin/privilege.php?act=login')
    sleep(1)
    yield driver
    sleep(2)
    driver.close()


@pytest.fixture(scope='session')
def session():
	session=requests.session()
	yield session