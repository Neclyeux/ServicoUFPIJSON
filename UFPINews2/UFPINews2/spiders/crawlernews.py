# -*- coding: utf-8 -*-
import scrapy
import json
from unidecode import unidecode


class CrawlernewsSpider(scrapy.Spider):
    name = 'crawlernews'
    allowed_domains = ['https://www.ufpi.br']
    start_urls = []
    file = open('/home/neclyeux/Documentos/UFPINews/output.json', 'rb')
    data = json.load(file)

    for index in range(len(data)):
        start_urls.append(data[index]['link'])

    file.close()

    def parse(self, response):
        for news in response.css('div.item-page'):
            yield{
                'title': unidecode((news.xpath('.//h1/a/text()').extract_first()).strip()),
                'news': news.xpath('.//p/text()').extract(),
            }
