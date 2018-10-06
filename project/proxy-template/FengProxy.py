"""
@author 我的孙女叫小芳
@date 2018-10-06
@description：获取代理 然后通过代理进行原始数据的获取
"""
import requests
import re
import time
from fake_useragent import UserAgent
import random


class FengProxy():

    def __init__(self):
        self.proxy_url = "http://www.xicidaili.com/wt/" ## 西刺代理
        self.content = ""
        self.proxy_list = [] ## 代理列表
        self.ua = UserAgent()
        self.getproxy()
        # print(self.proxy_list)
    
    def getproxy(self):
        ## 获取代理页源码
        url = self.proxy_url + "1" ## 只需要第一页
        headers = {
            "User-Agent": self.ua.random
            }
        try:
            html = requests.get(url=url,headers=headers).text ## 获取返回的源码
        except:
            print("获取代理失败。。。。")
        
        ## 通过正则表达式获取代理
        regx = r'alt="Cn" /></td>(\s*)<td>(.+)</td>(\s*)<td>(\d+)</td>' ## 需要通过 \s*过滤空白符
        pattern = re.compile(regx,re.M)
        tmp_list = pattern.findall(html)
        for tmp in tmp_list:
            proxy = "http://"+tmp[1]+":"+tmp[3]
            self.proxy_list.append(proxy)
        
    def get(self,url,params=None,headers=None,proxies=None,timeout=20,checkCount=5):
        """
        url 请求的地址
        params 请求的方式 kv
        proxies 代理
        timeout 超时时间
        尝试次数 默认 5次
        """
        print("开始请求",url)
        if headers == None:
            headers={'User-Agent':self.ua.random}
        if proxies == None:
            ## 在没有代理的情况下
            try:
                self.content = requests.get(url=url,headers=headers,params=params,timeout=timeout).text
            except:
                if checkCount > 0:
                    time.sleep(5) ## 睡眠5秒
                    return self.get(url=url,params=params,headers=headers,timeout=timeout,checkCount=checkCount-1)
                else:
                    ## 尝试超过5次之后开始添加代理
                    time.sleep(5)
                    proxy = {"http":random.choice(self.proxy_list)} ## 随机选择一个代理
                    self.get(url=url,params=params,headers=headers,proxies=proxy,timeout=timeout) ## 发送含有代理的请求
        else:
            try:
                self.content = requests.get(url=url,headers=headers,params=params,proxies=proxies,timeout=timeout).text
            except:
                if checkCount > 0:
                    time.sleep(5)
                    proxy = {"http":random.choice(self.proxy_list)} ## 随机选择一个代理
                    print("正在更换代理。。。。")
                    print("当前代理是：",proxy)
                    self.get(url=url,params=params,headers=headers,proxies=proxy,timeout=timeout,checkCount=checkCount-1)


    def post(self):
        pass
        

download = FengProxy()
download.get("http://www.baidu.com")

print(download.content)

