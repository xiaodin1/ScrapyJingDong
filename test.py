# -*- coding: utf-8 -*-

import pymysql
from datetime import datetime

mysql_conf = {
   'host':'192.168.137.1',
   'port':3306,
   'user':'root',
   'passwd':'123456',
   'db':'jddb',
   'charset':'utf8',
}

class test_mysql(object):
   def __init__(self):
      self._conn = pymysql.connect(**mysql_conf)
      self._table_name = 'tb_product_{0}'.format(datetime.now().strftime('%Y%m%d'))
      try:
         with self._conn.cursor() as cursor:
            sql = "CREATE TABLE IF NOT EXISTS {0}( \
                id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT, \
                product_id VARCHAR(16), \
                product_name CHARACTER(64), \
                product_price FLOAT, \
                product_url CHARACTER(128), \
                store_name CHARACTER(64), \
                store_url CHARACTER(128), \
                crawl_time CHARACTER(32) \
                );".format(self._table_name)
            cursor.execute(sql)
         self._conn.commit()
      except:
         raise

   def sql_insert(self,*args,**kwargs):
      try:
         with self._conn.cursor() as cursor:
            sql = "INSERT INTO {0}(product_id,product_name,product_price,product_url,store_name,store_url,crawl_time)  \
                  VALUES ('{product_id}','{product_name}',{product_price},'{product_url}','{store_name}','{store_url}','{crawl_time}')".format(self._table_name, **kwargs)
            cursor.execute(sql)
         self._conn.commit()
      except:
         raise

   def sql_test(self):
      try:
         with self._conn.cursor() as cursor:
            sql = "SELECT * FROM {0}".format(self._table_name)
            result = cursor.execute(sql)
            print(result)
            self._conn.commit()
      finally:
         self._conn.close()

if __name__=='__main__':
   test_sql = test_mysql()
   # result = test_sql.sql_test()

   kw = {
      'product_id':'2',
      'product_name': '2',
      'product_price': 1.0,
      'product_url': '2',
      'store_name': '2',
      'store_url': None,
      'crawl_time':'2',
   }
   result1 = test_sql.sql_insert(**kw)

   print('result >>> ',result1)


