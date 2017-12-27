# -*- coding: utf-8 -*-
import os
# import sys
# import scrapy.pipelines.images
# Scrapy settings for QiuShi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'QiuShi'

SPIDER_MODULES = ['QiuShi.spiders']
NEWSPIDER_MODULE = 'QiuShi.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'QiuShi (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'QiuShi.middlewares.QiushiSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'QiuShi.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#     # 'QiuShi.pipelines.QiushiPipeline': 1,
#     # 'scrapy.pipelines.images.ImagesPipeline': 1,
#     # 'QiuShi.pipelines.QiuShiImagesPipeline': 2,
#     # 'QiuShi.pipelines.QiuShiTwistedMysqlPipeline': 2,
# }
IMAGES_URLS_FIELD = 'image_url'
image_dir = os.path.abspath(os.path.dirname(__file__))
IMAGES_STORE = os.path.join(image_dir, 'images')

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
}

MYSQL_HOST = "127.0.0.1"
MYSQL_DBNAME = "QiuShi"
MYSQL_USER = "root"
MYSQL_PASSWORD = "808258"


## scrapy redis setting

# Enables scheduling requests queue in redis
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'

# Ensuer all spiders share same duplicates filter through redis
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'

ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300,
}

# Specify the host and port to use when connecting to Redis (optional).
REDIS_HOST = '144.168.63.88'
REDIS_PORT = '6999'

LOG_LEVEL = 'ERROR'