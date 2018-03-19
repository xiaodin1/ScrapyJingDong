# -*- coding: utf-8 -*-
import scrapy
from scrapy import log
from scrapy_redis.spiders import RedisSpider
import json
import demjson
import requests
import re
from ..items import ScrapyjdItem
from datetime import datetime
from ..helpers import log_param

class ProducturlSpider(RedisSpider):
    name = 'producturl'
    allowed_domains = ['jd.com']

    redis_key = 'producturl:start_urls'

    url_base = 'https://list.jd.com/list.html?cat=9987,653,655&ev=exbrand%5F14026&page={0}&sort=sort%5Frank%5Fasc&trans=1&JL=6_0_0#J_main'
    url_item_base = 'https://item.jd.com/{0}.html'
    url_price_base = 'https://p.3.cn/prices/mgets?pdtk=&skuIds=J_{0}'
    url_comments_base = 'https://sclub.jd.com/comment/productPageComments.action?productId={0}&score=0&sortType=5&page=0&pageSize=10'

    def start_requests(self):
        url = self.url_base.format(1)
        yield scrapy.Request(url=url,callback=self.parse,dont_filter=True)

    def parse(self, response):
        text = None
        try:
            text = response.xpath('//div[@class="page clearfix"]/div[@class="p-wrap"]/span[@class="p-skip"]/em/b/text()')[0].extract()
            pagesize = int(text)
        except Exception as ex:
            pagesize = 1
            log.msg(str(ex)+log_param(text=text),level=log.ERROR)
        for i in range(1,pagesize+1):
            yield scrapy.Request(self.url_base.format(i),callback=self.parse_itemurl,dont_filter=True)

    def parse_itemurl(self, response):
        skuids = self.get_skuids(response.text)
        if skuids is not None:
            for skuid in skuids:
                if type(skuid) is list:
                    skuid = skuid[0]
                itemurl = self.url_item_base.format(skuid)
                yield scrapy.Request(itemurl,callback=self.parse_item)

    def parse_item(self,response):
        items = ScrapyjdItem()
        itemurl = response.url
        try:
            skuIds = re.findall('/(\d.*).html', itemurl)
            skuId = skuIds[0]
        except Exception as ex:
            skuId = None
            log.msg(str(ex)+log_param(itemurl=itemurl), level=log.ERROR)

        iteminfo = response.xpath('//div[@class="itemInfo-wrap"]')[0]
        items['product_name'] = iteminfo.xpath('./div[@class="sku-name"]')[0].xpath('string(.)')[0].extract().replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '')
        items['product_price'] = float(self.get_price(skuId))
        items['product_url'] = itemurl
        items['product_id'] = skuId
        try:
            storeinfo = response.xpath('//div[@class="popbox-inner"]/div[@class="mt"]/h3/a')[0]
            items['store_name'] = storeinfo.xpath('./text()')[0].extract()
            items['store_url'] = 'http:%s'%storeinfo.xpath('./@href')[0].extract()
        except:
            items['store_name'] = '京东自营'
            items['store_url'] = None
        items['crawl_time'] = datetime.now().strftime('%Y:%m:%d %H:%M:%S')
        return items

    def get_skuids(self,text):
        '''获取skuid，唯一商品页面标识'''
        jsontexts = None
        jsontext = None
        try:
            jsontexts = re.findall('slaveWareList =(.*?);', text)
            jsontext = jsontexts[0]
            djson = demjson.decode(jsontext)
            skuid1 = list(djson.keys())
            skuid2 = []
            for i in list(djson.values()):
                for n in i:
                    skuid2.append(list(n.keys()))
            skuid = skuid1 + skuid2
        except Exception as ex:
            log.msg(str(ex)+log_param(text=text,jsontexts=jsontexts,jsontext=jsontext),level=log.ERROR)
            return None
        return skuid

    def get_price(self,skuId):
        '''获取价格'''
        if skuId is None:
            return -1
        pricejsonstr = None
        try:
            pricejsonstr = requests.get(self.url_price_base.format(skuId)).text
            jsonstr = json.loads(pricejsonstr)
            price = jsonstr[0]['p']
        except Exception as ex:
            log.msg(str(ex)+log_param(skuId=skuId,pricejsonstr=pricejsonstr),level=log.ERROR)
            return -1
        return price

    def get_commentcount(self,skuId):
        '''获取评论数'''
        if skuId is None:
            return -1
        commentsjsonstr=None
        try:
            commentsjsonstr = requests.get(self.url_comments_base.format(skuId)).text
            dic = dict(demjson.decode(commentsjsonstr))
            count = 0
            for comtype in dic['hotCommentTagStatistics']:
                count += comtype['count']
        except Exception as ex:
            log.msg(str(ex)+log_param(skuId=skuId,commentsjsonstr=commentsjsonstr),level=log.ERROR)
            return -1
        return count

