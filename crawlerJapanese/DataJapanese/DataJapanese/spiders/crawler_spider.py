# from scrapy.spiders import Spider
# from scrapy.selector import Selector
# from DataJapanese.hiragana import hiragana

# class CrawlerSpider(Spider):
#     name = "DataJapanese"
#     allowed_domains = ["nhk.or.jp"]
#     start_urls = [
#         "https://www.nhk.or.jphttps://www.nhk.or.jp/lesson/vi/letters/hiragana.html",
#     ]
    
#     def parse(self, response):
#         questions = Selector(response).xpath('//ul[@class="letters-list"]/li')

#         for question in questions:
#             item = hiragana()
#             # thuộc thẻ nào của html
#             item['alphabet_id'] = 1
#             item['image'] = question.xpath(
#                 'img/@src').extract_first()
#             item['content'] = question.xpath(
#                 'img/@alt').extract_first()
#             item['audio'] = question.xpath(
#                 'img/@src').extract_first()
#             yield item