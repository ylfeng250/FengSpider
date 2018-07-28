import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import csv

ua = UserAgent() # 伪造useragent
base_url = "https://movie.douban.com/subject/27180959/comments"
filename = "lieduren.csv"
short_file = "short.txt"
fileheader = ["avatar", "time", "rating", "votes", "short"]

# 获取数据
def get_html(url,params):
    # 伪造请求头部
    headers = {
        "Host": "movie.douban.com",
        "User-Agent":ua.random,
        "Cookie":'ll="108296"; bid=jneE_fXDSR0; __utmc=30149280; __utmz=30149280.1532772528.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=223695111; __utmz=223695111.1532772541.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; __yadk_uid=RcrHQ7Cc3etveSKWQfwJABsWxbxIcewg; _vwo_uuid_v2=DACDCD8DF7E4D1CC8269E69F7E4343269|9679267a6e169e97cc3f276adb266cc2; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1532776537%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fq%3D%25E7%258C%258E%25E6%25AF%2592%25E4%25BA%25BA%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1233726059.1532772528.1532772528.1532776537.2; ap=1; __utma=223695111.1713399185.1532772541.1532772541.1532776605.2; __utmb=223695111.0.10.1532776605; as="https://www.douban.com/search?q=%E7%8C%8E%E6%AF%92%E4%BA%BA"; ps=y; dbcl2="161794981:mKVbVxpEvxI"; ck=e2lK; push_noty_num=0; push_doumail_num=0; __utmv=30149280.16179; __utmb=30149280.7.10.1532776537; _pk_id.100001.4cf6=f279b3b3de0a6985.1532772541.2.1532778019.1532774589.'
    }
    res = requests.get(url=url,params=params,headers=headers)
    if res.status_code == "403":
        print(403)
        return False
    res.encoding = "utf-8"
    html = res.text
    soup = BeautifulSoup(html,"lxml")
    div_list = soup.find_all("div",class_="comment-item")
    for div in div_list:
        # item = {}
        # item["avatar"] = div.find_all("a")[0]['title'].strip() # 评论者
        # item["time"] = div.find("span",class_="comment-time").get_text().strip() # 评论时间
        # # 有的没有rating和votes 这些就不要了
        # if(div.find("span",class_="rating")==None):
        #     print("kong")
        #     continue
        # item["rating"] = div.find("span",class_="rating")["title"].strip() # 评价
        # item["votes"] = div.find("span",class_="votes").get_text().strip() # 支持度
        # item["short"] = div.find("span",class_="short").get_text().strip() # 短评
        # write2csv(item,filename,fileheader)
        short = div.find("span",class_="short").get_text().strip() # 只为了生成评论
        with open("short.txt","a+",encoding="utf-8",newline="") as f:
            f.write(short+"\n")
        # print(item)
    return True

def write2csv(item,filename,fileheader):
    with open(filename,"a",encoding="utf-8",newline='') as csvFile:
        dict_writer = csv.DictWriter(csvFile, fileheader) # 创建字典写入对象
        dict_writer.writerow(item) # 写入


def main():
    for start in range(0,500,20):
        params = {
            'start': start,
            'limit': 20,
            'sort': "new_score",
            'status': "P"
        }
        flag = get_html(base_url,params)
        if flag == False:
            break
        # time.sleep(1) # 睡眠1秒
        print(start)
    print("抓取完成")

if __name__ == "__main__":
    main()