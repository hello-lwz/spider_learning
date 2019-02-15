import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

url = 'https://fanyi.baidu.com/'
# proxies = {
#       "http": "http://12.34.56.79:9527",
#       "https": "https://12.34.56.79:9527",
#       }
data = {'kw':'hello'}
reponse = requests.post(url,headers=headers,data=data)

print(reponse.content.decode())