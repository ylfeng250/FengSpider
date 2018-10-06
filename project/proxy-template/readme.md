## 代理池

* 抓取西刺代理
* 封装requests的请求

## 使用方法

```python
download = FengProxy()
download.get("http://www.baidu.com")

print(download.content)
```