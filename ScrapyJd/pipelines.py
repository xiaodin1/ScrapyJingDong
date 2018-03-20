# -*- coding: utf-8 -*-

from .items import ScrapyjdItem
from .db import Db_Helper

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class ScrapyjdPipeline(object):
    def __init__(self):
        self._sql = Db_Helper().db

    def process_item(self,item,spider):
        if isinstance(item,ScrapyjdItem):
            self._sql.insert(**item)
        return item
