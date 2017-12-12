import random
import re

import requests


# 发起请求,


def get_request(url, user_agent):
    headers = {
        'Host': "v.youku.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        'Cache-Control': 'no-cache',
        "Connection": "keep-alive",
        "User-Agent": user_agent,
        'Referer': 'http://www.youku.com/'
    }
    try:
        html = requests.get(url, headers=headers, timeout=20).text
        return html
    except Exception as e:
        print(e)
        return -1

if __name__ == '__main__':
    # 视频播放的网页链接
    url = "http://v.youku.com/v_show/id_XMzIyMjk4MDcwMA==.html?spm=a2hww.20027244.m_250036.5~5!2~5~5!3~5~5~A&f=51249681"

    user_agent_list = ['Mozilla/4.0 (compatible; GoogleToolbar 6.1.1518.856; Windows XP 5.1; MSIE 8.0.6001.18702)','Mozilla/4.0 (compatible; MSIE 5.0; Mac_PowerPC; AtHome021)']
    user_agent = random.choice(user_agent_list)

    # 获取网页源码
    html_body = get_request(url, user_agent)
    # 查找真正的播放链接
    print(re.findall('http://player.youku.com/player.php/[A-Za-z0-9=/_]*/v.swf', html_body))

    # 将打印出来的播放链接直接在浏览器打开就可以观看视频，还没有过滤掉广告