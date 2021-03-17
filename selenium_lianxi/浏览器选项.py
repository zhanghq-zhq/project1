from selenium import webdriver
from time import sleep

opt=webdriver.ChromeOptions()
sleep(1)
# opt.headless=True # 无界面启动
# opt.add_argument('--headless') # 无界面启动
# opt.add_argument('headless') # 无界面启动
opt.add_argument('start-fullscreen')
driver=webdriver.Chrome(options=opt)
driver.get("https://www.baidu.com/")

print(driver.title,driver.current_url)

sleep(1)
driver.fullscreen_window() #全屏

driver.quit()