# -*- coding: utf-8 -*-
import scrapy
from scrapy import log
from scrapy_redis.spiders import RedisSpider
import json
import demjson
import requests
import re
from ..items import ScrapyjdItem

class ProducturlSpider(scrapy.Spider):
    name = 'producturl'
    allowed_domains = ['jd.com']
    redis_key = 'producturl:start_urls'
    url_base = 'https://list.jd.com/list.html?cat=9987,653,655&ev=exbrand%5F14026&page={0}&sort=sort%5Frank%5Fasc&trans=1&JL=6_0_0#J_main'

    url_item_base = 'https://item.jd.com/{0}.html'

    url_price_base = 'https://p.3.cn/prices/mgets?pdtk=&skuIds=J_{0}'

    start_urls = [url_base.format(1)]

    def parse(self,response):
        pagesize = int(response.xpath('//div[@class="page clearfix"]/div[@class="p-wrap"]/span[@class="p-skip"]/em/b/text()')[0].extract())
        for i in range(1,pagesize+1):
            yield scrapy.Request(self.url_base.format(i),callback=self.parse_itemurl)

    def parse_itemurl(self, response):
        print('page >>> ',response.url)
        slaveWareList = re.findall('slaveWareList =(.*?);', response.text)[0]
        skuids = self.get_skuids(slaveWareList)
        log.msg('skuids : %s'%len(skuids),level=log.INFO)
        for skuid in skuids:
            if type(skuid) is list:
                skuid = skuid[0]
            itemurl = self.url_item_base.format(skuid)
            log.msg('itemurl : %s' % itemurl)
            yield scrapy.Request(itemurl,callback=self.parse_item)

    def parse_item(self,response):
        items = ScrapyjdItem()
        itemurl = response.url
        print('item >>> ',itemurl)
        skuId = re.findall('/(\d.*).html', response.url)[0]
        iteminfo = response.xpath('//div[@class="itemInfo-wrap"]')[0]
        items['skuname'] = iteminfo.xpath('./div[@class="sku-name"]')[0].xpath('string(.)')[0].extract().replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '')
        items['price'] = float(self.get_price(skuId))
        items['itemurl'] = itemurl
        return items

    def get_skuids(self,jsontext):
        djson = demjson.decode(jsontext)
        skuid1 = list(djson.keys())
        skuid2 = []
        for i in list(djson.values()):
            for n in i:
                skuid2.append(list(n.keys()))
        skuid = skuid1+skuid2
        return skuid

    def get_price(self,skuId):
       pricejsonstr = requests.get(self.url_price_base.format(skuId)).text 
       jsonstr = json.loads(pricejsonstr)
       return jsonstr[0]['p']

