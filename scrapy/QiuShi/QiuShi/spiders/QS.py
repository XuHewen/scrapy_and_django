# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.loader import ItemLoader

from urllib.parse import urljoin
from QiuShi.items import QiushiItem
from QiuShi.items import QiuShiItemLoader

import time


class QsSpider(scrapy.Spider):
    name = 'QS'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/hot/']

    def parse(self, response):

        urls = response.xpath('//div[contains(@class, "article")]//a[@class="contentHerf"]/@href').extract()

        for url in urls:
            url = urljoin(response.url, url)
            yield Request(url, callback=self.parse_single)

        xpath_str = '//ul[@class="pagination"]/li[last()]/a/@href'
        xpath_str2 = '//ul[@class="pagination"]/li[last()]//span/text()'

        next_word = response.xpath(xpath_str2).extract()[0]
        next_url = response.xpath(xpath_str).extract()[0]

        if next_word.strip() == "下一页" and next_url:
            next_url = response.xpath(xpath_str).extract()[0]
            next_url = urljoin(response.url, next_url)
            yield Request(next_url, callback=self.parse)

    def parse_single(self, response):
        time.sleep(0.5)
        qsItem = QiushiItem()

        author_xpath = '//div[contains(@class, "author")]//a[last()]/h2/text()'
        content_xpath = '//div[@class="content"]/text()'
        image_url_xpath = '//div[@class="thumb"]/img/@src'
        item_loader = QiuShiItemLoader(item=qsItem, response=response)
        item_loader.add_xpath('author', author_xpath)
        item_loader.add_xpath('content', content_xpath)
        item_loader.add_xpath('image_url', image_url_xpath)

        return item_loader.load_item()
