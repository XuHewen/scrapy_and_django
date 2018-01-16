# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import datetime

import scrapy
from elasticsearch_dsl import connections
from w3lib.html import remove_tags

from wikipedia.models import es_types
from wikipedia.models.es_types import WikiType

from wikipedia.utils.md5 import md5


es = connections.create_connection(WikiType._doc_type.using)


def gen_suggests(index, info_tuple):
    used_words = set()
    suggests = []
    for text, weight in info_tuple:
        if text:
            words = es.indices.analyze(index=index,
                                       body={'analyzer': 'standard', 'text': text})
            anylyzed_words = set([r['token']
                                  for r in words['tokens'] if len(r['token']) > 1])
            new_words = anylyzed_words - used_words
            used_words.update(words)
        else:
            new_words = set()
        if new_words:
            suggests.append({'input': list(new_words), 'weight': weight})

    return suggests


class WikipediaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()

    created_time = scrapy.Field()
    update_time = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = '''
            INSERT INTO wikipedia (no, url, title, content, created_time, update_time)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE url=VALUES(url), title=VALUES(title),content=VALUES(content), update_time=VALUES(update_time)
        '''

        url = self['url']
        title = self['title']
        content = self['content']
        created_time = datetime.datetime.now()
        update_time = datetime.datetime.now()
        
        md5_str = url + '@@@' + title
        no = md5(md5_str)

        params = (no, url, title, content, created_time, update_time)

        return insert_sql, params

    def save_to_es(self):
        article = es_types.WikiType()
        article.title = self['title']
        article.url = self['url']

        article.content = remove_tags(self['content'])
        article.suggest = gen_suggests(article._doc_type.index,
                                       ((article.title, 10),))

        article.save()
