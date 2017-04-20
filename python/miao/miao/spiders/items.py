# !/usr/bin/env python3
# -*- coding:utf-8 -*-

from scrapy import Item, Field


class TopicItem(Item):
    url = Field()
    title = Field()
    author = Field()

class ContentItem(Item):
    url = Field()
    content = Field()
    author = Field()