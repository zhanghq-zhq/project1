from selenium import webdriver
import time

driver=webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.get("https://www.baidu.com/")
time.sleep(2)
dr=driver.find_element_by_class_name("s_ipt_wr")
dr.find_element_by_tag_name("input").send_keys("zhanghq") # 逐级定位

# dr.find_elements_by_tag_name("input").send_keys("zhanghq") # 如果dr下有多个input可以使用find_element索引定位

time.sleep(3)
driver.quit()


