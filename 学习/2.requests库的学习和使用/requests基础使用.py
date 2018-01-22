"""
requests的基础用法
"""
import requests

url_ip = 'http://httpbin.org/ip'
url_github = "https://github.com/timeline.json"
url_headers = 'http://httpbin.org/headers'
url_post = 'http://httpbin.org/post'
url_cookie = 'http://httpbin.org/cookies'
url_wiki = 'http://en.wikipedia.org/wiki/Monty_Python'
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

"""
回话对象
会话对象让你能够跨请求保持某些参数。它也会在同一个 Session 实例发出的所有请求之间保持 cookie
所以如果你向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升
"""

# 跨请求来保持一些cookie
def test11():
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    r = s.get('http://httpbin.org/cookies')
    print(r.text)

def test12():
    s = requests.Session()
    s.auth = ('user','pass')
    s.headers.update({'x-test':'true'})
    # x-test 和 x-test2都会被发送
    # 上面设置的头部信息会和下面方法中传入的头部信息合并
    r = s.get(url=url_headers,headers={'x-test2':'true'})
    print(r.text)
    r = s.get(url_headers)
    print(r.text)
    # 在headers.update中设置的x-test会被保留，但是在get方法中设置的x-test2不会

# 在方法级别设置的参数不会被夸请求保持
def test13():
    s = requests.Session()
    res = s.get(url_cookie,cookies={'from-my':'oh-my-god'})
    print(res.text)
    res = s.get(url_cookie)
    print(res.text)
    # 第二次访问的时候第一次设置的cookie不会被保存

"""
请求request与响应response对象
这一部分需要之后仔细看看
"""
def test14():
    res = requests.get(url_wiki)
    print('>>>>获取响应头部')
    print(res.headers)
    print('>>>>获取发送的请求头部')
    print(res.request.headers)
if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    # test7()
    # test8()
    # test10()
    # test11()
    # test12()
    # test13()
    test14()