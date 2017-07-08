# -*- coding: utf-8 -*-
import scrapy
from unidecode import unidecode


class CrawlerufpiSpider(scrapy.Spider):
    name = 'crawlerufpi'
    allowed_domains = ['https://www.ufpi.br']
    start_urls = ['https://www.ufpi.br/ultimas-noticias-ufpi',
                  'http://ufpi.br/ultimas-noticias-ufpi?start=10',
                  'http://ufpi.br/ultimas-noticias-ufpi?start=20',
                  'http://ufpi.br/ultimas-noticias-ufpi?start=30',
                  'http://ufpi.br/ultimas-noticias-ufpi?start=40']

    def parse(self, response):
        for news in response.css('div.span10'):
            link_news = news.xpath('.//h2/a/@href').extract_first()
            yield{
                'title': unidecode(news.xpath('.//h2/a/text()').extract_first()),
                'link': response.urljoin(link_news),
            }
