# -*- coding:utf-8 -*-

SERVER_IP = '192.168.1.108'

REDIS_URL = 'redis://root:@{0}:6380'.format(SERVER_IP)
RABBITMQ_URL = 'amqp://guest:guest@{0}:5676/'.format(SERVER_IP)

SPIDER_START_URLS_KEY = 'producturl:start_urls'
SPIDER_JOBID_KEY = 'id:jobid'
SPIDER_DB_CONF = {
   'default':'mysql',
   'sqlite':{
      'database':'jd.db',
   },
   'mysql':{
      'host':SERVER_IP,
      'port':3308,
      'user':'root',
      'passwd':'123456',
      'db':'jddb',
      'charset':'utf8',
   },
    'mongodb':{
        'host':SERVER_IP,
        'port':27017,
    },
}

SPIDERD_HOST = '{0}:6802'.format(SERVER_IP)


TEMP_PROJECT_NAME = 'ScrapyJD'
TEMP_SPIDER_NAME = 'producturl'
