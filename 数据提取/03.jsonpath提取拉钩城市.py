import json

import requests
from jsonpath import jsonpath

headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'

response = requests.get(url,headers=headers)
html_str = response.content.decode()

html_dict = json.loads(html_str)
country = jsonpath(html_dict,'$..name')

with open('country','w') as f:
    json.dump(country,f,ensure_ascii=False)
    