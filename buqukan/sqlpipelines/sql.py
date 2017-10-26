import  pymysql.cursors
from buqukan import settings


MYSQL_HOSTS = settings.MYSQL_HOST
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

# 打开数据库连接
db = pymysql.connect(host=MYSQL_HOSTS,
                     user=MYSQL_USER,
                     password=MYSQL_PASSWORD,
                     db=MYSQL_DB,
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)

class Sql:
    @classmethod
    def insert_dd_name(cls, book_name, book_author, book_url, book_category, book_abstract, book_updatime, book_newChapterName, \
                       book_newChapterUrl,book_imageUrl, book_ID ):
        try:
            with db.cursor() as cursor:

                 sql = "INSERT INTO `hixiaoshuo` (`book_name`, `book_author`, `book_url`, `book_category`,\
                 `book_abstract`, `book_updatime`, `book_newChapterName`, `book_newChapterUrl`, `book_imageUrl`, `book_id`)\
                  VALUES (%s, %s, %s, %s,%s, %s, %s,%s, %s, %s)"

                 cursor.execute(sql, (book_name, book_author, book_url, book_category, book_abstract, book_updatime, book_newChapterName, \
                                      book_newChapterUrl,book_imageUrl,book_ID))
                 # 执行sql语句
                 db.commit()
                # print(sql)
                 print('insert data success')
        except:
            # 发生错误时回滚
            db.rollback()
           # db.close()
            print("Error: insert field")
        # 关闭数据库连接
        #db.close()

    @classmethod
    def update_name(cls, book_name, book_author, book_url, book_category, book_abstract, book_updatime, book_newChapterName, \
                       book_newChapterUrl,book_imageUrl, book_ID ):
        try:
            with db.cursor() as cursor:
                sql = "UPDATE `hixiaoshuo` SET `book_name`=%s, `book_author`=%s, `book_url`=%s, `book_category`=%s,\
                                 `book_abstract`=%s, `book_updatime`=%s, `book_newChapterName`=%s, `book_newChapterUrl`=%s,\
                                  `book_imageUrl`=%s, `book_id`=%s  WHERE `book_name`=%s"

                cursor.execute(sql, (
                book_name, book_author, book_url, book_category, book_abstract, book_updatime, book_newChapterName, \
                book_newChapterUrl, book_imageUrl, book_ID,book_name ))
                db.commit()
                print('update success')
        except:
            db.rollback()
            print('Error: update error')


    @classmethod
    def select_name(cls, book_name, book_author):
        print('检查书名: ' + book_name)
        try:
            with db.cursor() as cursor:
                sql = "SELECT * FROM `hixiaoshuo` WHERE `book_name`=%s AND `book_author`=%s"

                #这里要对Book_name, book_author 出去掉空格、回车、换行等符号在做出比较

                #执行SQL语句
                cursor.execute(sql, (book_name, book_author))
                # 获取所有记录列表

                result = cursor.fetchone()

                if result == None:
                    print('数据库中没有存储' + book_author + '作者写的：' + book_name)

                    return 0
                else:
                    print('数据库中存在' + book_author + '作者写的：' + book_name)
                    return 1
        except:
            print("Error: unable to fetch data")
           # db.close()
        # 关闭数据库连接
        #db.close()