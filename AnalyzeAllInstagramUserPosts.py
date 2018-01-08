"""
Scrape alt. Instagram website for each of the following properties of each post of a user:
- Likes
- Comments
- Image URL
- Timestamp
"""

import scrapy
from scrapy import Selector
from scrapy.contrib.spiders import Rule
from scrapy.linkextractors import LinkExtractor
import time

class InstagramItem(scrapy.Item):
    image_urls = scrapy.Field()
    numLikes = scrapy.Field()
    numComments = scrapy.Field()
    date = scrapy.Field()

###### Instagram spider #######
class instagramSpider(scrapy.Spider):

    ###### Name of spider, allowed space, and starting page #######
    name = 'insta_pictures_spider'
    allowed_domains = ['snap361.com']
    start_urls = ["http://snap361.com/ig-user/ENTER_YUSERNAME_HERE/"]

    ###### Used to track page #######
    global page_num
    page_num = 1

    def parse(self, response):
        global page_num
        page_tries = 1

        time.sleep(5) #Forces 5 second delay per parse

        ###### Extract post #######
        all_posts = response.xpath('//div[@class="grid-item"]').extract()

        ###### Iterate through post in page #######
        for post in all_posts:
            ###### Finds all desired items from post #######
            url = (Selector(text=post)).xpath('//div[@class="imgbox"]/a/@href').extract()
            nLikes = Selector(text=post).xpath('//div[@class="post-meta"]//span[@class="likes"]/text()'
                                               ).extract()
            timestamp = Selector(text=post).xpath('//div[@class="post-meta"]//span[@class="time"]/text()').extract()
            numCom = Selector(text=post).xpath('//div[@class="post-meta"]//span[@class="comments"]/text()').extract()

            ###### Checks to see if url exists before storing properties in item #######
            if url:
                item = InstagramItem()
                item['image_urls'] = url[0]
                item['numLikes'] = nLikes[0]
                item['numComments'] = numCom[0]
                item['date'] = timestamp[0]
                yield item

        # follow next page links
        while(page_tries < 4):
            next_page = response.xpath('//div[@class="nextpage"]/a/@href').extract()
            base_url = "http://snap361.com"
            if next_page:
                print "=" * 50
                print "Go to next page"
                page_tries = 5
                next_href = base_url + next_page[0]
                print next_href
                request = scrapy.Request(url=next_href, callback=self.parse)
                page_num = page_num + 1
                print page_num
                yield request
            else:
                page_tries = page_tries + 1
                print("on next page try:" + str(page_tries))
                if(page_tries == 4):
                    print("No next page \n")





