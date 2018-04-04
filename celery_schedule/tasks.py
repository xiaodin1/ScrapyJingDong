# -*- coding:utf-8 -*-

from __future__ import absolute_import
from .application import app
import requests
import sys
sys.path.append('..')
import redis
from . import *

url_get_status = 'http://{0}/listjobs.json'.format(SPIDERD_HOST)
url_start_spider = 'http://{0}/schedule.json'.format(SPIDERD_HOST)

url_base = 'https://list.jd.com/list.html?cat=9987,653,655&ev=exbrand%5F14026&page={0}&sort=sort%5Frank%5Fasc&trans=1&JL=6_0_0#J_main'
rd = redis.from_url(REDIS_URL)

@app.task
def start_spider():
    get_status_response = requests.get(url_get_status,params={'project':TEMP_PROJECT_NAME})
    jsonstr = get_status_response.json()
    start_spider_jsonstr = None
    if jsonstr['running'] == []:
        start_spider_response = requests.post(url_start_spider,data={'project':TEMP_PROJECT_NAME,'spider':TEMP_SPIDER_NAME})
        start_spider_jsonstr = start_spider_response.json()
        rd.lpush(JOBID_KEY,start_spider_jsonstr['jobid'])
    else:
        pass
    return start_spider_jsonstr

@app.task
def feed_spider():
    result = None
    try:
        result = rd.lpush(START_URLS_KEY,url_base.format(1))
    except Exception as ex:
        raise ex
    finally:
        return result

