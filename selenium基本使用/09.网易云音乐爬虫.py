import time
from selenium import webdriver


class cloud_music_spider:
    def __init__(self):
        self.url = 'https://music.163.com/#/discover/playlist'
        # 不打开窗口调用chrome
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    # 提取数据
    def get_content_list(self):
        # 切换iframe
        frame = self.driver.find_element_by_id("g_iframe")
        self.driver.switch_to.frame(frame)

        li_list = self.driver.find_elements_by_xpath('//ul[@id="m-pl-container"]/li')
        content_list= []
        for li in li_list:
            item = {}
            item['title'] = li.find_element_by_xpath("./p/a").get_attribute("title")
            item['href'] = li.find_element_by_xpath("./p/a").get_attribute("href")
            content_list.append(item)

        # 提取下一页的元素
        next_url = self.driver.find_elements_by_xpath("//a[@class = 'zbtn znxt']")
        next_url = next_url[0] if len(next_url) > 0 else None
        js = 'window.scrollTo(0,document.body.scrollHeight)'  # js语句：滚动到页面最底部
        self.driver.execute_script(js)  # 执行js的方法
        # print(next_url)
        return content_list, next_url

    def save_content_data(self,content_list):
        with open('cloud_music.txt', 'a', encoding='utf-8') as f:
            for content in content_list:
                f.write(str(content)+'\n')

    def run(self):
        self.driver.get(self.url)
        content_list,next_url = self.get_content_list()
        self.save_content_data(content_list)

        while next_url is not None:
            next_url.click()
            time.sleep(3)

            # 此时在iframe标签中 代码逻辑需要我们先切出
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[0])

            content_list, next_url = self.get_content_list()
            self.save_content_data(content_list)

if __name__ == '__main__':
    cloud_music = cloud_music_spider()
    cloud_music.run()