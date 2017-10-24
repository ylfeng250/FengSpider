"""
抓取新浪军事有关的网页URL
最后失败了，需要再完善完善
"""
from urllib import request,parse
from bs4 import BeautifulSoup
import re
from urllib.error import HTTPError,URLError
def getNews(url):
    # 获取html页面
    html = request.urlopen(url).read().decode("utf-8","ignore")
    # 解析
    soup = BeautifulSoup(html,"html5lib")

    print("get:"+url)                
    

def dfs(url):

    pattern1 = 'http://(roll\.)?mil\.news\.sina\.com\.cn\/[a-z0-9_\/\.]*$'     #可以继续访问的url规则  
    pattern2 = 'http://mil\.news\.sina\.com\.cn\/[a-z0-9]+\/[0-9]{4}-[0-9]{2}-[0-9]{2}\/[a-z0-9_\/\.]*shtml$'  #解析新闻信息的url规则
    #如果页面访问过就返回
    if url in visited:  return
   

    try:
        # 这个url没有被访问过，那就访问一下
        html = request.urlopen(url).read().decode('utf-8','ignore')
        soup = BeautifulSoup(html,"html5lib")

        if re.match(pattern2,url):
            getNews(url)
             # 将url 放入已访问的队列
            print(url)
            visited.add(url)
        

        #提取该页面其中所有的url  
        links = soup.findAll('a', href=re.compile(pattern1))  
        for link in links:  
            # print(link['href'])  
            if link['href'] not in visited:   
                dfs(link['href']) 
    except HTTPError as e:  
        print(e)  
        return  
    except URLError as e:  
        print(e)  
        return  




visited = set()  ##存储访问过的url  
url = "http://mil.news.sina.com.cn/"
dfs(url)