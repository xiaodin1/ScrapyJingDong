# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyjdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_url = scrapy.Field()            #商品url
    product_id = scrapy.Field()             #标识ID
    product_name = scrapy.Field()           #品名
    product_price = scrapy.Field()          #价格
    store_name = scrapy.Field()             #店铺名
    store_url = scrapy.Field()              #店铺url
    crawl_time = scrapy.Field()             #抓取时间

class CommentItem(scrapy.Item):
    product_url = scrapy.Field()            #商品url
    product_id = scrapy.Field()             #标识ID
    comment_count = scrapy.Field()          #评论数
    comment_pro_type = scrapy.Field()       #评论商品型号
    comment_time = scrapy.Field()           #评论时间
    crawl_time = scrapy.Field()             #抓取时间

