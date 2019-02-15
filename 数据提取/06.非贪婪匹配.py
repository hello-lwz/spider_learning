import re

s = '123xxxxxx456'

result_1 = re.search('\d+', s).group()
result_2 = re.search('\d+?', s).group()

print(result_1)
print(result_2)