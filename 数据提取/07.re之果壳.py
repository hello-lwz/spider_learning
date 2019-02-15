import re

import requests

headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
for i in range(1,10):
    url = 'https://www.guokr.com/ask/highlight/?page={}'.format(i)
    response = requests.get(url,headers=headers)
    html_str = response.content.decode()
# print(html_str)

    h2 = re.findall(r'<h2><a target="_blank".*?</h2>',html_str)
    print(h2)
 
