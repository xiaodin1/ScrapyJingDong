# -*- coding:utf-8 -*-

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from ScrapyJd.spiders import producturl

settings = get_project_settings()
process = CrawlerProcess(settings=settings)
process.crawl(producturl.ProducturlSpider)

process.start()
