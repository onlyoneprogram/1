# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class MiaoPipeline(object):
    def process_item(self, item, spider):
        return item

from scrapy import Item, Field

class TopicItem(Item):
    url = Field()
    title = Field()
    author = Field()

class ContentItem(Item):
    url = Field()
    content = Field()
    author = Field()

import os
f_path = '/home/wangxy/Desktop/python/miao/miao'
if not os.path.exists(f_path):
    os.makedirs(f_path)
f = open(r'/home/wangxy/Desktop/python/miao/miao/info.txt', 'a')


class FilePipeline(object):

    #爬虫的分析结果都会由scrapy交给此函数处理
    def process_item(self, item, spider):
        if isinstance(item, TopicItem):
            ##在此可进行文件写入/数据库写入等操作
            print("##########################################################################")
            print(item)
            #f.writelines(u'抬头', item)
        if __name__ == '__main__':
            if isinstance(item, ContentItem):
                ##在此可进行文件写入/数据库写入等操作
                pass
            ## ..
        f.close()
        return item

