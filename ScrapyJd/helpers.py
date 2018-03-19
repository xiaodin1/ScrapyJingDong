# -*- coding:utf-8 -*-

def log_param(**kwargs):
    '''日志参数记录'''
    param = ''
    for i in kwargs.keys():
        param += '\n%s:%s'%(i,kwargs[i])
    return param
