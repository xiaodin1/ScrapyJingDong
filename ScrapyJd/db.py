#-*- coding: utf-8 -*-

import pymysql
from datetime import datetime
from scrapy import log

class Sql(object):
    def __init__(self,**kwargs):
        self._conn = pymysql.connect(**kwargs)
        self._table_name = 'tb_product_{0}'.format(datetime.now().strftime('%Y%m%d'))
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
        except:
            raise

    def insert(self, *args,**kwargs):
        try:
            with self._conn.cursor() as cursor:
                sql = "INSERT INTO {0}(product_id,product_name,product_price,product_url,store_name,store_url,crawl_time)  \
                      VALUES ('{product_id}','{product_name}',{product_price},'{product_url}','{store_name}','{store_url}','{crawl_time}')".format(self._table_name,**kwargs)
                # log.msg(sql,level=log.INFO)
                cursor.execute(sql)
            self._conn.commit()
            return True
        except:
            raise
