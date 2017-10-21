import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from heartsong.items import HeartsongItem


class HeartsongSpider(scrapy.Spider):
    name = "heartsong"
    allowed_domains = ["heartsong.top"]  # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = ["http://www.heartsong.top/forum.php?mod=viewthread&tid=8"]

    def parse(self, response):
        selector = Selector(response)  # 创建选择器
        # 后注：在新版的Scrapy1.2.x版本中，不再需要这句话，直接使用response.xpath("xx")即可

        table = selector.xpath('//*[starts-with(@id, "pid")]')  # 取出所有的楼层
        for each in table:  # 对于每一个楼层执行下列操作
            item = HeartsongItem()  # 实例化一个Item对象
            item['title'] = selector.xpath('//*[@id="thread_subject"]/text()').extract()[0]
            item['author'] = \
                each.xpath(
                    'tr[1]/td[@class="pls"]/div[@class="pls favatar"]/div[@class="pi"]/div[@class="authi"]/a/text()').extract()[0]
            item['post_time'] = \
                each.xpath('tr[1]/td[@class="plc"]/div[@class="pi"]').re(r'[0-9]+-[0-9]+-[0-9]+ [0-9]+:[0-9]+:[0-9]+')[
                    0]
            content_list = each.xpath('.//td[@class="t_f"]').xpath('string(.)').extract()
            content = "".join(content_list)  # 将list转化为string
            item['url'] = response.url  # 用这种方式获取网页的url
            # 把内容中的换行符，空格等去掉
            item['content'] = content.replace('\r\n', '').replace(' ', '').replace('\n', '')
            yield item  # 将创建并赋值好的Item对象传递到PipeLine当中进行处理