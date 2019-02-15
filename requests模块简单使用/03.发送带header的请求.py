import requests

url = 'https://www.baidu.com'

response = requests.get(url)

print(response.content)
# 打印响应对应的请求的头
print(response.request.headers)