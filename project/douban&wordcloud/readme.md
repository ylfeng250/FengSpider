## 简介
猎毒人这个剧建议大家看看，虽然剧情没有什么可圈可点，但可以看出导演下了血本，就当是给友情出演的老戏骨一点支持，今天我爬取了豆瓣上猎毒人的评论数据，看看网友们是什么评价,虽然看剧的时候在弹幕上已经了解了大部分网友的想法，就当一次爬虫的实战演练吧！
![](https://user-gold-cdn.xitu.io/2018/7/28/164e061fc42d3f9d?w=270&h=385&f=png&s=212437)

## 目标分析

目标地址`https://movie.douban.com/subject/27180959/comments?start=20&limit=20&sort=new_score&status=P`

一共有4个参数，分别如下所示
| start    | limit      | new_score | status |
| :------- | :--------- | :-------- | :----- |
| 起始位置 | 返回的条数 | 排序方式  | 状态   |

查看了网页请求，直接返回的HTML，所以只要定位评论数据的位置就可以获取数据。我想获取的是这五部分数据

![](https://user-gold-cdn.xitu.io/2018/7/28/164e07df7ef29fa1?w=706&h=132&f=png&s=25375)
查看源代码定位需要的数据，初步看还是很简单的，只要通过class属性查找就行了

![](https://user-gold-cdn.xitu.io/2018/7/28/164e07fd226c29d6?w=1581&h=475&f=png&s=43344)

需要注意的地方是，有的用户没有给评分，所以在获取评分的时候需要判断，若没有评分就直接滤过(只有少量用户)。本文虽然抓取了评分数据，但是没有使用，为之后做准备

## 关于反爬
这次还是比较顺利的，只是用了随机更换UA，所以说很多教程都拿豆瓣开刀~~。这里推荐一个python的库用来随机更换UA，这样就不用自己收集了。

```
# 安装
pip install fake-useragent

# 用法简介

from fake_useragent import UserAgent
ua = UserAgent()

ua.ie
# Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US);
ua.msie
# Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)'
ua['Internet Explorer']
# Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)
ua.opera
# Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11
ua.chrome
# Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
ua.google
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13
ua['google chrome']
# Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11
ua.firefox
# Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1
ua.ff
# Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1
ua.safari
# Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25

# and the best one, random via real world browser usage statistic
ua.random
```

## 开始爬取

源码
```python
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import csv

ua = UserAgent() # 伪造useragent
base_url = "https://movie.douban.com/subject/27180959/comments"
filename = "lieduren.csv"
fileheader = ["avatar", "time", "rating", "votes", "short"]

# 获取数据
def get_html(url,params):
    # 伪造请求头部
    headers = {
        "Host": "movie.douban.com",
        "User-Agent":ua.random,
    }
    res = requests.get(url=url,params=params,headers=headers)
    if res.status_code == "403":
        return False
    res.encoding = "utf-8"
    html = res.text
    soup = BeautifulSoup(html,"lxml")
    div_list = soup.find_all("div",class_="comment-item")
    for div in div_list:
        item = {}
        item["avatar"] = div.find_all("a")[2].get_text().strip() # 评论者
        item["time"] = div.find("span",class_="comment-time").get_text().strip() # 评论时间
        # 有的没有rating和votes 这些就不要了
        if(div.find("span",class_="rating")==None):
            print("kong")
            continue
        item["rating"] = div.find("span",class_="rating")["title"].strip() # 评价
        item["votes"] = div.find("span",class_="votes").get_text().strip() # 支持度
        item["short"] = div.find("span",class_="short").get_text().strip() # 短评
        write2csv(item,filename,fileheader)
        # print(item)
    return True

def write2csv(item,filename,fileheader):
    with open(filename,"a",encoding="utf-8",newline='') as csvFile:
        dict_writer = csv.DictWriter(csvFile, fileheader) # 创建字典写入对象
        dict_writer.writerow(item) # 写入


def main():
    for start in range(0,10000,20):
        params = {
            'start': start,
            'limit': 20,
            'sort': "new_score",
            'status': "P"
        }
        flag = get_html(base_url,params)
        if flag == False:
            break
        time.sleep(1) # 睡眠1秒
        print(start)
    print("抓取完成")

if __name__ == "__main__":
    main()
```

## 生成词云

![](https://user-gold-cdn.xitu.io/2018/7/28/164e0f925134e6ca?w=618&h=486&f=png&s=164641)

![](https://user-gold-cdn.xitu.io/2018/7/28/164e0f94c8c26ec1?w=640&h=476&f=png&s=98235)

```python
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from os import path
import matplotlib.pyplot as plt
import jieba
import jieba.posseg as pseg
from PIL import Image
import numpy as np
d = path.dirname(__file__)
stopwords = set(STOPWORDS)
# 中文分词处理
def processChinese(text):  
    seg_generator = jieba.cut(text)
    seg_list = [i for i in seg_generator if i not in stopwords]  # 排除stopwords
    seg_list = [i for i in seg_list if i != '\n']  # 排除换行
    seg_list = r' '.join(seg_list)
    return seg_list

def  main():
    # 读取文本
    text = open('short.txt', encoding = 'utf-8').read()
    # 读取图片
    alice_mask = np.array(Image.open(path.join(d, "xx.png")))
    # jieba分词
    text = processChinese(text)
    fontpath = "./SourceHanSerifK-Light.otf"
    wordcloud = WordCloud(font_path = fontpath,background_color='white',mask=alice_mask,max_words=200).generate(text)
    # 绘制
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

main()
```
从词云可以看出，大家对这部剧的评价主要集中在（**剧情**，**演技**，**演员**，**编剧**，**女主**，**阵容**）

情感分析还没有仔细研究过，看过这剧的我只服导演的脑洞和老戏骨的能力。

------
欢迎关注我的孙女叫小芳的微信公众号~~

![](https://user-gold-cdn.xitu.io/2018/7/28/164e0fdfb5d4b2fb?w=344&h=344&f=jpeg&s=8465)
