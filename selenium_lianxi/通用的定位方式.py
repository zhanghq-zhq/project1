from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

def ty1():
    # 通用定位方式1

    driver = webdriver.Chrome()
    sleep(1)
    driver.maximize_window()
    sleep(1)
    driver.get('https://www.hao123.com/')
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="search"]/form/div[2]/input').send_keys('zhanghq')
    print(driver.title)
    sleep(2)
    driver.quit()



def ty2():
    # 通用定位2
    driver = webdriver.Chrome()
    sleep(1)
    driver.maximize_window()
    sleep(1)
    driver.get('https://www.baidu.com/')
    sleep(1)
    name_loc=('name','wd')
    id_loc=('id','su')

    driver.find_element(*name_loc).send_keys('zhanghq')
    sleep(2)
    driver.find_element(*id_loc).click()
    print(driver.title)
    sleep(2)
    driver.quit()
ty2()