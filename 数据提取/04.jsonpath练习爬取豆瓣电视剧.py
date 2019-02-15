import json

import requests
from jsonpath import jsonpath

headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
url = 'https://m.douban.com/tv/american'

response = requests.get(url,headers=headers)
html_str = response.content.decode()
print(html_str)

# html_dict = json.loads(html_str)
# print(jsonpath(html_str,'$..item'))