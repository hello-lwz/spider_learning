import time

from lxml import etree
from selenium import webdriver


# 指定driver的绝对路径
# driver = webdriver.PhantomJS(executable_path='C:/Users/10601/Desktop/phantomjs-2.1.1-windows/bin/phantomjs')
driver = webdriver.Chrome()

# 向一个url发起请求
driver.get("http://www.baidu.cn/")

# print(driver.page_source) # 查看网页源码
# print(driver.get_cookies()) # 网站所有cookie
# print(driver.current_url) # 网站当前url


# 查找id为kw的元素  输入关键字
driver.find_element_by_id('kw').send_keys('python')
# 查找id为su的元素 点击
driver.find_element_by_id('su').click()

time.sleep(3)

# 退出当前页面
driver.close()

# 退出模拟浏览器
# driver.quit() # 一定要退出！不退出会有残留进程！