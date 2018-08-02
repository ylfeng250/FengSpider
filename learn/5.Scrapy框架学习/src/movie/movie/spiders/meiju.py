# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem
from bs4 import BeautifulSoup

class MeijuSpider(scrapy.Spider):
    name = 'meiju' # 定义爬虫的名字
    allowed_domains = ['meijutt.com']
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        soup = BeautifulSoup(response.body,"lxml")
        movies = soup.find_all('ul',class_="top-list")[0].find_all("li")
        for movie in movies:
            name = movie.find('a').get_text()
            item = MovieItem()
            item['name'] = name
            yield item
            
            
