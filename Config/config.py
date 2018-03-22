# -*- coding:utf-8 -*-

from Config import _config

def _get_config(section):
    cfg = {}
    configs = _config.options(section)
    for conf in configs:
        cfg[conf] = _config.get(section,conf)
    return cfg

redis_config = _get_config('redis')
sqlite_config = _get_config('sqlite')
mysql_config = _get_config('mysql')
storage_config = _get_config('storage')
