#-*- coding: utf-8 -*-

import pymysql
import sqlite3
from scrapy import log
from .settings import db_conf
from .helpers import log_param


class Db_Helper(object):
    def __init__(self):
        try:
            db_cfg = db_conf['default']
            if db_cfg == 'sqlite':
                self.db = Sqlite_Helper(**db_conf[db_cfg])
            elif db_cfg == 'mysql':
                self.db = Mysql_Helper(**db_conf[db_cfg])
            else:
                log.msg('setting.db_conf is error',level=log.ERROR)
        except Exception as ex:
            raise ex


class Mysql_Helper(object):
    '''Mysql操作'''
    def __init__(self,**kwargs):
        self._conn = pymysql.connect(**kwargs)
        # self._table_name = 'tb_product_{0}'.format(datetime.now().strftime('%Y%m%d'))
        self._table_name = 'tb_product'
        sql = None
        try:
            with self._conn.cursor() as cursor:
                sql = "CREATE TABLE IF NOT EXISTS {0}( \
                    id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT, \
                    product_id VARCHAR(16), \
                    product_name VARCHAR(128), \
                    product_price FLOAT, \
                    product_url VARCHAR(128), \
                    store_name VARCHAR(64), \
                    store_url VARCHAR(128), \
                    crawl_time VARCHAR(32) \
                    );".format(self._table_name)
                cursor.execute(sql)
            self._conn.commit()
        except Exception as ex:
            log.msg(str(ex) + log_param(sql=sql), level=log.ERROR)

    def insert(self, *args,**kwargs):
        sql = None
        try:
            with self._conn.cursor() as cursor:
                sql = "INSERT INTO {0}(product_id,product_name,product_price,product_url,store_name,store_url,crawl_time)  \
                      VALUES ('{product_id}','{product_name}',{product_price},'{product_url}','{store_name}','{store_url}','{crawl_time}')".format(self._table_name,**kwargs)
                # log.msg(sql,level=log.INFO)
                cursor.execute(sql)
            self._conn.commit()
            return True
        except Exception as ex:
            log.msg(str(ex) + log_param(sql=sql), level=log.ERROR)

class Sqlite_Helper(object):
    '''Sqlite操作'''
    def __init__(self,**kwargs):
        self._conn = sqlite3.connect(**kwargs)
        # self._table_name = 'tb_product_{0}'.format(datetime.now().strftime('%Y%m%d'))
        self._table_name = 'tb_product'
        sql = None
        try:
            cursor = self._conn.cursor()
            sql = "CREATE TABLE IF NOT EXISTS {0}( \
                id INTEGER PRIMARY KEY NOT NULL, \
                product_id VARCHAR(16), \
                product_name VARCHAR(128), \
                product_price FLOAT, \
                product_url VARCHAR(128), \
                store_name VARCHAR(64), \
                store_url VARCHAR(128), \
                crawl_time VARCHAR(32) \
                );".format(self._table_name)
            cursor.execute(sql)
            self._conn.commit()
        except Exception as ex:
            log.msg(str(ex) + log_param(sql=sql), level=log.ERROR)

    def insert(self, *args,**kwargs):
        sql = None
        try:
            cursor = self._conn.cursor()
            sql = "INSERT INTO {0}(product_id,product_name,product_price,product_url,store_name,store_url,crawl_time)  \
                  VALUES ('{product_id}','{product_name}',{product_price},'{product_url}','{store_name}','{store_url}','{crawl_time}')".format(self._table_name,**kwargs)
            # log.msg(sql,level=log.INFO)
            cursor.execute(sql)
            self._conn.commit()
            return True
        except Exception as ex:
            log.msg(str(ex) + log_param(sql=sql), level=log.ERROR)
