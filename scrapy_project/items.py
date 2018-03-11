# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuestionItem(scrapy.Item):
    title = scrapy.Field()
    keyword = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
    h1 = scrapy.Field()
    h2 = scrapy.Field()
    text = scrapy.Field()
    googl_anal = scrapy.Field()
    yandex_metrick = scrapy.Field()


class SeoItem(scrapy.Item):
    title = scrapy.Field()
    keyword = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
    h1 = scrapy.Field()
    h2 = scrapy.Field()
    text = scrapy.Field()
    googl_anal = scrapy.Field()
    yandex_metrick = scrapy.Field()
    count_analytics = scrapy.Field()

class SecondItem(scrapy.Item):
    title = scrapy.Field()
    keywords = scrapy.Field()
    description = scrapy.Field()
    h1 = scrapy.Field()
    h2 = scrapy.Field()
    text = scrapy.Field()
    googl_anal = scrapy.Field()
    yandex_metrika = scrapy.Field()
