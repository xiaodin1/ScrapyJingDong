# -*- coding:utf-8 -*-

import sys
sys.path.append('..')
from Config import global_settings as gset

REDIS_URL = gset.REDIS_URL
START_URLS_KEY = gset.SPIDER_START_URLS_KEY
JOBID_KEY = gset.SPIDER_JOBID_KEY

RABBITMQ_URL = gset.RABBITMQ_URL
SPIDERD_HOST = gset.SPIDERD_HOST

TEMP_PROJECT_NAME = gset.TEMP_PROJECT_NAME
TEMP_SPIDER_NAME = gset.TEMP_SPIDER_NAME
