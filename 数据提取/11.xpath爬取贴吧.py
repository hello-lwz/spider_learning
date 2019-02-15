import requests
from lxml import etree

# 贴吧极简版 提取帖子标题和链接
class spider:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    def parse_url(self,i): # 发送请求 获取响应
        url = 'http://tieba.baidu.com/mo/q---F5237104801464AE3DDE5DC245293218%3AFG%3D1--1-1-0--2--wapp_1550217457649_235/m?kw=qq%E5%8D%8E%E5%A4%8F&lp=5011&lm=&pn={}'.format(i)
        response = requests.get(url,headers=self.headers)
        html_str = response.content
        return html_str

    def get_data(self,html_str): # 提取数据
        html = etree.HTML(html_str)
        a_list = html.xpath("//body/div/div[@class='i']/a")
        content_list = []
        href_prex='http://tieba.baidu.com/mo/q---F5237104801464AE3DDE5DC245293218%3AFG%3D1--1-1-0--2--wapp_1550217457649_235/'
        for a in a_list:
            item={}
            item['title'] = a.xpath('./text()')[0][3:].replace('\xa0','')
            item['href'] = href_prex + a.xpath('./@href')[0]
            content_list.append(item)
        return content_list

    def save_content_list(self,content_list):
        for content in content_list:
            print(content)

    def run(self):
        for i in range(10):
            html_str = self.parse_url(i*10)
            content_list = self.get_data(html_str)
            self.save_content_list(content_list)

if __name__ == '__main__':
    tieba = spider()
    tieba.run()

