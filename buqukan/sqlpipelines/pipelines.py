from  .sql import Sql
from  buqukan.items import BookDescItem

class BuqukanPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, BookDescItem):

            book_name = item['book_name']
            # 小说作者
            book_author =item['book_author']
            # 小说URL
            book_url = item['book_url']
            # 小说类别
            book_category = item['book_category']
            # 小说ID
            book_ID = item['book_ID']
            # 小说简介
            book_abstract = item['book_abstract']
            # 小说最新更新时间
            book_updatime = item['book_updatime']
            # 小说最新章节名称
            newchapterName = item['book_newChapterName']
            # 小说最新章节URL
            newchapterUrl = item['book_newChapterUrl']
            # 小说封面图片URL
            book_imageUrl = item['book_imageUrl']

            ret = Sql.select_name(book_name, book_author)

            #如果存在更新数据库
            if ret == 1:
                print('开始更新小说信息' + '\n')
                Sql.update_name(book_name, book_author, book_url, book_category, book_abstract, book_updatime, newchapterName, \
                                   newchapterUrl,book_imageUrl, book_ID )
            else:
                print('开始存储小说信息' + '\n')
                Sql.insert_dd_name(book_name, book_author, book_url, book_category, book_abstract, book_updatime, newchapterName, \
                                   newchapterUrl,book_imageUrl, book_ID )


