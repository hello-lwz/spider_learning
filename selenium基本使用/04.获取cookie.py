from selenium import webdriver

# 使用chrome不调用窗口
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.douban.com/")

# selenium 处理cookie
cookies_dict = {cookie['name']:cookie['value'] for cookie in driver.get_cookies()}
print(cookies_dict)

# 删除某个name的key和value
driver.delete_cookie('ll')

# 删除全部cookie
driver.delete_all_cookies()


