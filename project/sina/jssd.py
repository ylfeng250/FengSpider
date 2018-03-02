"""
军事深度
通过 F12开发者工具探知正确的访问接口
http://platform.sina.com.cn/news/news_list?app_key=2872801998&channel=mil&cat_1=jssd&show_all=0&show_cat=1&show_ext=1&tag=1&format=json&page=5&show_num=10&callback=jQuery191032227597860790613_1509022011977&_=1509022011987
"""
from urllib import request
from bs4 import BeautifulSoup
import json
# 最后那个参数自己设置
url = "http://platform.sina.com.cn/news/news_list?app_key=2872801998&channel=mil&cat_1=jssd&show_all=0&format=json&show_num=6000"

html = request.urlopen(url).read()

datas = json.loads(html)["result"]["data"]
print(type(datas))
# print(json_data["data"])
f = open("./jssd/urllist.md","a+",encoding="utf8")
for data in datas:
    title = data["title"]
    url = data["url"]
    f.write("["+title+"]("+url+")\n")


f.close()