# -*- coding: utf-8 -*-

from ScrapyJd.db import Db_Helper

kw = {
    'product_id': '2',
    'product_name': '2',
    'product_price': 1.0,
    'product_url': '2',
    'store_name': '2',
    'store_url': None,
    'crawl_time': '2',
}

sql = Db_Helper().db

# print(db)

sql.insert(**kw)


