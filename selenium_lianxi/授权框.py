from selenium import webdriver
from time import sleep


driver=webdriver.Chrome()
sleep(1)
driver.maximize_window()
sleep(1)
driver.get("http://admin:secret@115.28.108.130:5000/api/user/login2/")
sleep(3)
driver.quit()

