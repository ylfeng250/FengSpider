"""
以豆瓣电影为例谈谈如何抓取由ajax传输的数据
"""

from urllib import request,parse
import chardet
import json


def get_taglist(url):
    # 设置请求头部
    headers = {
        "Referer":"https://movie.douban.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "X-Requested-With":"XMLHttpRequest"
    }

    req = request.Request(url,headers=headers)

    data = request.urlopen(req).read()
    data = data.decode(chardet.detect(data)['encoding']) # 查看返回的编码类型
    data = json.loads(data)
    return data["tags"]

def get_tag_items(tagname):
    query = {
        "type":"movie",
        "tag":tagname,
        "page_limit":50,
        "page_start":0
    }
    urlquery = parse.urlencode(query)
    url = "https://movie.douban.com/j/search_subjects?" + urlquery
     # 设置请求头部
    headers = {
        "Referer":"https://movie.douban.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    }
    req = request.Request(url,headers=headers)
    data = request.urlopen(req).read()
    data = data.decode(chardet.detect(data)['encoding']) # 查看返回的编码类型
    data = json.loads(data) # 转json
    print(data)
def main():
    # 获取tag
    url1 = "https://movie.douban.com/j/search_tags?type=movie&source=index"
    tags = get_taglist(url1)
    for tag in tags:
        print(tag)
        get_tag_items(tag)

if __name__ == "__main__":
    main()