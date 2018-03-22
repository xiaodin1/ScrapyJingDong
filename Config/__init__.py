# -*- coding:utf-8 -*-

import os
import configparser

try:
    _app_path = os.path.dirname(os.path.abspath(__file__))
    _base_dir = os.path.dirname(_app_path)
    _config = configparser.ConfigParser()
    _cfg_file = os.path.join(_base_dir, 'global.cfg')
    _config.read(_cfg_file)
except Exception as ex:
    raise ex

