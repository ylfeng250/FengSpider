"""
requests的基础用法
"""
import requests

url_ip = 'http://httpbin.org/ip'
url_github = "https://github.com/timeline.json"
url_headers = 'http://httpbin.org/headers'
url_post = 'http://httpbin.org/post'
url_cookie = 'http://httpbin.org/cookies'
# 发送普通的get请求 
def test1():
    res = requests.get(url_ip)
    print('>>>>>print headers')
    print(res.headers)
    print('>>>>>print response body')
    print(res.text) #以字符串形式查看
    print(res.content) # 以字节的形式查看
    print('状态相应码：',res.status_code)
    print('状态码查询对象:',res.status_code == requests.codes.ok)

# 传递URL参数 
def test2():
    params = {
        'param1':'hello',
        'param2':'world'
    }
    res = requests.get(url_ip,params=params)
    print('>>>>print request url')
    print(res.url)
    print('>>>>>print encoding')
    print(res.encoding)

# json的解析
def test3():
    res = requests.get(url_github)
    data = res.json()
    print(">>>>>>print json")
    print(data)
    print(data['message']) # 打印返回的json中的key为message的value
# 制定请求头
def test4():
    headers = {
        'user-agent':'no-96'
    }
    res = requests.get(url=url_headers,headers=headers)
    print(res.text)
    print(">>>>获取响应头部的信息")
    print(res.headers['content-type'])

# 发送post请求
def test5():
    postdata = {
        'key1':'value1',
        'key2':'value2'
    }
    res = requests.post(url=url_post,data=postdata)
    print(res.text)
# post上传文件
def test6():
    files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
    res = requests.post(url_post,files=files)
    print(res.text)

# cookie
def test7():
    # res = requests.get(url_cookie)
    # print(res.text)
    # 如果response中含有cookie，可以通过res.cookies[example_cookie_name]获取
    # 发送cookie到服务器
    cookies = dict(cookies_are='working')
    res = requests.get(url_cookie,cookies=cookies)
    print(res.text)
def test8():
    #Cookie 的返回对象为 RequestsCookieJar它的行为和字典类似，但界面更为完整，适合跨域名跨路径使用
    jar = requests.cookies.RequestsCookieJar()
    jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
    res = requests.get(url_cookie, cookies=jar)
    print(res.text)
# 重定向
def test9():
    # 可以使用响应对象的 history 方法来追踪重定向。
    # Response.history 是一个 Response 对象的列表，为了完成请求而创建了这些对象。这个对象列表按照从最老到最近的请求进行排序。
    # 例如，Github 将所有的 HTTP 请求重定向到 HTTPS
    r = requests.get('http://github.com')
    print(r.url)
    print(r.history)
    # 可以通过allow_redirects来禁止重定向
    r = requests.get('http://github.com', allow_redirects=False)
    print(r.status_code)
# 超时设置
def test10():
    # 超出时间没有响应的页面将不会被响应
    # timeout 仅对连接过程有效，与响应体的下载无关。 
    # timeout 并不是整个下载响应的时间限制，而是如果服务器在 timeout 秒内没有应答，
    # 将会引发一个异常（更精确地说，是在 timeout 秒内没有从基础套接字上接收到任何字节的数据时）
    # If no timeout is specified explicitly, requests do not time out.
    try:
        res = requests.get('http://github.com', timeout=0.001)
    except:
        print('超时')
if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    # test7()
    # test8()
    test10()