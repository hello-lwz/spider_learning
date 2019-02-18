from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

driver.find_element_by_id('kw').send_keys('qq邮箱')
time.sleep(1)

driver.find_element_by_id('su').click()
time.sleep(1)

driver.find_element_by_class_name('favurl').click()
time.sleep(2)

windows = driver.window_handles
driver.switch_to.window(windows[1])
# 获取登录iframe并切换
login_frame = driver.find_element_by_id('login_frame') # 根据id定位 frame元素
driver.switch_to.frame(login_frame)

# 输入账号。密码
driver.find_element_by_id('u').send_keys('1031244227')
driver.find_element_by_id('p').send_keys('LWZ199508')
driver.find_element_by_id('login_button').click()
time.sleep(1)
# driver.quit()