from selenium import webdriver


# 指定driver的绝对路径
# driver = webdriver.PhantomJS(executable_path='C:/Users/10601/Desktop/phantomjs-2.1.1-windows/bin/phantomjs')
driver = webdriver.Chrome(executable_path='D:/lwz/python/chromedriver')

# 向一个url发起请求
driver.get("http://www.baidu.cn/")

# 把网页保存为图片
driver.save_screenshot("baidu2.png")

# 退出模拟浏览器
driver.quit() # 一定要退出！不退出会有残留进程！