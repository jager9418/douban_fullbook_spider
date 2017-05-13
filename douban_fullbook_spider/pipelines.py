# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from items import Douban_BooksItem
from scrapy.conf import settings
from scrapy import log

class DoubanFullbookSpiderPipeline(object):
    def process_item(self, item, spider):
        return item

class MongoDBPipeline(object):
    def __init__(self):
        self.server = settings['MONGODB_SERVER']
        self.port = settings['MONGODB_PORT']
        self.db = settings['MONGODB_DB']
        self.collection = settings['MONGODB_COLLECTION']

        connection = pymongo.MongoClient(self.server, self.port)
        db = connection[self.db]
        self.Books = db[self.collection]

    def process_item(self, item, spider):
        self.Books.insert(dict(item))
        # log.msg('Item written to MongoDB database %s/%s' % (self.db, self.Infor), level=log.DEBUG, spider=spider)
        return item
