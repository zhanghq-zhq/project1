from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
sleep(2)
driver.maximize_window()
sleep(2)
driver.get("https://www.baidu.com/")
sleep(2)
dr=driver.find_element_by_id("kw")
dr.send_keys("zhangqw") #send_keys将内容输入到文本框
sleep(2)
print(dr.tag_name)
print(driver.find_element_by_id('su').get_attribute('value'))
print(dr.get_attribute('value'))
print(dr.is_displayed(),dr.is_enabled())

driver.find_element_by_id("kw").clear() #清除内容

sleep(3)
driver.quit()
