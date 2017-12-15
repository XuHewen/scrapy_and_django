# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import pymysql
import pymysql.cursors
from twisted.enterprise import adbapi


class QiushiPipeline(object):
    def process_item(self, item, spider):
        return item


class QiuShiImagesPipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for ok, value in results:
            image_path = value['path']
            item['image_path'] = image_path
            print(image_path)
        return item


class QiuShiMysqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='808258',
            db='QiuShi',
            charset='utf8',
            use_unicode=True)

        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            INSERT INTO qiushi (author, image_url, image_path, content)
            VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(insert_sql,
                            (item['author'],
                             item.get('image_url', ''),
                             item.get('image_path', ''),
                             item['content']))
        self.conn.commit()

        return item

    def spider_closed(self, spider):
        self.conn.close()


class QiuShiTwistedMysqlPipeline(object):

    def __init__(self, db_pool):
        self.db_pool = db_pool

    @classmethod
    def from_settings(cls, settings):

        db_parms = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWORD'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True)

        db_pool = adbapi.ConnectionPool('pymysql', **db_parms)

        return cls(db_pool)

    def process_item(self, item, spider):
        query = self.db_pool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_err)
        return item

    def handle_err(self, failure):
        print(failure)

    def do_insert(self, cursor, item):
        insert_sql = """
            INSERT INTO qiushi (author, image_url, image_path, content)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_sql,
                       (item['author'],
                        item.get('image_url', ''),
                        item.get('image_path', ''),
                        item['content']))
