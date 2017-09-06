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
    def insert_dd_name(cls, book_name, book_author, book_url, book_staus, book_TotalNumber, book_category, lastTime):

        try:
            with db.cursor() as cursor:
                 sql = "INSERT INTO `buqukan` (`book_name`, `book_author`, `book_url`, `book_staus`,\
                 `book_category`, `lastTime`, `book_TotalNumber`) VALUES (%s, %s, %s, %s,%s, %s, %s)"

                 cursor.execute(sql, (book_name, book_author, book_url, book_staus, book_category, lastTime, book_TotalNumber))
                 # 执行sql语句
                 db.commit()
                 print(sql)
                 print('insert data success')
        except:
            # 发生错误时回滚
            db.rollback()
           # db.close()
            print("Error: insert field")
        # 关闭数据库连接
        #db.close()

    @classmethod
    def update_name(cls, book_name, book_author, book_url, book_staus, book_TotalNumber, book_category, lastTime):
        try:
            with db.cursor() as cursor:
                sql = "UPDATE `buqukan` SET `book_author`=%s, `book_url` = %s, `book_staus`=%s, \
                 `book_TotalNumber`=%s, `book_category`=%s, `lastTime`= %s WHERE `book_name`=%s"
                cursor.execute(sql, (book_author, book_url, book_staus,book_TotalNumber,book_category,lastTime, book_name))
                db.commit()
        except:
            db.rollback()
            print('Error: update error')


    @classmethod
    def select_name(cls, book_name):
        print('检查书名: ' + book_name)
        try:
            with db.cursor() as cursor:
                sql = "SELECT * FROM `buqukan` WHERE `book_name`=%s"
                #执行SQL语句
                #cursor.execute(sql, ('aaa', ))
                cursor.execute(sql, book_name)
                # 获取所有记录列表
                result = cursor.fetchall()[0]
                #print(result)
                return result['book_name'] == book_name
        except:
            print("Error: unable to fetch data")
           # db.close()
        # 关闭数据库连接
        #db.close()