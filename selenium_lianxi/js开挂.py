from selenium import webdriver
from time import sleep


driver=webdriver.Chrome()
driver.maximize_window()
sleep(1)
driver.get('https://www.baidu.com/')
sleep(2)
driver.execute_script('document.querySelector("#kw").value="zhanghq";') # 修改一个属性
sleep(1)
driver.execute_script("document.querySelector('form#upform').removeAttribute('style')") # 移除一个属性 实现上传文件
sleep(1)
driver.execute_script("")

sleep(3)
driver.quit()
