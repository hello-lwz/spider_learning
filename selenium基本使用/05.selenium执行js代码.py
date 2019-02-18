#selenium执行js代码
import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("http://www.douban.com/")
time.sleep(1)

js = 'window.scrollTo(0,document.body.scrollHeight)' # js语句 下滑到页尾
driver.execute_script(js) # 执行js的方法

time.sleep(3)
driver.quit()
