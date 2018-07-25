import requests
import time
from bs4 import BeautifulSoup


def ecnu_spider(tar_url):
    # 发起请求
    res = requests.get(url=tar_url)
    if res.status_code == "404":
        return
    # 设置编码
    res.encoding = "utf-8"
    # 创建soup对象
    soup = BeautifulSoup(res.text,"html5lib")
    a_list = soup.find_all("a", class_="col-news-item")

    for item in a_list:
        title = item.find_all("span",class_="col-news-title")[0].get_text() # 报告的主题
        url = base_url + item["href"] # 详情地址
        time = item.find_all("span",class_="lecture-date")[0].get_text() # 报告的时间
        # 写入文件
        write2txt(filename,title,url,time)

def write2txt(filename,title,url,time):
    with open(filename,"a+",encoding="utf8") as file:
        file.write(time+"\n")
        file.write(title+"\n")
        file.write(url+"\n")
        file.write("=====================================\n")


if __name__ == "__main__":
    base_url = "http://www.ecnu.edu.cn"
    filename = "page.txt"
    for i in range(262):
        tar_url = base_url + '/jzbg/list'+str(i+1)+'.htm'
        ecnu_spider(tar_url)
        time.sleep(1)
        print(i)
        