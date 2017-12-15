# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst

from urllib.parse import urljoin


def process_author(value):
    if len(value) == 0:
        return "匿名用户"
    else:
        return value


def process_content(value):
    return value.replace('/n/n', '\n').replace('\n', '')


def process_image_url(value):
    if value is not None:
        return urljoin('https://pic.qiushibaike.com', value)
    else:
        return value


def process_image_url_output(value):
    return value


class QiuShiItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class QiushiItem(scrapy.Item):
    author = scrapy.Field(
        input_processor=MapCompose(process_author)
    )
    content = scrapy.Field(
        input_processor=MapCompose(process_content)
    )
    image_url = scrapy.Field(
        input_processor=MapCompose(process_image_url),
        output_processor=MapCompose(process_image_url_output)
    )
    image_path = scrapy.Field()
