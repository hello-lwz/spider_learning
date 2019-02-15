import requests
from retrying import retry

headers = {
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

# 让函数报错后继续重新执行，达到最大执行次数的上限，如果每次都报错，整个函数报错，如果中间有一个成功，程序继续往后执行
@retry(stop_max_attempt_number=3)  # 3次重试
def _parse_url(url):
    # 超时报错并重试
    response = requests.get(url, headers=headers, timeout=3)
    # 状态码不是200也要重试
    assert response.status_code== 200
    return response

def parse_url(url):
    try:    # 捕获异常
        response = _parse_url(url)
    except Exception as e:
        print(e)
        # 报错 返回None
        response = None
    return response.content.decode()
print(parse_url('https://www.12306.cn/mormhweb/'))

# reponse = requests.get(url,headers=headers,verify=True,timeout=0.1)
#                                     #timeout 最大延迟时间
# print(reponse.content.decode())