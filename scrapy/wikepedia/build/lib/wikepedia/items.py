# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime


class WikepediaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()

    crawl_time = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = '''
            INSERT INTO wikipedia (url, title, content, crawl_time)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE title=VALUES(title), content=VALUES(content), crawl_time=VALUES(crawl_time)
        '''

        url = self['url']
        title = self['title']
        content = self['content']
        crawl_time = datetime.datetime.now()

        params = (url, title, content, crawl_time)

        return insert_sql, params





