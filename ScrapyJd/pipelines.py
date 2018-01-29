# -*- coding: utf-8 -*-

from pymongo import MongoClient
from .settings import Mongodb_Host,Mongodb_Port
from .items import ScrapyjdItem
from datetime import datetime

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyjdPipeline(object):
    def __init__(self):
        client = MongoClient(host=Mongodb_Host,port=Mongodb_Port)
        db = client["jd"]
        nowtime = datetime.now().strftime('%Y%m%d')
        self.jdinfo = db[nowtime]

    def process_item(self, item, spider):
        if isinstance(item,ScrapyjdItem):
            try:
                self.jdinfo.insert(dict(item))
            except Exception as e:
                print (e)
        return item
