import requests
"""
发送一个请求，当请求返回响应的时候去执行回调函数
"""

def get_key_info(reqponse,*args,**kwargs):
    """
    回调函数
    """
    print(reqponse.headers['Content-Type'])
    # print('>>>>打印args')
    # print(args)
    # print('>>>>打印kwargs')
    # print(kwargs)

def main():
    """
    主函数
    """
    requests.get('http://www.baidu.com',hooks=dict(response=get_key_info))

if __name__ == "__main__":
    main()