from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
sleep(2)
driver.get('https://www.hao123.com/')
sleep(2)
driver.maximize_window()
sleep(2)
t1=driver.find_elements_by_class_name('g-gc') # 获取一组数据
t1[0].click()
sleep(5)
driver.back()
sleep(2)
t1[1].click()
sleep(5)
driver.quit()
