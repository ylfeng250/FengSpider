
import random
import requests
import json
import time


first_url = 'https://m.douban.com/rexxar/api/v2/tv/26322642/interests?count=20&order_by=hot&start=0&ck=dNhr&for_mobile=1'
url = 'https://m.douban.com/rexxar/api/v2/tv/26322642/interests'
# 移动端头部信息
useragents = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/47.0.2526.70 Mobile/13C71 Safari/601.1.46",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)"
]


def visit_URL(i):
    print(">>>>>",i)
    # 请求头部
    headers = {
        'Host':'m.douban.com',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':random.choice(useragents)
    }
    params = {
        'count':'50',
        'order_by':'hot',
        'start':str(i),
        'for_mobile':'1',
        'ck':'dNhr'
    }
    res = requests.get(url=url,headers=headers,params=params)
    res_json = res.json()
    interests = res_json['interests']
    print(len(interests))
    for item in interests:
        with open('huge.txt','a',encoding='utf-8') as file:
            if item['user']:
                if item['user']['name']:
                    file.write('评论用户:'+item['user']['name']+'\n')
            else:
                file.write('评论用户:none\n')
            if item['create_time']:
                file.write('评论时间:'+item['create_time']+'\n')
            else:
                file.write('评论时间:none\n')
            if item['comment']:
                file.write('评论内容:'+item['comment']+'\n')
            else:
                file.write('评论内容:none\n')
            if item['rating']:
                if item['rating']['value']:
                    file.write('对电影的评分:'+str(item['rating']['value'])+'\n\n')
            else:
                file.write('对电影的评分:none\n')
    


if __name__ == '__main__':
    for i in range(0,66891,20):
        # time.sleep(2)
        visit_URL(i)