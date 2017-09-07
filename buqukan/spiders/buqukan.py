import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from ..items import BookDescItem

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
        #for i in self.book_sort:
            #url = self.bash_url + str(i)
            yield  Request('http://zhannei.baidu.com/cse/search?q=&p=0&s=2758772450457967865&srt=totalClick&nsid=0', self.fetch_bookInfo)


    def fetch_bookInfo(self, response):
        soup = BeautifulSoup(response.text, 'lxml').find_all('div', {'class': 'result-item result-game-item'})

        #第一步找到小说封面图片
        for tag in soup:

            #获取到小说图片URL
            result_game_item_pic = tag.find('div', {'class': 'result-game-item-pic'})

            book_url = result_game_item_pic.find('a')['href']

            print('小说图片URL = ' + book_url)

            book_imageUrl = result_game_item_pic.find('img')['src']

            print('小说URL = ' + book_imageUrl)


            result_game_item_detail = tag.find('div',  {'class': 'result-game-item-detail'})

            book_name = result_game_item_detail.find('a', {'class': 'result-game-item-title-link'})['title']

            print('小说名字:' + book_name)

            #小说简介
            book_desc = result_game_item_detail.find('p', {'class': 'result-game-item-desc'})

            if book_desc == None:
                print(book_name + ':  没有简介')
                book_abstract = ''
            else:
                book_abstract =  re.sub(r'\r\n|&nbsp|\xa0|\\xa0|\u3000|\\u3000|\\u0020|\u0020', '', str(book_desc.text))
                print('小说简介：' + book_desc.text)

            result_game_item_info = result_game_item_detail.find_all('p',  {'class': 'result-game-item-info-tag'})

            #小说作者
            tmp = result_game_item_info[0].find_all('span')

            book_author = re.sub(r'\r\n|&nbsp|\xa0|\\xa0|\u3000|\\u3000|\\u0020|\u0020', '', str(tmp[1].text))

            print(book_author)

            #小说分类
            tmp1 = result_game_item_info[1].find_all('span', {'class': 'result-game-item-info-tag-title'})[1].text

            print(tmp1)

            #最新更新时间
            tmp2 = result_game_item_info[2].find_all('span', {'class': 'result-game-item-info-tag-title'})[1].text

            print(tmp2)

            newchapter = result_game_item_info[3].find('a')

            newchapterName = re.sub(r'\n|&nbsp|\xa0|\\xa0|\u3000|\\u3000|\\u0020|\u0020', '', str(newchapter.text))

            newchapterUrl =  re.sub(r'\n|&nbsp|\xa0|\\xa0|\u3000|\\u3000|\\u0020|\u0020', '', str(newchapter['href']))

            print(newchapterName)
            print(newchapterUrl)

            print('\n')

            item = BookDescItem()
            # 小说名字
            item['book_name'] = book_name
            # 小说作者
            item['book_author'] = book_author
            # 小说URL
            item['book_url'] = book_url
            # 小说类别
            item['book_category'] =  tmp1
            # 小说ID
            item['book_ID'] = ''
            # 小说简介
            item['book_abstract'] = book_abstract
            # 小说最新更新时间
            item['book_updatime'] = tmp2
            # 小说最新章节名称
            item['book_newChapterName'] = newchapterName
            # 小说最新章节URL
            item['book_newChapterUrl'] = newchapterUrl
            # 小说封面图片URL
            item['book_imageUrl'] = book_imageUrl
            yield item





    # #获取书的url
    # def parse(self, response):
    #     soup = BeautifulSoup(response.text, 'lxml').find_all('div', {'class': 'll'})
    #     for v in soup:
    #         for a in v.find_all('div',{'class': 'image'}):
    #             url = self.bash_url + a.find('a')['href']
    #             print(url)
    #             yield Request(url, callback=self.get_name, meta={'url':url})
    #
    # #获取书名, url
    # def get_name(self, response):
    #     soup = BeautifulSoup(response.text, 'lxml').find('div', {'class' : 'info'})
    #     book_name1 = soup.find('h2').string
    #     info = soup.find('div', {'class' : 'small'}).contents
    #     book_author = info[0].string
    #     book_status = info[2].string
    #     book_TotalNumber = re.sub("\D", "", info[3].string)
    #     book_category = info[1].string
    #     lastTime = info[4].string
    #     item = BuqukanItem()
    #     item['book_author'] = book_author.replace('作者：', '', 1)
    #     item['book_name'] = book_name1
    #     item['book_url'] = response.meta['url']
    #     item['book_status'] = book_status.replace('状态：', '', 1)
    #     item['book_TotalNumber'] = book_TotalNumber
    #     item['book_category'] = book_category.replace('分类：', '', 1)
    #     item['lastTime'] = lastTime.replace('更新时间：', '', 1)
    #     yield item
    #     yield Request(response.meta['url'], self.get_chapterurl, meta={'book_name':book_name1,
    #                                                                  'url':response.meta['url'],
    #                                                                  'book_author':info[0].string,
    #                                                                  'book_status':info[2].string,
    #                                                                  'book_TotalNumber':info[3].string,
    #                                                                  'book_category':info[1].string,
    #                                                                  'lastTime':info[4].string})

    # def get_chapterurl(self, response):
    #     pass
    #

