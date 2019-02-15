import time
from queue import Queue
import threading
import requests
from lxml import etree


class xiushi_spider:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        self.url = 'https://www.qiushibaike.com/text/page/{}/'
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.data_queue = Queue()

    def url_list(self):
        for i in range(1, 14):
            self.url_queue.put(self.url.format(i))

    def parse_url(self):
        while True:
            url = self.url_queue.get()
            response = requests.get(url,self.headers)
            html_str = response.content.decode()
            self.html_queue.put(html_str)
            self.url_queue.task_done()

    def get_data(self):
        while True:
            html_str = self.html_queue.get()
            html = etree.HTML(html_str)
            data = html.xpath("//div[@class='content']/span/text()")
            self.data_queue.put(data)
            self.html_queue.task_done()

    def save_data(self):

        while True:
            f = open('xiushi.txt', 'a', encoding='utf-8')
            data = self.data_queue.get()
            for i in data:
                f.write(i.replace('\n\n\n','')+'\n')
            self.data_queue.task_done()
            f.close()

    def run(self):
        threading_list=[]
        # url_lsit_task
        url_t = threading.Thread(target=self.url_list)
        threading_list.append(url_t)

        for i in range(3):
            # 开启三个线程发送请求
            parse_url_t = threading.Thread(target=self.parse_url)
            threading_list.append(parse_url_t)

        # 解析数据，得到想要的内容
        get_data_t = threading.Thread(target=self.get_data)
        threading_list.append(get_data_t)

        # 保存数据到txt
        save_data_t = threading.Thread(target=self.save_data)
        threading_list.append(save_data_t)

        for t in threading_list:
            t.setDaemon(True) # 守护线程 保证主线程结束 子线程也结束
            t.start()

        for q in [self.data_queue,self.html_queue,self.url_queue]:
            q.join() # 设置阻塞等待 等待队列为空 避免子线程还未结束 主线程就结束
        print('-------主线程结束----------')

if __name__ == '__main__':
    begin = time.time()
    xiushi = xiushi_spider()
    xiushi.run()
    end = time.time()
    print(end-begin)

# 节省一半时间