# 大致代码如下：
from billiard.process import Process
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from django.db import connection

class BilliardCrawlProcess(Process):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, daemon=None, **_kw):
        super(BilliardCrawlProcess, self).__init__(group, target, name, args, kwargs, daemon, **_kw)

    def run(self):
        settings = get_project_settings()
        process = CrawlerProcess(settings)

        process.crawl('stackoverflow',
                      )
        process.start()


def crawl():
    crawl_process = BilliardCrawlProcess()
    crawl_process.start()
    crawl_process.join()  # blocks here until scrapy finished
    connection.close()  # NOTE