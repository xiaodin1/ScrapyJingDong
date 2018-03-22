# -*- coding:utf-8 -*-

from __future__ import absolute_import
from celery import Celery
# from celery.signals import after_task_publish

app = Celery('celery_schedule',include=['celery_schedule.tasks'])
app.config_from_object('celery_schedule.celery-config')

if __name__ == '__main__':
    app.start()
