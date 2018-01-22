# requests库的学习和使用

## 环境搭建

[requests官方网址](https://github.com/requests/requests)

[requests中文文档](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)

1.安装`virtualenv`非必要

```
pip install virtualenv 
```

2.创建一个工程目录如`myproject`,在该目录下创建虚拟环境
```
virtualenv .env
```
此时工程目录下会有一个`.env`的隐藏文件，设置为隐藏文件是因为平时不需要去理会里面的东西


3.进入隐藏文件夹，在命令行执行`\Scripts\activate`
```
D:\code\python\requests\.env\Scripts>activate
```
我的操作系统和是win10，如果是Linux可以自行Google。进入虚拟环境就会显示
```
(.env) D:\code\python\requests\.env\Scripts>
```
之后的操作可以在虚拟环境中操作，也可以在本机中操作

2.安装requests
```
pip install requests
```