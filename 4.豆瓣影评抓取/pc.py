"""
抓取豆瓣电影 蜘蛛侠：英雄归来 的短评
pc版
"""
import requests
from bs4 import BeautifulSoup


first_url = 'https://movie.douban.com/subject/26322642/comments?status=P'


# 请求头部
headers = {
    'Host':'movie.douban.com',
    'Referer':'https://movie.douban.com/subject/24753477/?tag=%E7%83%AD%E9%97%A8&from=gaia_video',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
}

def visit_URL(url):
    res = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(res.content,'html5lib')
    div_comment = soup.find_all('div',class_='comment-item') # 找到所有的评论模块
    for com in div_comment:
        username = com.find('div',class_='avatar').a['title']
        comment_time = com.find('span',class_='comment-time')['title']
        votes = com.find('span',class_='votes').get_text()
        comment = com.p.get_text()
        with open('1.txt','a',encoding='utf8') as file:
            file.write('评论人：'+username+'\n')
            file.write('评论时间：'+comment_time+'\n')
            file.write('支持人数：'+votes+'\n')
            file.write('评论内容：'+comment+'\n')

    # 检查是否有下一页
    next_url = soup.find('a',class_='next')
    if next_url:
        temp = next_url['href'].strip().split('&amp;') # 获取下一个url
        next_url = ''.join(temp)
        print(next_url)
    # print(next_url)
    if next_url:
        visit_URL('https://movie.douban.com/subject/24753477/comments'+next_url)


if __name__ == '__main__':
    visit_URL(first_url)