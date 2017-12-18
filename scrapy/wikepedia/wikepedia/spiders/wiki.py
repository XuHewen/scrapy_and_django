# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WikiSpider(CrawlSpider):
    name = 'wiki'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/']

    rules = (
        Rule(LinkExtractor(allow=r'en.wikipedia.org/wiki/',
                           deny=r'en.wikipedia.org/wiki/Wikipedia'),
             callback='parse_item',
             process_links='process_links',
             process_request='process_request',
             follow=True
             ),
    )

    def parse_start_url(self, response):
        return []

    def process_results(self, response, results):
        return results

    def process_links(self, links):
        return links

    def process_request(self, response):
        return response

    def parse_item(self, response):
        print(response.url)
