"""
抓取代理ip
目标网站:www.xicidaili.com
"""
from urllib import request
import re

def getproxy():
    # 匹配ip和端口号
    pattern1 = '<td>([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})</td>'
    pattern2 = '<td>([0-9]{1,5})</td>'
    proxy = []
    url = "http://www.xicidaili.com/"
    req=request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

    html = request.urlopen(req).read().decode("utf8")
    ips = re.findall(pattern1,html)
    ports = re.findall(pattern2,html)
    for i in range(len(ips)):
        proxy.append(ips[i]+":"+ports[i])

    return proxy

if __name__ == "__main__":
    proxy=getproxy()
    print(proxy)

