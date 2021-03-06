# -*- coding:utf-8 -*-

from __future__ import absolute_import
from .application import app
import requests

url_get_status = 'http://192.168.110.130:6800/listjobs.json'
url_start_spider = 'http://192.168.110.130:6800/schedule.json'

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
        with open('id.txt','a+') as fp:
            fp.write(start_spider_jsonstr['jobid']+'\n')
    else:
        pass
    return start_spider_jsonstr

@app.task
def feed_spider():
    pass