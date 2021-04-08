from test.test_ui.beaspage.beas_page import Beas_Page
from config import logging


class Goods_Method_Page(Beas_Page):

    goods_loc=('xpath',"//*[text()='商品管理']")
    goods_list_loc=("xpath","//*[text()='商品管理']/following::a[1]")
    check_goods_list_loc=("xpath","//*[text()='商品管理']/following::a[2]")
    add_goods_loc=("xpath","//*[text()='商品管理']/following::a[3]")


    def click_goods_method(self):
        logging.info(f"点击商品管理，元素是:{self.goods_loc}")
        self.iframe_enter("menu_frame")
        self.my_sleep(2)
        self.wait_find(self.goods_loc).click()

    def click_goods_list_method(self):
        logging.info(f"点击商品列表，元素是：{self.goods_list_loc}")
        self.click_goods_method()
        self.wait_find(self.goods_list_loc).click()

    def click_check_goods_list_method(self):
        logging.info(f"点击入住商品管理，元素是：{self.check_goods_list_loc}")
        self.click_goods_method()
        self.wait_find(self.check_goods_list_loc).click()

    def add_goods_method(self):
        logging.info(f"点击添加商品，元素是：{self.add_goods_loc}")
        self.click_goods_method()
        self.wait_find(self.add_goods_method()).click()