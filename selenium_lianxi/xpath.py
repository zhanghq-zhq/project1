from selenium import webdriver
from time import sleep


driver=webdriver.Chrome()
driver.maximize_window()
sleep(1)
driver.get('https://www.baidu.com/')
sleep(2)
# 通过xpath相对路径文本定位，在xpath中还可以使用 or 和 and
# driver.find_element_by_xpath("//div//a[text()='新闻']").click()

# 通过contains定位，包含的文字
# driver.find_element('xpath',"//a[contains(text(),'新')]").click()

# 通过轴的方式定位，following是定位该元素往后的元素
# driver.find_element('xpath',"//a[text()='新闻']/following::a[1]").click()

# 通过轴的方式定位，following-sibling是定位元素同级后面的元素
# driver.find_element('xpath',"//*[text()='新闻']/following-sibling::a[1]").click()

# preceding:定位改节点前面的全部属性，//*[text()='学术']/preceding::a[1]
# preceding:定位改节点同级前面的属性，//*[text()='学术']/preceding-sibling::[1]

# css selector,在过滤元素的时候前面不需要加@，定位的时候input[id=kw] 元素可以不加引号， id是特殊属性可以简写 input#kw
# .表示class > 表示往下找


sleep(2)
driver.quit()