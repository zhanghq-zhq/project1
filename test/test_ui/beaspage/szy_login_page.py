from test.test_ui.beaspage.beas_page import Beas_Page
from config import logging


class Login_page(Beas_Page):

    user_loc=('xpath',"//*[text()='用户名']/following::input[1]")
    pwd_loc=('xpath',"//*[text()='用户名']/following::input[2]")
    login_loc=('xpath',"//*[text()='用户名']/following::input[4]")

    def user_input_method(self,user):
        logging.info(f'输入用户名：{user}，元素是{self.user_loc}')
        self.wait_find(self.user_loc).send_keys(user)

    def pwd_input_method(self,pwd):
        logging.info(f'输入密码：{pwd}，元素是{self.pwd_loc}')
        self.wait_find(self.pwd_loc).send_keys(pwd)

    def click_login_button_method(self):
        logging.info(f'点击登录按钮，元素是{self.login_loc}')
        self.wait_find(self.login_loc).click()


    def login_method(self,user,pwd):
        logging.info('开始登录')
        self.user_input_method(user)
        self.pwd_input_method(pwd)
        self.click_login_button_method()


