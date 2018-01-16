# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class WikepediaPipeline(object):
#     def process_item(self, item, spider):
#         return item
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi


class WikipediaPipeline(object):

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
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True)

        db_pool = adbapi.ConnectionPool('MySQLdb', **db_parms)

        return cls(db_pool)

    def process_item(self, item, spider):
        query = self.db_pool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_err, item, spider)
        return item

    def handle_err(self, failure, item, spider):
        print(failure)

    def do_insert(self, cursor, item):

        insert_sql, params = item.get_insert_sql()

        cursor.execute(insert_sql, params)


class ElasticSearchPipeline(object):

    def process_item(self, item, spider):
        item.save_to_es()
        return item
