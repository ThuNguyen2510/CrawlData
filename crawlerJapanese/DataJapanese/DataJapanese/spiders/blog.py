from scrapy.spiders import Spider
from scrapy.selector import Selector
from DataJapanese.blog import blog
import random


class CrawlerSpider(Spider):
    name = "DataJapanese"
    allowed_domains = ["jes.edu.vn"]
    start_urls = [
        "https://jes.edu.vn/thanh-ngu-tieng-nhat-ve-cuoc-song-hay-nhat",
    ]

    def parse(self, response):
        # questions = Selector(response).xpath('//div[@class="td-big-grid-wrapper"]/div[@class="td-big-grid-scroll"]/div')
        # questions = Selector(response).xpath(
        #     '//div[@class="td-pb-span8 td-main-content"]/div[@class="td-ss-main-content"]/div')
        questions = Selector(response).xpath(
            '//div[@class="td-ss-main-content"]')
        for question in questions:
            item = blog()
            # item['type_id'] = 2
            # item['user_id'] = random.randrange(15)
            # thuộc thẻ nào của html
            # item['title'] = question.xpath('div[@class="td-module-thumb"]/a/@title').extract_first()
            # item['image'] = question.xpath(
            #     'div[@class="td-module-thumb"]/a/img/@src').extract_first()
            # item['content'] = ""
            # item['created_at'] = question.xpath(
            #     'div[@class="td-meta-info-container"]/div[@class="td-meta-align"]/div[@class="td-module-meta-info"]/span[@class="td-post-date"]/@datetime').extract_first()

            # item['title'] = question.xpath(
            #     'div[@class="td-block-span6"]//div[@class="item-details"]/h3/a/@title').extract_first()
            # item['image'] = question.xpath(
            #     'div[@class="td-block-span6"]//div[@class="td-module-thumb"]/a/img/@src').extract_first()
            item['content'] = question.xpath('//div[@class="td-post-content"]').extract_first()
            # item['created_at'] = question.xpath(
            #     'div[@class="td-block-span6"]//div[@class="item-details"]/div[@class="td-module-meta-info"]/span[@class="td-post-date"]/time/@datetime').extract_first()

            yield item
