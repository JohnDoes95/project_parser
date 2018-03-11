# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from questions.models import Questions, Yandex_metricks
from scrapy_project.check_seo import Check
from questions.views import result ,resultkey,resultdesc,resultgoogl

class ScrapyProjectPipeline(object):
    def process_item(self, item, spider):

        if item['title']:
            result[item['link']] = item['title']
            resultkey[item['link']] = item['keyword']
        if item['description']:
            resultdesc[item['link']] = item['description']
       # resultlink.append(item["link"])
       # self.resulth1[item['link']] = item['h1']
       # self.resulttext[item['link']] = item['text']
        resultgoogl[item['link']] = item['googl_anal']
       # resultyandex.append(item['link'])
        itt = Yandex_metricks(yandex=item['link'])
            # question = Questions.objects.get(identifier=item["identifier"])
          #  print ("Question already exist")
           # return item

         #   pass
        #         item =item['url']
        itt.save()
        self.save_data()
        return item

    def save_data(self):
        """if item['title']:
            self.result[item['link']] = item['title']
        self.resultkey[item['link']] = item['keyword']
        if item['description']:
            self.resultdesc[item['link']] = item['description']
        self.resultlink.append(item["link"])
        self.resulth1[item['link']] = item['h1']
        self.resulttext[item['link']] = item['text']
        self.resultgoogl[item['link']] = item['googl_anal']
        self.resultyandex.append(item['link'])"""
