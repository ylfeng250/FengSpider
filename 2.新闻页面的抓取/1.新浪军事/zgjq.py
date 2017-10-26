"""
# 中国军情
# http://roll.mil.news.sina.com.cn/col/zgjq/index.shtml

# 对应文章列表页的URL
# http://roll.mil.news.sina.com.cn/col/zgjq/index_0.shtml 只要改变数字就好了

# MD发现按照日期分类的了
http://roll.mil.news.sina.com.cn/col/zgjq/2017-10-15.shtml
# 对应文章也的URL
# http://mil.news.sina.com.cn/china/2017-10-24/doc-ifymzksi1470524.shtml

# 根据日期进行存储，判断span标签的class为time
# a = "(10月24日 17:34)"
# print(a[1:8])
"""

import random
from urllib import request
from bs4 import BeautifulSoup
from getproxy import getproxy
import re
days = [31,28,31,30,31,30,31,31,30,31,30,31]
topic = "zgjq"
# UserAgents
useragents = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063"
]
# 代理
proxys = getproxy()
def createURL(i,j):
     # 构造url 方法有点low啊
    if i<10:
        if j<10:
            url = "http://roll.mil.news.sina.com.cn/col/"+topic+"/2017-0" + str(i) +"-0"+str(j)+".shtml"
            filename="20170"+str(i)+"0"+str(j)
        else:
            url = "http://roll.mil.news.sina.com.cn/col/"+topic+"/2017-0" + str(i) +"-"+str(j)+".shtml"
            filename="20170"+str(i)+str(j)
    else:
        if j<10: 
            url = "http://roll.mil.news.sina.com.cn/col/"+topic+"/2017-" + str(i) +"-0"+str(j)+".shtml"
            filename="2017"+str(i)+"0"+str(j)
        else:
            url = "http://roll.mil.news.sina.com.cn/col/"+topic+"/2017-" + str(i) +"-"+str(j)+".shtml"
            filename="2017"+str(i)+str(j)
    return url,filename

def createFilename(i,j):
    if i<10:
        if j<10:
            filename="20170"+str(i)+"0"+str(j)
        else:
            filename="20170"+str(i)+str(j)
    else:
        if j<10:
            filename="2017"+str(i)+"0"+str(j)
        else:
            filename="2017"+str(i)+str(j)


def main():
    count = 0
    for i in range(1,11):
        for j in range(1,days[i-1]+1):
            url,filename = createURL(i,j)
            # filename = createFilename(i,j)
            f = open("./zgjq/"+filename+".md","a+",encoding="utf8")
            print("url:"+url)

            # # 设置代理服务器的信息
            # proxy =  request.ProxyHandler({
            #     'http':random.choice(proxys)
            # })
            # # 自定义opener对象，第一个参数是代理信息，第二个参数是urllib.request.HTTPHandler类
            # opener = request.build_opener(proxy,request.HTTPHandler)
            # # 设置为全局的opener对象
            # request.install_opener(opener)

            headers={
                "User-Agent": random.choice(useragents)
            }
            req = request.Request(url,headers={})
            html = request.urlopen(req).read().decode("gbk")

            soup = BeautifulSoup(html,"html5lib")
            # 获取页面中的所有li标签
            ul_lists = soup.find_all('ul',{"class":"linkNews"})
            # patterns = '<li><a href="(http://mil\.news\.sina\.com\.cn/.*\.shtml)$"'
            for ul in ul_lists:
                for a in ul.find_all("a"):
                    href = a["href"]
                    topic = a.get_text()
                    f.write("["+topic+"]("+href+")\n")
                    print(href)

if __name__=="__main__":
    main()