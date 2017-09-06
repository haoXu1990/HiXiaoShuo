# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BuqukanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #小说名字
    book_name = scrapy.Field()
    #小说作者
    book_author = scrapy.Field()
    #小说URL
    book_url = scrapy.Field()
    #小说状态
    book_status = scrapy.Field()
    #小说连载字数
    book_TotalNumber = scrapy.Field()
    #小说类别
    book_category = scrapy.Field()
    #小说ID
    book_ID = scrapy.Field()
    #最后更新时间
    lastTime = scrapy.Field()

class DcontentItem(scrapy.Item):
    id_name = scrapy.Field()
    #小说编号
    chaptercontent = scrapy.Field()
    #章节内容
    num = scrapy.Field()
    #用于绑定章节顺序
    chapterurl = scrapy.Field()
    #章节URL
    chaptername = scrapy.Field()