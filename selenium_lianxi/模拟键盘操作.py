from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
sleep(1)
driver.maximize_window()
sleep(1)
driver.get('file:///E:/学习相关资料/自动化学习课件/selenium_demo/selenium.html')

driver.find_element('xpath',"//*[text()='双击']/following::input[1]").send_keys(Keys.CONTROL,'a')
sleep(1)
driver.find_element('xpath',"//*[text()='双击']/following::input[1]").send_keys(Keys.CONTROL,'c')
sleep(1)
driver.find_element('xpath',"//*[text()='双击']/following::input[2]").send_keys(Keys.CONTROL,'v')
sleep(1)













# driver.get('https://www.baidu.com/')
# sleep(1)
# input_q=('id','kw')
# x=driver.find_element(*input_q)
# x.send_keys('百度你好')
# sleep(1)
# x.send_keys(Keys.BACK_SPACE)
# sleep(1)
# x.send_keys(Keys.BACK_SPACE)
# sleep(1)
# x.send_keys(Keys.CONTROL,'a')
# x.send_keys(Keys.CONTROL,'c')
# sleep(1)
# driver.find_element('tag name','body').click()
# sleep(1)
# x.send_keys(Keys.CONTROL,'v')
# sleep(1)
# x.send_keys(Keys.ENTER)
#
#
sleep(2)
driver.quit()