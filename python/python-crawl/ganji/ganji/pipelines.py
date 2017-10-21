# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class GanjiPipeline(object):
    def open_spider(self, spider):
        self.con = sqlite3.connect("zufang.sqlite")
        self.cursor = self.con.cursor()

    def process_item(self, item, spider):
        insert_sql = 'insert into zufang(title, price) VALUES ("{}", "{}")'.format(item['title'], item['price'])
        self.cursor.execute(insert_sql)
        self.con.commit()
        return item

    def spider_close(self, spider):
        self.con.close()
