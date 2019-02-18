import time

from selenium import webdriver


driver = webdriver.Chrome()
driver.get('http://www.baidu.cn/')
# 查找id为kw的元素  输入关键字
driver.find_element_by_id('kw').send_keys('python')
time.sleep(1)
# 查找id为su的元素 点击
driver.find_element_by_id('su').click()
time.sleep(1)

js = "window.open('https://www.sogou.com/')"
driver.execute_script(js)
time.sleep(2)

# 获取当前所有窗口
windows = driver.window_handles

# 根据窗口索引进行切换
driver.switch_to.window(windows[0])
time.sleep(2)
driver.switch_to.window(windows[1])
time.sleep(2)
driver.find_element_by_id('query').send_keys('python')
driver.find_element_by_id('stb').click()
time.sleep(1)
driver.close()
time.sleep(1)
driver.quit()