from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep


driver=webdriver.Chrome()
sleep(1)
driver.maximize_window()
sleep(1)
driver.get("file:///E:/学习相关资料/自动化学习课件/selenium_demo/selenium.html")
sleep(1)
elm=Select(driver.find_element("id","area"))
# elm.select_by_index(1) # 通过下标选择下拉框数据
# sleep(2)
# elm.select_by_value("hebei")
# sleep(2)
elm.select_by_visible_text("上海")

sleep(5)

driver.quit()

