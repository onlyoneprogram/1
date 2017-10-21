import scrapy
from ..items import GanjiItem


class zufangSpider(scrapy.Spider):
    name = 'zufang'
    start_urls = ['http://cd.ganji.com/fang1/m1p2/']

    def parse(self, response):
        items = GanjiItem()
        title_list = response.xpath(".//div[@class='f-list-item ']/dl/dd[1]/a/@title").extract()
        price_list = response.xpath(".//div[@class='f-list-item ']/dl/dd[5]/div[1]/span[1]/text()").extract()
        for i,j in zip(title_list, price_list):
            items['title'] = i
            items['price'] = j
            yield items

