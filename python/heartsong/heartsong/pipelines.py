# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import heartsong.settings


class HeartsongPipeline(object):
    def process_item(self, item, spider):
        file = open("item.txt", "a")
        file.write(str(item))
        file.write('\n')
        file.close()
        print(item)
        return item
