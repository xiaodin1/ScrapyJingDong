# -*- coding:utf-8 -*-

from __future__ import absolute_import
from .application import app
import requests
import sys
sys.path.append('..')
from Config import config
import redis

url_get_status = 'http://192.168.110.130:6800/listjobs.json'
url_start_spider = 'http://192.168.110.130:6800/schedule.json'

url_base = 'https://list.jd.com/list.html?cat=9987,653,655&ev=exbrand%5F14026&page={0}&sort=sort%5Frank%5Fasc&trans=1&JL=6_0_0#J_main'
rd = redis.from_url(config.REDIS_URL)


@app.task
def add(x,y):
    return x+y

@app.task
def start_spider():
    get_status_response = requests.get(url_get_status,params={'project':'JingDongSpider'})
    jsonstr = get_status_response.json()
    start_spider_jsonstr = None
    if jsonstr['running'] == []:
        start_spider_response = requests.post(url_start_spider,data={'project':'JingDongSpider','spider':'producturl'})
        start_spider_jsonstr = start_spider_response.json()
        rd.lpush(config.JOBID_KEY,start_spider_jsonstr['jobid'])
        # with open('id.txt','a+') as fp:
        #     fp.write(start_spider_jsonstr['jobid']+'\n')
    else:
        pass
    return start_spider_jsonstr

@app.task
def feed_spider():
    result = None
    try:
        result = rd.lpush(config.START_URLS_KEY,url_base.format(1))
    except Exception as ex:
        raise ex
    finally:
        return result

