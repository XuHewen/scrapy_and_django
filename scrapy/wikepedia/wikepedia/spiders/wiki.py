# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wikepedia.items import WikepediaItem

from selenium import webdriver
from pydispatch import dispatcher
from scrapy import signals


class WikiSpider(CrawlSpider):
    name = 'wiki'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/']

    rules = (
        Rule(LinkExtractor(allow=r'en.wikipedia.org/wiki',
                           deny=[r'en.wikipedia.org/wiki/Wikipedia',
                                 r'en.wikipedia.org/wiki/Special',
                                 r'en.wikipedia.org/wiki/.*?:.*',
                                 r'en.wikipedia.org/wiki/Main_Page']),
             callback='parse_item',
             process_links='process_links',
             process_request='process_request',
             follow=True
             ),
    )

    # 启动浏览器，并在spider关闭时关闭浏览器
    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     super(WikiSpider, self).__init__()
    #     dispatcher.connect(self.spider_closed, signals.spider_closed)

    # def spider_closed(self, spider):
    #     print('spider closed')
    #     self.driver.quit()

    def parse_start_url(self, response):
        return []

    def process_results(self, response, results):
        return results

    def process_links(self, links):
        return links

    def process_request(self, response):
        return response

    def parse_item(self, response):
        xpath_title = 'string(//h1[@id="firstHeading"])'
        xpath_content = '//div[@id="bodyContent"]'

        item = WikepediaItem()

        title = response.xpath(xpath_title).extract_first()
        content = response.xpath(xpath_content).extract_first()

        item['url'] = response.url
        item['title'] = title
        item['content'] = content

        # yield item
        print(title)
