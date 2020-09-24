from scrapy.spiders import Spider
from scrapy.selector import Selector
from DataJapanese.hiragana import hiragana

class CrawlerSpider(Spider):
    name = "DataJapanese"
    allowed_domains = ["tofugu.com"]
    start_urls = [
        "https://www.tofugu.com/japanese/learn-hiragana/",
    ]
    
    def parse(self, response):
        questions = Selector(response).xpath('//ul/li[@class="article-audio-sentence-player"]')

        for question in questions:
            item = hiragana()
            # thuộc thẻ nào của html
            item['alphabet_id'] = 1
            item['image'] = ""
            item['content'] = ""
            item['audio'] = question.xpath(
                'audio/@src').extract_first()
            yield item