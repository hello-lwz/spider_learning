import time

from selenium import webdriver


class douyu_spider:
    def __init__(self):
        self.url = 'https://www.douyu.com/directory/all'
        # 不打开窗口调用chrome
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    # 提取数据
    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath("//ul[@class='layout-Cover-list']/li")
        content_list= []
        for li in li_list:
            item = {}
            item['title'] = li.find_element_by_xpath(".//h3").get_attribute("title")
            item['author'] = li.find_element_by_xpath(".//h2").text
            item['watch_num'] = li.find_element_by_xpath(".//span[@class='DyListCover-hot']").text
            content_list.append(item)

        # 提取下一页的元素
        next_url = self.driver.find_elements_by_xpath("//li[contains(@aria-disabled, 'false') and (@title = '下一页')]/span")
        next_url = next_url[0] if len(next_url) > 0 else None
        # print(next_url)
        return content_list, next_url

    def save_content_data(self,content_list):
        with open('douyu.txt', 'a', encoding='utf-8') as f:
            for content in content_list:
                f.write(str(content)+'\n')

    def run(self):
        self.driver.get(self.url)
        content_list,next_url = self.get_content_list()
        self.save_content_data(content_list)

        while next_url is not None:
            next_url.click()
            time.sleep(3)
            content_list, next_url = self.get_content_list()
            self.save_content_data(content_list)

if __name__ == '__main__':
    douyu = douyu_spider()
    douyu.run()