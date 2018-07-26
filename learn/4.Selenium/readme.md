## 简介
上一篇文章([爬虫实战 | 掘金文章单页爬虫](https://juejin.im/post/5b5861336fb9a04fba6e8632))中为了找到文章真正的请求地址需要去查看网页请求并对参数进行测试，那么有没有什么方法可以直接获取到js处理之后的网页呢？

另外，通过右键检查网页发现网页中的内容并没有上一篇文章中提到的问题，于是猜想，能不能有一种方法模拟浏览器的行为进行js代码的处理，并获取处理完之后的页面。当然是有的，这就是我们今天的主角Selenium

![](https://user-gold-cdn.xitu.io/2018/7/26/164d582bf7cb31a8?w=1551&h=688&f=png&s=210730)

## 工欲善其事必先利其器
* Selenium

Selenium是一个浏览器自动化测试工具，Selenium Python bindings 使用非常简洁方便的API让你去使用像Firefox, IE, Chrome, Remote等等 这样的Selenium WebDrivers（Selenium web驱动器）.通过下面的方式安装

```
pip install selenium
```
* 下载浏览器驱动

在这个链接中选择一个安装 [http://selenium-python.readthedocs.io/installation.html#drivers](http://selenium-python.readthedocs.io/installation.html#drivers),我下载的是火狐的driver.下载之后添加到系统的path（不好意思实验是在win10下处理的）

* 安装Firefox和插件

插件 Katalon Recorder，一款类似按键精灵的工具，可以记录你对浏览器的操作，还能够导出代码。
![](https://user-gold-cdn.xitu.io/2018/7/26/164d5859f738a840?w=1161&h=449&f=png&s=71144)
使用方法

首先打开火狐的Katalon Recorder插件

1.点击New新建一个，然后点击Record开始录制，之后就可以返回浏览器操作了
![](https://user-gold-cdn.xitu.io/2018/7/26/164d58bff0a663d2?w=700&h=674&f=png&s=124060)
2.录制完毕之后点击stop,之后导出代码，这里是python2的代码，但我们不全用，我们只选择交互的部分。而且本文中不使用这个插件，这个插件可以方便的模拟表单提交和模拟登陆操作，这次还是简单的网页原文获取。

![](https://user-gold-cdn.xitu.io/2018/7/26/164d58cabdf84cdb?w=700&h=674&f=png&s=233267)

## 开始爬取
下面是一个简单的demo,获取掘金文章的标题和正文，之后和上一篇文章一样用html2text翻译成markdown就行了，当然可以不用bs4来解析网页，可以直接用selenium自带的api进行元素查找，详细的api见[http://selenium-python.readthedocs.io/installation.html#drivers](http://selenium-python.readthedocs.io/installation.html)
```
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from bs4 import BeautifulSoup

firefox_options = Options() # 配置项
firefox_options.add_argument("--headless") # 无头参数，不会打开浏览器
driver = webdriver.Firefox(firefox_options=firefox_options)
driver.implicitly_wait(10) # 隐式的等待10秒，为了完全加载页面处理js代码
url = "https://juejin.im/post/5b5861336fb9a04fba6e8632"
driver.get(url)
driver.set_page_load_timeout(20) # 超时设置
time.sleep(2) # 睡眠2秒
html = driver.page_source
soup = BeautifulSoup(html,"lxml") # 用html5lib会有一点问题，无法解析H5特有的网页标签，很费解
title = soup.title.get_text()
article = soup.find("article")
print("title:",title)
print("article:",article)
## 保存html
with open("text.html","w",encoding="utf-8") as f:
    f.write(html)
```

selenium的功能远不止这些，按需使用，我只是简单的用了一下，是不是比自己找请求方便多了~~~

-------
欢迎关注我的孙女叫小芳的微信公众号

![](https://user-gold-cdn.xitu.io/2018/7/26/164d5922c99f9640?w=344&h=344&f=jpeg&s=8465)