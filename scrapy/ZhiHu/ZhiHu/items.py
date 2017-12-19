# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import re
import scrapy
import datetime


def extract_num(text):
    # 从字符串中提取出数字
    match_re = re.match(".*?(\d+).*", text)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0

    return nums


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ZhiHuQuestionItem(scrapy.Item):

    zhihu_id = scrapy.Field()
    topics = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    answer_num = scrapy.Field()
    comments_num = scrapy.Field()
    watch_user_num = scrapy.Field()
    click_num = scrapy.Field()
    crawl_time = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
            INSERT INTO question (zhihu_id, title, url, topics, content,
            answer_num, comments_num, watch_user_num, click_num, crawl_time)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        zhihu_id = self['zhihu_id'][0]
        title = self['title'][0]
        url = self['url'][0]
        topics = ', '.join(self['topics'])
        content = self['content']
        answer_num = extract_num(self['answer_num'][0])
        comments_num = extract_num(self['comments_num'][0])
        watch_user_num = int(self['watch_user_num'][0])
        click_num = int(self['click_num'][1])
        crawl_time = datetime.datetime.now()

        params = (zhihu_id, title, url, topics,
                  content, answer_num, comments_num,
                  watch_user_num, click_num, crawl_time)

        return insert_sql, params


class ZhiHuAnswerItem(scrapy.Item):
    zhihu_id = scrapy.Field()
    url = scrapy.Field()
    question_id = scrapy.Field()
    author_id = scrapy.Field()
    content = scrapy.Field()
    praise_num = scrapy.Field()
    comments_num = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()
    crawl_time = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
            INSERT INTO answer (zhihu_id, url, question_id, author_id, content,
            praise_num, comments_num, create_time, update_time, crawl_time)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        zhihu_id = int(self['zhihu_id'])
        url = self['url'][0]
        question_id = self['question_id']
        author_id = self['author_id']
        content = self['content']
        praise_num = self['praise_num']
        comments_num = self['comments_num']
        create_time = datetime.datetime.fromtimestamp(self['create_time'])
        update_time = datetime.datetime.fromtimestamp(self['update_time'])
        crawl_time = datetime.datetime.now()

        params = (zhihu_id, url, question_id, author_id,
                  content, praise_num, comments_num,
                  create_time, update_time, crawl_time)

        return insert_sql, params
