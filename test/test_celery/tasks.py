# -*- coding:utf-8 -*-

from __future__ import absolute_import
from test_celery.celery import app

@app.task
def add(x,y):
    return x+y
