# -*- coding:utf-8 -*-

from __future__ import absolute_import
from celery import Celery
# from celery.signals import after_task_publish

app = Celery('test_celery',include=['test_celery.tasks'])
app.config_from_object('test_celery.celery-config')

if __name__ == '__main__':
    app.start()
