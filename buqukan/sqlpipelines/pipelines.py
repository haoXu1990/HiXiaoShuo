from  .sql import Sql
from  buqukan.items import BuqukanItem

class BuqukanPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, BuqukanItem):
            name = item['book_name']
            ret = Sql.select_name(name)
            book_name = item['book_name']
            book_author = item['book_author']
            book_url = item['book_url']
            book_staus = item['book_status']
            book_TotalNumber = item['book_TotalNumber']
            book_category = item['book_category']
            lastTime = item['lastTime']

            #如果存在更新数据库
            if ret == 1:
                Sql.update_name(book_name, book_author, book_url, book_staus,book_TotalNumber, book_category, lastTime)
            else:
                Sql.insert_dd_name(book_name, book_author, book_url, book_staus,book_TotalNumber, book_category, lastTime)
                print('开始存储小说信息' + '\n')
     #   return item