from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.douban.com/")

id1 = driver.find_element_by_id('anony-nav')
print(id1)

id_list = driver.find_element_by_id('anony-nav')
print(id_list)

# find_element 只是获取元素 .text 才能获取文本 而获得属性值：.get_attribute("href")
xpath1 = driver.find_element_by_xpath("//div[@id='anony-nav']/h1/a")
print(xpath1.text)

xpath2 = driver.find_elements_by_tag_name("h2")
print(xpath2[0].text)


link = driver.find_elements_by_link_text("一生难忘一碗面")
print(link[0].get_attribute('href'))

driver.close()

# 根据xpath定位元素:driver.find_elements_by_xpath("//*[@id='s']/h1/a")
# 根据class定位元素:driver.find_elements_by_class_name("box")
# 根据link_text定位元素:driver.find_elements_by_link_text("下载豆瓣 App")
# 根据tag_name定位元素:driver.find_elements_by_tag_name("h1")
# 获取文本内容:element.text
# 获取标签属性: element.get_attribute("href")