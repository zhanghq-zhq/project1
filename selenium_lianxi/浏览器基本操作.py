from selenium import webdriver
from time import sleep

driver=webdriver.Chrome() # 打开浏览器
sleep(2)
driver.maximize_window() # 窗口最大化
sleep(2)
driver.set_window_size(600,600) # 设置窗口大小
sleep(2)
driver.get("https://www.baidu.com/") # 打开网址
sleep(2)


driver.quit()

