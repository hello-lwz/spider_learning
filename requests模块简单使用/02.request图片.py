import requests

url = 'https://www.baidu.com/img/bd_logo1.png'

response = requests.get(url)

with open('baidu.png','wb') as f:
    f.write(response.content)
        # content 是byte类型 二进制