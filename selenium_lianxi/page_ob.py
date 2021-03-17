from selenium import webdriver

class Page_my():
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver


    input_loc=("xpath","//input[@id='kw']")
    bouut_loc=("css selector","input#su")

    def input_my(self,data):
        elm=self.driver.find_element(*self.input_loc)

        elm.clear()
        elm.send_keys(data)

    def b_my(self):
        self.driver.find_element(*self.bouut_loc).click()

    def zhuhe(self,data):

        self.input_my(data)
        self.b_my()



if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com/')
    baidu=Page_my(driver)
    baidu.zhuhe("大赢家")
    driver.quit()