#-*- coding:utf-8 -*-

import re
import datetime
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request
from douban_fullbook_spider.items import Douban_BooksItem

class Spider(CrawlSpider):
    name = 'DoubanbooksSpider'

    allowed_domains=['douban.com']

    start_urls = [
        'https://book.douban.com/tag/?icn=index-nav'
    ]

    # 爬虫规则
    rules = (
        Rule(LinkExtractor(allow='/tag/', restrict_xpaths='//div[@class="article"]'), follow=True),
        Rule(LinkExtractor(allow='\?start=\d+\&type=', restrict_xpaths='//div[@class="paginator"]'), follow=True),
        Rule(LinkExtractor(allow='/subject/\d+/$', restrict_xpaths='//ul[@class="subject-list"]'), callback='parse_item')

    )

    def parse_item(self, response):
        def value(list):
            return list[0] if len(list) else ' '
        item = Douban_BooksItem()
        sel = Selector(response)

        item['book_id'] = response.url.split('/')[-2]
        item['book_name'] = value(sel.xpath('//div[@id="wrapper"]/h1/span/text()').extract())
        item['author_info'] = ''
        author_info = sel.xpath('//div[@id="info"]/a[1]/text()').extract()
        if author_info:
            item['author_info'] = ''.join(author_info).strip().replace('\n', '')
        item['book_star'] = value(sel.xpath('//div[@class="rating_self clearfix"]/strong/text()').extract())
        item['people_num'] = value(sel.xpath('//div[@class="rating_sum"]/span/a/span/text()').extract())
        item['book_quote'] = ''
        book_quote = sel.xpath('//div[@class="intro"]//p/text()').extract()
        if book_quote:
            for line in book_quote:
                item['book_quote'] = item['book_quote'] + line

        item['author_quote'] = ''
        author_quote = sel.xpath('//div[@class="indent "]/div/div[@class="intro"]//p/text()').extract()
        if author_quote:
            for l in author_quote:
                item['author_quote'] = item['author_quote'] + l

        yield item










