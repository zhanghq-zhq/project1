from selenium import webdriver
from time import sleep

def test_02():
    driver=webdriver.Chrome()
    sleep(2)
    driver.maximize_window()
    sleep(2)
    driver.get("https://www.baidu.com/")