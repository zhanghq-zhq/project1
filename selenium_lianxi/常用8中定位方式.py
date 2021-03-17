from selenium import webdriver
from time import sleep

def t1(data):
    driver = webdriver.Chrome()
    sleep(1)
    driver.get(data)
    sleep(1)
    driver.maximize_window()
    sleep(1)
    return driver
def t2():
    driver=t1("https://www.baidu.com/")
    driver.find_element_by_name("wd").send_keys("python") #通过name定位获取元素
    sleep(1)
    driver.find_element_by_id("su").click() #通过id定位元素
    sleep(5)
    driver.quit()

def t3():
    driver=t1("https://www.hao123.com/")
    sleep(2)
    driver.maximize_window()
    sleep(2)
    driver.find_element_by_class_name("button-hook").click() # 通过class name定位获取元素
    sleep(2)
    driver.quit()

def t4():
    driver=t1("https://www.hao123.com/")
    sleep(2)
    driver.find_element_by_link_text("人民网").click() # 通过文字定位链接
    sleep(5)
    driver.quit()


def t5():
    driver=t1("https://www.hao123.com/")
    sleep(2)
    driver.find_element_by_partial_link_text("人民").click() # 通过部分文字定位链接
    sleep(5)
    driver.quit()


def t6():
    driver = t1("https://www.hao123.com/")
    sleep(2)
    driver.find_element_by_xpath('//*[@id="search"]/form/div[2]/input').send_keys('zhanghq') # 通过xpath定位元素
    sleep(2)
    driver.quit()


def t6():
    driver = t1("https://www.hao123.com/")
    sleep(2)
    driver.find_element_by_xpath('//*[@id="search"]/form/div[2]/input').send_keys('zhanghq') # 通过xpath定位元素
    sleep(2)
    driver.quit()

def t7():
    driver = t1("https://www.hao123.com/")
    sleep(2)
    driver.find_element_by_css_selector('#search > form > div.g-ib.textWrapper.shadow-hook.wrapper-hook > input').send_keys('zhanghq')
    sleep(2)
    driver.quit()

t7()
def lianxi():
    driver=webdriver.Chrome()

    driver.get("https://www.hao123.com/")
    sleep(1)
    driver.maximize_window()
    print(driver.title)
    sleep(2)
    driver.get("https://www.qq.com/")
    sleep(5)
    print(driver.title)
    driver.back()
    sleep(2)
    driver.set_window_size(600,200)
    sleep(2)
    driver.save_screenshot(r'E:\project1\printscreen\2.png')
    sleep(2)

    driver.quit()

