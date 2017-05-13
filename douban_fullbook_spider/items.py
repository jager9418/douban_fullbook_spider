# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanFullbookSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Douban_BooksItem(scrapy.Item):
    """
    书本属性
    book_id 书本序号
    book_name 书名
    book_star 评分
    people_num 评价人数
    author_info 作者

    book_quote 内容简介
    image_urls 书本封面
    """
    book_id = scrapy.Field()
    book_name = scrapy.Field()
    book_star = scrapy.Field()
    people_num = scrapy.Field()
    author_info = scrapy.Field()

    book_quote = scrapy.Field()
    author_quote = scrapy.Field()
    image_urls = scrapy.Field()