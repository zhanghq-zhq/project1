from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

from test.test_ui.beaspage.qq_login_page import Qq_Login_Page

from config import logging

from time import sleep
def test_02(driver):
    logging.info('测试登录qq邮箱')
    Qq_Login_Page(driver).iframe_enter("login_frame")
    Qq_Login_Page(driver).loggin("3091356800","zhq0508.")
    Qq_Login_Page(driver).my_sleep(20)