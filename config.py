#_*_coding:utf-8_*_

import os

basedir = os.path.dirname(os.path.realpath(__file__))

class Config:
    @staticmethod
    def init_app(app):
        pass

class devconfig(Config):
    pass
