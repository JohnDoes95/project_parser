# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerRunner
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy_project.check_seo import Check
from scrapy_project.items import QuestionItem
import time

Ch = Check()
class StackoverflowSpider(CrawlSpider):
    name = "stackoverflow"
    allowed_domains = ["mospolytech.ru"]
    start_urls = ["http://mospolytech.ru"]
    rules = (
        Rule(LinkExtractor(allow="http://mospolytech.ru/"), callback='parse_asd'),
        Rule(LinkExtractor(allow="http://mospolytech.ru/"), follow=True),
    )



    def parse_asd(self, response):
        item = QuestionItem()
        for quote in response.css('html'):
            counters_anal = quote.css('script').extract()
            if 'https://www.google-analytics.com/analytics.js' in str(counters_anal):
                yee = 'Есть'
            else:
                yee = 'Нет'
            if 'mc.yandex.ru/metrika' in str(counters_anal):
                res = 'Есть'
            else:
                res = 'Нет'
            urls = response.url

            title = quote.css('title::text').extract_first(),
            url = response.url
            Ch.chech_title(title, url)
            item['title'] = Ch.chech_title(title,urls)
            description = quote.css(
                'meta[name*=description]::attr(content), meta[name*=Description]::attr(content)').extract(),
            Ch.check_description(description, url)
            h1 = quote.css('h1::text').extract(),
            h2 = quote.css('h2::text, H2::text').extract(),
            item['description'] = Ch.errors_descriptions
            item['h1'] = Ch.check_h1_and_h2(h1, h2, url)
            item['h2'] = Ch.check_h1_and_h2(h1, h2, url)
            item['keyword'] = quote.css(
                'meta[name*=Keywords]::attr(content), meta[name*=keywords]::attr(content)').extract(),
            item['link'] = response.url
            item['text'] = quote.css('p::text, span::text').extract(),
            item['googl_anal'] = yee,
            item['yandex_metrick'] = res,
            return item







