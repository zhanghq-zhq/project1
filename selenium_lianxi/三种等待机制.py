from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

from selenium.webdriver.support import expected_conditions as ES


# 强制等待
def mysleep():
    driver=webdriver.Chrome()
    driver.maximize_window()
    sleep(1) # 强制等待
    driver.get('https://www.baidu.com/')
    sleep(1)
    elm=driver.find_element('xpath',"//div[@id='u1']//span[text()='设置']")
    sleep(1)
    ActionChains(driver).move_to_element(elm).perform()
    sleep(2)
    driver.find_element('xpath',"//*[text()='高级搜索']").click()

    sleep(5)
    driver.quit()


# 智能等待，智能等待是使用driver.implictly_wait(最大等待时间）。
# 每次会话（一次运行为一次会话）只需要使用一次。使用智能等待后，在任何元素定位不到时，
# 会自动间隔一定的时间再次定位，直到定位到元素或者超时。
def zhinengdengdai():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://www.baidu.com/')

    elm=driver.find_element('xpath',"//div[@id='u1']//span[text()='设置']")

    ActionChains(driver).move_to_element(elm).perform()

    driver.find_element('xpath',"//*[text()='高级搜索']").click()

    sleep(5)
    driver.quit()

def xianxingdengdai():
    driver=webdriver.Chrome()
    driver.maximize_window()
    sleep(1)
    driver.get('https://www.baidu.com/')

    elm=driver.find_element('xpath',"//div[@id='u1']//span[text()='设置']")
    sleep(2)

    WebDriverWait(driver,30,1).until(lambda driver:ActionChains(driver).move_to_element(elm)).perform()
    # WebDriverWait(driver,30,1).until(ES.presence_of_element_located(lambda driver:ActionChains(driver).move_to_element(elm))).perform()




    sleep(2)



    WebDriverWait(driver,30,1).until(lambda driver:driver.find_element('xpath',"//*[text()='高级搜索']")).click()
    sleep(5)
    driver.quit()
xianxingdengdai()