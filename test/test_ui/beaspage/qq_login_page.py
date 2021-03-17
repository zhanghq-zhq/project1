from test.test_ui.beaspage.beas_page import Beas_Page

from selenium import webdriver
from config import logging
class Qq_Login_Page(Beas_Page):
    """该类是qq邮箱登录页的page"""


    user_element_loc=("xpath","//input[@id='u']")
    pwd_element_loc=("xpath","//input[@id='u']/following::input[1]")
    loggin_element_loc=("xpth","//a[@class='login_button']/input")

    def user_input_method(self,user):
        logging.info(f"向用户框输入用户名，数据是：{user}")
        self.wait_find(self.user_element_loc).send_keys(user)


    def pwd_input_method(self,pwd):
        logging.info(f"向密码框输入密码，数据是：{pwd}")
        self.wait_find(self.pwd_element_loc).send_keys(pwd)

    def loggin_button_method(self):
        logging.info("点击登录按钮")
        self.wait_find(self.loggin_element_loc).click()


    def loggin(self,user,pwd):
        self.user_input_method(user)
        self.pwd_input_method(pwd)
        self.loggin_button_method()
