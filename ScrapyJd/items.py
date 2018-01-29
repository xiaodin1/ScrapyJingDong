# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyjdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    skuname = scrapy.Field()
    price = scrapy.Field()
    itemurl = scrapy.Field()
