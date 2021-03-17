import random
import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ES
from config import printscreen_path
from config import logging


class Beas_Page():
    """该类是WEB UI测试基础方法类"""

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def my_element(self, element):
        """
        :user : 定位器
        :param element: 调用函数时传入element 实例('xpath','元素'),元组类型
        """
        logging.info("定位器，元素是：{}".format(element))
        try:
            return self.driver.find_element(*element)
        except BaseException:
            id = random.randint(10000, 99999)
            logging.error('定位失败,定位的元素是：{},图片id是:{}'.format(element, id))
            raise

    def wait_find(self, element, max_time=10, interva_time=1):
        """
            :user :显示等待
            :param element: 调用该函数时传入需要定位的元素，元组形式传入,示例('xpath','xxxxx')
            :param max_time: 调用该函数时传入需要循环定位的最大时间,默认是10s,int类型
            :param interva_time: 调用该函数时传入循环定位的间隔时间，默认1s循环一次，int类型
        """
        logging.info("通过显示等待定位{}".format(element))
        try:
            return WebDriverWait(
                self.driver, max_time, interva_time).until(
                ES.presence_of_element_located(element))

        except BaseException:
            id = random.randint(10000, 99999)
            logging.error("定位元素失败,定位的元素是：{},图片id是：{}".format(element, id))
            self.screenshot(id, '定位失败')
            raise

    def my_sleep(self, s):
        """
            :user : 强制等待
            :type : int
            :param s: 调用该方法时传入一个等待的时间,单位秒
        """
        logging.info("强制等待{}秒".format(s))
        sleep(s)

    def smart_sleep(self, s):
        """
            :user : 智能等待
            :type : int
            :param s: 调用该方法时传入一个最大等待时间,单位秒
        """
        self.driver.implicitly_wait(s)

    def screenshot(self, id, data):
        """
        :user : 截图
        :param id: 传入一个id作为图片的id号，int类型 or str类型
        :param data: 传入一个描述，str类型，示例：定位失败
        """
        logging.info('调用截图函数，进行截图')
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        user = "{}-".format(id) + "{}".format(data) + \
            now_time.replace(" ", '-').replace(":", '-')

        self.driver.get_screenshot_as_file(
            printscreen_path + "/{}.png".format(user))

    def iframe_enter(self, element):
        """
        :user : 切入框架
        :param element: 传入要切入的框架，name or id
        """
        logging.info(f'切入框架{element}')
        try:
            self.driver.switch_to.frame(element)
        except BaseException:
            logging.error(f'切入框架失败，元素是{element}')
            raise

    def iframe_go(self):
        """
        :user : 切到父框架
        """
        logging.info('切到父框架')
        self.driver.switch_to.parent_frame()

    def iframe_go_all(self):
        """
        :user : 切出所有框架
        """
        logging.info('切出所有框架')
        self.driver.switch_to.default_content()

    def trade(self, title):
        """
        :user : 切换网页
        :param title: 调用该函数时传入一个网页的标题，str类型
        """
        logging.info(f"切换窗口，切到{title}窗口")
        all_win = self.driver.window_handles
        for x in all_win:
            if self.driver.title != title:
                self.driver.switch_to.window(x)

    def js_del_element(self, element_loc, element):
        """
        :user : 使用js删除页面元素
        :param element_loc: 调用该函数时传入css selector 定位元素，str类型
        :param element: 调用函数时传入要删除的元素
        """
        logging.info(f"使用js移除{element}元素")
        self.driver.execute_script(
            f"document.querySelector({element_loc}).removeAttribute({element})")

    def mouse_hover(self,elm):
        """
        :user : 模拟鼠标悬停
        :param element: 调用参数时传需要定位的元素
        """
        logging.info(f"模拟鼠标悬停在{elm}上")
        ActionChains(self.driver).move_to_element(elm).perform()


    def select_pull(self,elm,text):
        """
        :user : 通过Select类处理选择下拉框
        :param text: 调用该函数时传入要选择的数据text文本,str 类型
        :param elm: 调用该函数时传入下拉框的element, str 类型
        """
        logging.info(f"在{elm}选择框选择:{text}")
        Select(self.driver.find_element("xpath",elm)).select_by_visible_text(text)