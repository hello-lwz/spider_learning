import json

mydict = {
    "store": {
        "book": [
            {"category": "reference",
             "author": "刘卫正",
             "title": "Sayings of the Century",
             "price": 8.95
             },
            {"category": "fiction",
             "author": "Evelyn Waugh",
             "title": "Sword of Honour",
             "price": 12.99
             },
        ],
    }
}

# json.dumps 实现python类型转化为json字符串
# indent实现换行和空格
# ensure_ascii=False实现让中文写入的时候保持为中文
json_str = json.dumps(mydict, indent=2, ensure_ascii=False)
print('json.dumps python_type-->json_str: {}'.format(type(json_str)))
print(json_str)

# json.loads 实现json字符串转化为python的数据类型
py_str = json.loads(json_str)
print('json.loads json_str-->python_type: {}'.format(type(py_str)))
print(py_str)

# json.dump 实现把python类型写入类文件对象
with open('py.txt','w') as f:
    json.dump(py_str,f,indent=2,ensure_ascii=False)

# json.load 实现把类文件对象中json类型转化为python类型
with open('py.txt','r') as f:
    py_str1 = json.load(f)
print('json.load 读取文件--> {}: {}'.format(type(py_str1), py_str1))
