import scrapy

from tutorial.items import TutorialItem


class TutorialSpider(scrapy.Spider):
    name = "tutorial"
    start_urls = [
        "http://bbs.ngacn.cc/thread.php?fid=406"
    ]

    def parse(self, response):
        item = TutorialItem()
        item['title'] = response.xpath('//title/text()').extract()
        yield item



