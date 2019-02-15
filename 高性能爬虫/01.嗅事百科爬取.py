import time

import requests
from lxml import etree


class xiushi_spider:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        self.url = 'https://www.qiushibaike.com/text/page/{}/'

    def url_list(self):
        return [self.url.format(i) for i in range(1,14)]

    def parse_url(self,url):
        response = requests.get(url,self.headers)
        html_str = response.content.decode()
        return html_str

    def get_data(self,html_str):
        html = etree.HTML(html_str)
        data = html.xpath("//div[@class='content']/span/text()")
        return data

    def save_data(self,data):
        with open('xiushi.txt','a',encoding='utf-8') as f:
            for i in data:
                f.write(i.replace('\n\n\n','')+'\n')

    def run(self):
        url_list = self.url_list()
        for url in url_list:
            # 请求url 获取数据
            html_str = self.parse_url(url)
            # 解析数据，得到想要的内容
            data = self.get_data(html_str)
            # 保存数据到txt
            self.save_data(data)

if __name__ == '__main__':
    begin = time.time()
    xiushi = xiushi_spider()
    xiushi.run()
    end = time.time()
    print(end-begin)