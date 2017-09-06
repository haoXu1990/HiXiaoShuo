import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from ..items import BuqukanItem
import re

class Myspider(scrapy.Spider):
    # 玄幻： http://www.biqukan.com/xuanhuanxiaoshuo/

    # 修真：http://www.biqukan.com/xiuzhenxiaoshuo/

    # 都市： http://www.biqukan.com/dushixiaoshuo/

    # 穿越： http://www.biqukan.com/chuanyuexiaoshuo/

    # 网游： http://www.biqukan.com/wangyouxiaoshuo/

    # 科幻： http://www.biqukan.com/kehuanxiaoshuo/

    # 完本：http://www.biqukan.com/wanben/
    name = 'buqukan'
    bash_url = 'http://www.biqukan.com/'
    book_sort = ('xuanhuanxiaoshuo/', 'xiuzhenxiaoshuo/', 'dushixiaoshuo/', 'chuanyuexiaoshuo/')

    def start_requests(self):
        for i in self.book_sort:
            url = self.bash_url + str(i)
            yield  Request(url, self.parse)
    #获取书的url
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml').find_all('div', {'class': 'll'})
        for v in soup:
            for a in v.find_all('div',{'class': 'image'}):
                url = self.bash_url + a.find('a')['href']
                print(url)
                yield Request(url, callback=self.get_name, meta={'url':url})

    #获取书名, url
    def get_name(self, response):
        soup = BeautifulSoup(response.text, 'lxml').find('div', {'class' : 'info'})
        book_name1 = soup.find('h2').string
        info = soup.find('div', {'class' : 'small'}).contents
        book_author = info[0].string
        book_status = info[2].string
        book_TotalNumber = re.sub("\D", "", info[3].string)
        book_category = info[1].string
        lastTime = info[4].string
        item = BuqukanItem()
        item['book_author'] = book_author.replace('作者：', '', 1)
        item['book_name'] = book_name1
        item['book_url'] = response.meta['url']
        item['book_status'] = book_status.replace('状态：', '', 1)
        item['book_TotalNumber'] = book_TotalNumber
        item['book_category'] = book_category.replace('分类：', '', 1)
        item['lastTime'] = lastTime.replace('更新时间：', '', 1)
        yield item
        yield Request(response.meta['url'], self.get_chapterurl, meta={'book_name':book_name1,
                                                                     'url':response.meta['url'],
                                                                     'book_author':info[0].string,
                                                                     'book_status':info[2].string,
                                                                     'book_TotalNumber':info[3].string,
                                                                     'book_category':info[1].string,
                                                                     'lastTime':info[4].string})

    def get_chapterurl(self, response):
        pass


