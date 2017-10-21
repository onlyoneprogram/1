import scrapy
from image.items import ImageItem


class spider_huaban(scrapy.Spider):
    name = 'huaban'
    start_urls = ['http://www.xiaohuar.com/2014.html']

    def parse(self, response):
        item = ImageItem()
        url_1 = 'http://www.xiaohuar.com'
        url = response.xpath(".//div[@class='item masonry_brick masonry-brick']/div[1]/div[2]/a/img/@src").extract()
        #url = response.xpath(".//*[@id='list_img']/div[1]/div/div[46]/div[1]/div[2]/a/img/@src").extract()
        print(url)
        #url_2 = ''.join(url)
        #item['image_urls'] = (url_1+url_2).split()
        #print(item['image_urls'])
        #return item

