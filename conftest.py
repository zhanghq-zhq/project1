from selenium import webdriver
from time import sleep
import pytest


@pytest.fixture(scope='session')
def driver():
    driver=webdriver.Chrome()
    sleep(1)
    driver.maximize_window()
    sleep(1)
    driver.get('https://mail.qq.com/')
    # driver.get('file:///E:/学习相关资料/自动化学习课件/selenium_demo/selenium.html')
    sleep(1)
    yield driver
    sleep(2)
    driver.close()

