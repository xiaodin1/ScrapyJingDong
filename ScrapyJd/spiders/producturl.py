# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider,log
from scrapy_redis.spiders import RedisSpider
import json
import demjson
import requests
import re
from ..items import ScrapyjdItem

class ProducturlSpider(RedisSpider):
    name = 'producturl'
    allowed_domains = ['jd.com']
    redis_key = 'producturl:start_urls'

    url_base = 'https://list.jd.com/list.html?cat=9987,653,655&ev=exbrand%5F14026&page={0}&sort=sort%5Frank%5Fasc&trans=1&JL=6_0_0#J_main'
    url_item_base = 'https://item.jd.com/{0}.html'
    url_price_base = 'https://p.3.cn/prices/mgets?pdtk=&skuIds=J_{0}'
    url_comments_base = 'https://sclub.jd.com/comment/productPageComments.action?productId={0}&score=0&sortType=5&page=0&pageSize=10'

    # start_urls = [url_base.format(1)]

    def parse(self,response):
        pagesize = int(response.xpath('//div[@class="page clearfix"]/div[@class="p-wrap"]/span[@class="p-skip"]/em/b/text()')[0].extract())
        for i in range(1,pagesize+1):
            yield scrapy.Request(self.url_base.format(i),callback=self.parse_itemurl)

    def parse_itemurl(self, response):
        print('page >>> ',response.url)
        skuids = self.get_skuids(response.text)
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
        items['commentCount'] = self.get_commentcount(skuId)
        items['itemurl'] = itemurl
        return items

    def get_skuids(self,text):
        '''获取skuid，唯一商品页面标识'''
        jsontext = re.findall('slaveWareList =(.*?);', text)[0]
        djson = demjson.decode(jsontext)
        skuid1 = list(djson.keys())
        skuid2 = []
        for i in list(djson.values()):
            for n in i:
                skuid2.append(list(n.keys()))
        skuid = skuid1+skuid2
        return skuid

    def get_price(self,skuId):
        '''获取价格'''
        pricejsonstr = requests.get(self.url_price_base.format(skuId)).text
        jsonstr = json.loads(pricejsonstr)
        return jsonstr[0]['p']

    def get_commentcount(self,skuId):
        '''获取评论数'''
        commentsjsonstr = requests.get(self.url_comments_base.format(skuId)).text
        dic = dict(demjson.decode(commentsjsonstr))
        count = 0
        for comtype in dic['hotCommentTagStatistics']:
            count += comtype['count']
        return count



