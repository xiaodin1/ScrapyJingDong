#_*_coding:utf-8_*_

import requests
import json
import redis
import logging
from .settings import REDIS_URL

logger = logging.getLogger(__name__)
reds = redis.Redis.from_url(REDIS_URL,db=2,decode_responses=True)
login_url = 'https://passport.jd.com/uc/login?ltype=logout'

def get_cookie(account,password):
    '''获取Cookie'''



    s = requests.Session()
    payload = {
        'log':account,
        'pwd':password,
        'rememberme':'forever',
        'wp-submit':'submit',
        'redicrct_to':'',
        'testcookie':1
    }
    response = s.post(login_url,data=payload)
    cookies = response.cookies.get_dict()
    logger.info(u'获取Cookie成功！(账号为：%s)'%account)
    return json.dumps(cookies)

def init_cookie(red,spidername):
    '''将Cookie写入Redis'''
    redkeys = reds.keys()
    for user in redkeys:
        password = reds.get(user)
        if red.get('%s:Cookies:%s--%s'%(spidername,user,password)):
            cookie = get_cookie(user,password)
            red.set('%s:Cookies:%s--%s'%(spidername,user,password),cookie)

