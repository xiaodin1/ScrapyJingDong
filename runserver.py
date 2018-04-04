# -*- coding:utf-8 -*-

import subprocess
from celery_schedule.tasks import start_spider
import time

cmds = [
    'scrapyd',
    'celery -B -A celery_schedule.application worker -l info',
]

for cmd in cmds:
    subprocess.Popen(cmd,shell=True)

time.sleep(10)
start_spider()
