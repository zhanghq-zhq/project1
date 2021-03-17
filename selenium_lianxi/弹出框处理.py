from selenium import webdriver
from time import sleep


driver=webdriver.Chrome()
sleep(1)
driver.maximize_window()
sleep(1)
driver.get("file:///E:/学习相关资料/自动化学习课件/selenium_demo/selenium.html")
sleep(1)

"""
# div弹框 DOM弹框 --直接定位元素操作即可
driver.find_element("xpath","/html/body/div[2]/div[5]/div/button").click()
sleep(2)
# 逐级定位
driver.find_element("class name","modal-footer").find_element("tag name","button").click()
"""

# js弹框 也叫警告框
driver.find_element("id","alert").click()
sleep(1)
driver.switch_to.alert.dismiss()
sleep(1)
driver.find_element("id","confirm").click()
sleep(1)
driver.switch_to.alert.accept()
sleep(1)
driver.find_element_by_id('prompt').click()
sleep(1)
driver.switch_to.alert.send_keys('Kevin')
sleep(1)
driver.switch_to.alert.accept()

# div.dismiss() # 关闭
# div.accept() # 确定
# div.send_keys("输入")

sleep(5)

driver.quit()