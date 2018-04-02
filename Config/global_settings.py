# -*- coding:utf-8 -*-

REDIS_URL = 'redis://root:@192.168.2.125:6380'
RABBITMQ_URL = 'amqp://guest:guest@192.168.2.125:5676/'

SPIDER_START_URLS_KEY = 'producturl:start_urls'
SPIDER_JOBID_KEY = 'id:jobid'
SPIDER_DB_CONF = {
   'default':'mysql',
   'sqlite':{
      'database':'jd.db',
   },
   'mysql':{
      'host':'192.168.2.125',
      'port':3308,
      'user':'root',
      'passwd':'123456',
      'db':'jddb',
      'charset':'utf8',
   },
    'mongodb':{
        'host':'192.168.2.125',
        'port':27017,
    },
}

SPIDERD_HOST = '192.168.2.125:6801'


TEMP_PROJECT_NAME = 'ScrapyJD'
TEMP_SPIDER_NAME = 'producturl'
