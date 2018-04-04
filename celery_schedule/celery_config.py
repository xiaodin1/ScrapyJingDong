# -*- coding:utf-8 -*-

from datetime import timedelta
from . import RABBITMQ_URL,REDIS_URL
from celery.schedules import crontab

BROKER_URL = RABBITMQ_URL  #使用RabbitMQ作为消息代理
CELERY_RESULT_BACKEND = '%s/1'%REDIS_URL  #把任务结果存在Redis  'redis://192.168.2.125:6380/1'
CELERY_TASK_SERIALIZER = 'msgpack' #任务序列化和反序列化使用msgpack方案
CELERY_RESULT_SERIALIZER = 'json'   #读取任务结果一般性能要求不高，所以使用了可读性更好的JSON
CELERY_TASK_RESULT_EXPIRES = 60*60*24     #任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显
CELERY_ACCEPT_CONTENT = ['json','msgpack']  #指定接受的内容类型

# crontab()     每分钟执行一次
# crontab(minute=0, hour=0)     每天凌晨十二点执行
# crontab(minute='*/15')        每十五分钟执行一次
# crontab(minute='*',hour='*', day_of_week='sun')   每周日的每一分钟执行一次
# crontab(minute='*/10',hour='3,17,22', day_of_week='thu,fri')  每周三，五的三点，七点和二十二点没十分钟执行一次

CELERYBEAT_SCHEDULE = {
    'feed_spider':{
        'task': 'celery_schedule.tasks.feed_spider',
        # 'schedule': timedelta(seconds=10),
        'schedule':crontab(minute=0, hour=0),
    }
}

