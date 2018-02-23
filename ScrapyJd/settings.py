# -*- coding: utf-8 -*-

from datetime import datetime

# Scrapy settings for ScrapyJd project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ScrapyJd'

SPIDER_MODULES = ['ScrapyJd.spiders']
NEWSPIDER_MODULE = 'ScrapyJd.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ScrapyJd (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16 #对当个网站进行并发请求的最大值
CONCURRENT_REQUESTS_PER_IP = 0  #对单个IP进行并发请求的最大值。如果非0则忽略DOMAIN设置。

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'ScrapyJd.middlewares.ScrapyjdSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'ScrapyJd.middlewares.ScrapyjdDownloaderMiddleware': 543,
   'ScrapyJd.middlewares.UserAgentmiddleware':400
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'ScrapyJd.pipelines.ScrapyjdPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True   #启用自动限速扩展
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5  #初始化下载延时 5s
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 30   #设置在高延迟情况下最大的下载延迟 30s
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False #用于启动Debug模式

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# HTTPERROR_ALLOWED_CODES = [301]

REDIRECT_ENABLED = True   #重定向 False为禁止

LOG_LEVEL = 'INFO'   #日志级别
LOG_FILE="./Logs/%s.txt"%datetime.now().strftime('%Y%m%d%H%M%S')  #输入日志到指定文件


########################################################################################################################################
#>>> Scrapy-Redis config
########################################################################################################################################

# 启动Redis调度存储请求队列
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'

# 确保所有的爬虫通过Redis去重
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'

# 是否在关闭时候保留原来的调度器和去重记录，True=保留，False=清空
SCHEDULER_PERSIST = True

# 是否在开始之前清空 调度器和去重记录，True=清空，False=不清空
# SCHEDULER_FLUSH_ON_START = False

# 最大空闲时间防止分布式爬虫因为等待而关闭
# SCHEDULER_IDLE_BEFORE_CLOSE = 10

# 将清除的项目在Redis中进行处理
# ITEM_PIPELINES = {
#     'scrapy_redis.pipelines.RedisPipeline': 300
# }

# 指定连接Redis的端口和地址（可选）
# REDIS_HOST = 'localhost'
# REDIS_PORT = 6379

# 设置此项优先级高于设置指定端口和地址
# 例：REDIS_URL = 'redis://root:password@hostname:port'
REDIS_URL = 'redis://root:@localhost:6379'


########################################################################################################################################
#>>> Scrapy_Redis_bloomfilter config
########################################################################################################################################

#启动bloomfilter调度
# SCHEDULER = 'scrapy_redis_bloomfilter.scheduler.Scheduler'

# 使用bloomfilter去重
# DUPEFILTER_CLASS = 'scrapy_redis_bloomfilter.dupefilter.RFPDupeFilter'

# BLOOMFILTER_HASH_NUMBER = 6

# BLOOMFILTER_BIT = 30


########################################################################################################################################
#>>> MongoDB config
########################################################################################################################################

Mongodb_Host = 'localhost'
Mongodb_Port = 27017
