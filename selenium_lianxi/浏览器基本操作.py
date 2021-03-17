from selenium import webdriver
from time import sleep

driver=webdriver.Chrome() # 打开浏览器
sleep(1)

driver.set_window_size(600,600) # 设置窗口大小
sleep(1)
driver.maximize_window() # 窗口最大化
sleep(1)
driver.get("https://www.baidu.com/") # 打开网址
sleep(1)
driver.refresh() #刷新网页
sleep(1)
driver.save_screenshot(r"E:\project1\printscreen\1.png") #截图
sleep(1)

# driver.close() #关闭当前网页
sleep(1)
print(driver.title) # 获取当前窗口的title
sleep(2)
print(driver.current_url) # 获取当期的url

# driver.refresh() #前进
# sleep(2)
# driver.back() #后退
sleep(2)

driver.quit()

