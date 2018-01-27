import requests
import re
import random
import os
import html2text


def jianshuDownLoad(url):
    useragents = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    ]
    headers = {
        'Host': 'www.jianshu.com',
        'Referer': 'https://www.jianshu.com/',
        'User-Agent': random.choice(useragents)
    }
    h = html2text.HTML2Text()
    h.ignore_links = False

    res = requests.get(url=url,headers=headers).text
    title = re.findall(r'<title>(.*)</title>',res,re.S|re.M)[0]
    html_script = r'<div class="article">(.*)<div class="support-author">' # 匹配csdn中博客正文的正则表达式，比较简陋
    html = re.findall(html_script,res,re.S|re.M)[0]
    html = re.sub('(src=")|(data-original-src=")','src="https:',html)
    # 提取正文并转换成md
    article = h.handle(html)

    pwd = os.getcwd() # 获取当前文件的路径
    dirpath = pwd + '/jianshu/'
    if not os.path.exists(dirpath):# 判断目录是否存在，不存在则创建新的目录
        os.makedirs(dirpath)
    # 创建html页面
    with open(dirpath+title+'.html','w',encoding='utf8') as f:
        f.write(html) 
    # 创建md文件
    with open(dirpath+title+'.md','w',encoding="utf8") as f:
        lines = article.splitlines()
        for line in lines:
            if line == "![](https://upload-":
                f.write(line)
            else:
                f.write(line+"\n")

if __name__ == "__main__":
    url = "https://www.jianshu.com/p/b6220e99df2d" # 测试url
    jianshuDownLoad(url)