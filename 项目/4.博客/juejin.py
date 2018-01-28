import requests
import re
import html2text
from bs4 import BeautifulSoup
import random
import os


def juejinDownDLoad(url):
    useragents = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    ]
    headers = {
        'Host': 'juejin.im',
        'Referer': 'https://juejin.im/',
        'User-Agent': random.choice(useragents)
    }
    res = requests.get(url=url,headers=headers).text # 获取整个html
    h = html2text.HTML2Text()
    h.ignore_links = False
    soup = BeautifulSoup(res,'lxml')
    title = soup.find('title').text
    print(title)
    html = soup.find(class_='post-content-container')
    print(html)
    # 提取正文并转换成md
    article = h.handle(str(html))
    pwd = os.getcwd() # 获取当前文件的路径
    dirpath = pwd + '/juejin/'
    if not os.path.exists(dirpath):# 判断目录是否存在，不存在则创建新的目录
        os.makedirs(dirpath)
    with open(dirpath+title+'.html','w',encoding='utf8') as f:
        f.write(str(html)) # 创建html页面
    with open(dirpath+title+'.md','w',encoding="utf8") as f:
        f.write(article) # 创建markdown文件
if __name__ == "__main__":
    url = "https://juejin.im/post/5a68437b6fb9a01ca47aabc6" # 测试用例
    juejinDownDLoad(url)