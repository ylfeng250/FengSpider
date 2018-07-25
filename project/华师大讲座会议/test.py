"""
测试网页接口
"""
import requests
from bs4 import BeautifulSoup

base_url = "http://www.ecnu.edu.cn"

list_url = "/jzbg/" # 讲座报告

res = requests.get(url="http://www.ecnu.edu.cn/jzbg/list.htm")
res.encoding = "utf-8" # 转化编码
soup = BeautifulSoup(res.text,"html5lib")
a_list = soup.find_all("a", class_="col-news-item")

for item in a_list:
    title = item.find_all("span",class_="col-news-title")[0].get_text() # 报告的主题
    url = base_url + item["href"] # 详情地址
    time = item.find_all("span",class_="lecture-date")[0].get_text() # 报告的时间
    # print(title)
    # print(url)
    # print(time)
    # print("--------------")