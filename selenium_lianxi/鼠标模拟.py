from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep

# move_to_element()：移动到元素,有些元素是将鼠标移动到元素显示下拉
def yidong():
    driver=webdriver.Chrome()
    driver.maximize_window()
    sleep(1)
    driver.get('https://www.baidu.com/')
    sleep(1)
    elm=driver.find_element('xpath',"//div[@id='u1']//span[text()='设置']")
    sleep(1)
    ActionChains(driver).move_to_element(elm).perform()
    sleep(2)
    driver.find_element('xpath',"//*[text()='高级搜索']").click()

    sleep(5)
    driver.quit()

def yidong():
    driver=webdriver.Chrome()
    driver.maximize_window()
    sleep(1)
    driver.get('https://www.baidu.com/')
    sleep(1)
    elm=driver.find_element('xpath',"//div[@id='u1']//span[text()='设置']")
    sleep(1)
    ActionChains(driver).move_to_element(elm).perform()
    sleep(2)
    driver.find_element('xpath',"//*[text()='高级搜索']").click()

    sleep(5)
    driver.quit()