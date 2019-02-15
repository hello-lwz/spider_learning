import re

title = u'你好，hello，世界'
# pattern = re.compile(r'[\u4e00-\u9fa5]+')
result = re.findall(r'[\u4e00-\u9fa5]+',title)

print(result)