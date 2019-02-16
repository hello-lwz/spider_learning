import time
from multiprocessing import JoinableQueue as Queue
import requests
from lxml import etree
from multiprocessing import Process

# 不建议使用 频率太快容易被封禁

class spider_process:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        self.url = 'https://www.qiushibaike.com/text/page/{}/'
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.data_queue = Queue()

    def url_list(self):
        print('1')
        for i in range(1,14):
            self.url_queue.put(self.url.format(i))

    def parse_url(self):
        print('2')
        while True:
            url = self.url_queue.get()
            response = requests.get(url,headers = self.headers)
            self.html_queue.put(response.content.decode())
            self.url_queue.task_done()

    def get_data(self):
        print('3')
        while True:
            html_str = self.html_queue.get()
            html = etree.HTML(html_str)
            data = html.xpath("//div[@class='content']/span/text()")
            self.data_queue.put(data)
            self.html_queue.task_done()

    def save_data(self):
        print('4')
        while True:
            with open('xiushi2.txt','a', encoding='utf-8') as f:
                data = self.data_queue.get()
                for i in data:
                    f.write(i.repalce('\n\n\n','')+'\n')
                self.data_queue.task_done()

    def run(self):
        process_list = []
        # 获取url 添加到进程列表
        url_t = Process(target=self.url_list)
        process_list.append(url_t)

        # 解析url 添加到进程列表中
        for i in range(3):# 创建3个子进程
            parse_url_t = Process(target=self.parse_url)
            process_list.append(parse_url_t)

        # 获取数据 添加到进程列表中
        data_t = Process(target=self.get_data)
        process_list.append(data_t)

        # 保存数据 添加到进程列表中
        save_date_t = Process(target=self.save_data)
        process_list.append(save_date_t)

        for t in process_list:
            # t.daemon = True
            t.start()

        for i in [self.url_queue,self.html_queue,self.data_queue]:
            i.join() # 进程阻塞等待

        print('----主进程结束----')

if __name__ == '__main__':
    begin = time.time()
    xiushi_process = spider_process()
    xiushi_process.run()
    end = time.time()
    print(end-begin)

