import requests
import re
import random
import tomd # 用来将html转换成md
import os

url = "http://blog.csdn.net/qq_14998713/article/details/79166335" # 测试url
useragents = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
]
headers = {
    'Host': 'blog.csdn.net',
    'Referer': 'http://blog.csdn.net/',
    'User-Agent': random.choice(useragents)
}

res = requests.get(url=url,headers=headers).text
title = re.findall(r'<title>(.*)</title>',res,re.S|re.M)[0]
html_script = r'<div class="markdown_views">(.+)</article>' # 匹配csdn中博客正文的正则表达式，比较简陋
html = re.findall(html_script,res,re.S|re.M)[0]
# 提取正文并转换成md
article = tomd.convert(html)

pwd = os.getcwd() # 获取当前文件的路径
dirpath = pwd + '/csdn/'
if not os.path.exists(dirpath):# 判断目录是否存在，不存在则创建新的目录
    os.makedirs(dirpath)
with open(dirpath+title+'.html','w',encoding='utf8') as f:
    f.write(html) # 创建html页面
with open(dirpath+title+'.md','w',encoding="utf8") as f:
    f.write(article) # 创建markdown文件

