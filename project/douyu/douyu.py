#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2018/12/08 11:50:05
@Author  :   我的孙女叫小芳 
@Contact :   1119030015@qq.com
'''

# here put the import lib
import socket
import struct
import time
import re
from threading import Thread
import requests

class Douyu():
    def __init__(self,url="475252"):
        print("==============start================")
        # 房间号
        self.url = str(url)
        # ip
        # self.ip = "openbarrage.douyutv.com"
        # 2019-12-11 修改 服务器连接地址 上述域名应该不再使用
        # 感谢 @梅子酒 提供最新的ip地址
        self.ip = "119.96.201.28"
        # 端口号
        self.port = 8601
        self.get_info()

        print(f"=======您现在正在接收{self.room_id}房间的弹幕数据==========")
    def get_info(self):
        base_url = "http://open.douyucdn.cn/api/RoomApi/room/"
        if self.url.isdigit():
            self.room_id = self.url
        else:
            self.room_id = self.url.strip().split('/')[-1]
        link = base_url + self.room_id
        headers = {
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
        }
        res = requests.get(link,headers=headers).json()
        # print(res)
        if res["error"] == 101:
            print(res.data)
            print("请输入房间号或者带房间号的直播间地址")
        else:
            owner_name = res["data"]["owner_name"]
            room_name = res["data"]["room_name"]
            print(f"欢迎来到  {owner_name}  的直播间——房间名称  {room_name}")
        

    def run(self):
        """
        启动脚本
        """
        self.connect()
        self.login()
        t = Thread(target=self.keep_alive,daemon=True) ## 主线程退出后直接退出
        t.start()
        self.recive_msg()


    def connect(self):
        """
        连接弹幕服务器
        第三方接入弹幕服务器列表：
        IP 地址： openbarrage.douyutv.com 端口： 8601
        """
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.connect((self.ip,self.port))

    def send_msg(self,msg):
        msg = msg.encode()
        code = 689 # 客户端发送给弹幕服务器
        msg_length = len(msg) + 8  # 加 8 就行 不行换12
        head = struct.pack('i',msg_length) + struct.pack('i',msg_length) + struct.pack('i',code)
        self.socket.sendall(head+msg)

    def login(self):
        """
        登录
        """
        login = f"type@=loginreq/roomid@={self.room_id}/\x00"
        # login = login.encode('utf-8')
        self.send_msg(login)
        joingroup = f"type@=joingroup/rid@={self.room_id}/gid@=-9999/\x00"
        # joingroup = joingroup.encode('utf-8')
        self.send_msg(joingroup)
    
    def recive_msg(self):
        """
        接收消息
        """
        pattern = re.compile(b'type@=chatmsg/(.*?)\x00')
        while True:
            content = self.socket.recv(1024)
            content = pattern.search(content)
            if content:
                msg_obj = self.parse(content.group(1))
                nick_name = msg_obj["nn"]
                txt = msg_obj["txt"]
                # repin = msg_obj["repin"]
                print(f"{nick_name}\t\tsend\t\t{txt}")
            else:
                pass
    

    def keep_alive(self):
        """
        保持于弹幕服务器的连接 每隔45秒发送心跳信息
        """
        while True:
            t = str(int(time.time()))
            msg = f"type@=keeplive/tick@={t}/\x00"
            self.send_msg(msg)
            time.sleep(45)        

    def parse(self,content):
        """
        解析返回的消息
        存在不能转为utf-8的表情符号
        UnicodeDecodeError: 'utf-8' codec can't decode byte 0xed in position 75: invalid continuation byte
        """
        content_obj = {}
        # print(content)
        content = content.decode(errors='replace').strip()
        tmp_kv_list = content.split('/')
        for kv in tmp_kv_list:
            kv = kv.strip()
            if len(kv) == 0:
                continue
            kv = kv.split("@=")
            content_obj[kv[0]]=kv[1]
        return content_obj
    



if __name__ == "__main__":
    douyu = Douyu(475252)
    douyu.run()