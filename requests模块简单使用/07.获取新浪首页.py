import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

url = 'https://www.sina.com.cn/'

response = requests.get(url,headers=headers)

# print(response.text)
# 中文乱码

print(response.content.decode())