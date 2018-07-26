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