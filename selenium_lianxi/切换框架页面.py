# 框架页面是指在一个HTML中引入多个HTML

from selenium import webdriver
from time import sleep


driver=webdriver.Chrome()
driver.maximize_window()
sleep(1)
driver.get("file:///E:/学习相关资料/自动化学习课件/selenium_demo/selenium.html")
sleep(1)
# 切入第一层
driver.switch_to.frame("parent_frame") # 可以使用name、iframe的id、index
sleep(1)
# 切入第二层
driver.switch_to.frame('left') # 同级不能切换
driver.find_element('xpath','/html/body/ul/li[1]/a').click()
sleep(1)
# 切出到父框架
driver.switch_to.parent_frame() #无参数
sleep(1)
driver.switch_to.frame('main')
sleep(1)
driver.find_element('id','kw').send_keys('zhdjashkd')
sleep(1)
driver.switch_to.default_content() #切出所有框架


sleep(10)
driver.quit()