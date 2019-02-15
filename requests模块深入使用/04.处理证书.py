import requests

headers = {
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

url = 'https://www.12306.cn/mormhweb/'

reponse = requests.get(url,headers=headers,verify=True,timeout=0.1)
                                    #timeout 最大延迟时间
print(reponse.content.decode())