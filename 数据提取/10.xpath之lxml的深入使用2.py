from lxml import etree

text = '''<div> <ul> 
<li class="item-1"><a>first item</a></li> 
<li class="item-1"><a href="link2.html">second item</a></li> 
<li class="item-inactive"><a href="link3.html">third item</a></li> 
<li class="item-1"><a href="link4.html">fourth item</a></li> 
<li class="item-0"><a href="link5.html">fifth item</a> 
</ul> </div>'''

html = etree.HTML(text)
href_list = html.xpath('//li[@class="item-1"]/a')
print(href_list)
title_list = html.xpath('//li[@class="item-1"]/a/text()')
# print(title_list)
# 这样取可能有的值取不到 则会发生错位 深入使用2会处理这个问题
#组装成字典
# for href in href_list:
#     item={}
#     item['href'] = href
#     item['title'] = title_list[href_list.index(href)]
#     print(item)
