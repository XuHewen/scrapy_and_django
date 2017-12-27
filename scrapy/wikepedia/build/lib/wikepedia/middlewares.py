# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from fake_useragent import UserAgent
import random


class WikepediaSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RandomUserAgentMiddleware(object):
    '''
    随机更换User-Agent
    '''

    def __init__(self, crawler):
        super(RandomUserAgentMiddleware, self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get('RANDOM_UA_TYPE', 'random')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):

        def get_ua():
            return getattr(self.ua, self.ua_type)
        request.headers.setdefault('User-Agent', get_ua())


class MyproxiesSpiderMiddleware(object):

    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        thisip = random.choice(IPPOOL)
        print("this is ip:" + thisip["ipaddr"])
        request.meta['proxy'] = 'http://' + thisip['ipaddr']


IPPOOL = [
    {"ipaddr": "61.129.70.131:8080"},
    {"ipaddr": "61.152.81.193:9100"},
    {"ipaddr": "120.204.85.29:3128"},
    {"ipaddr": "219.228.126.86:8123"},
    {"ipaddr": "61.152.81.193:9100"},
    {"ipaddr": "218.82.33.225:53853"},
    {"ipaddr": "223.167.190.17:42789"}
]

# class JSPageMiddleware(object):

#     def process_request(self, request, spider):
#         if spider.name == 'wiki':
#             spider.driver.get(request.url)

#             import time
#             from scrapy.http import HtmlResponse
#             print(u'浏览器安全检查，强行等待6秒')
#             time.sleep(60)

#             return HtmlResponse(url=spider.driver.current_url,
#                                 encoding='utf-8',
#                                 body=spider.driver.page_source,
#                                 request=request)
