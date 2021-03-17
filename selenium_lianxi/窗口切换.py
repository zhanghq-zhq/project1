from selenium import webdriver
from time import sleep


driver=webdriver.Chrome()
driver.maximize_window()
sleep(1)
driver.get('https://www.baidu.com/')
sleep(1)
driver.find_element('id','s-top-left').find_elements('tag name','a')[0].click()
all_win=driver.window_handles
for x in all_win:
    print(x)
print('所有窗口',all_win)
sleep(2)
new_win=all_win[1]
print('切换前',driver.title)
sleep(1)
driver.switch_to.window(new_win) # 切换窗口
print('切换后',driver.title)
sleep(4)

driver.quit()