# from scrapy.spiders import Spider
# from scrapy.selector import Selector
# from DataJapanese.alphabet import alphabet

# class CrawlerSpider(Spider):
#     name = "DataJapanese"
#     allowed_domains = ["nhk.or.jp"]
#     start_urls = [
#         "https://www.nhk.or.jp/lesson/vi/letters/katakana.html",
#     ]
    
#     def parse(self, response):
#         questions = Selector(response).xpath('//ul[@class="letters-list"]/li[@class="module-modal"]')

#         for question in questions:
#             item = alphabet()
#             # thuộc thẻ nào của html
#             item['alphabet_id'] = 2
#             item['image'] = "https://www.nhk.or.jp/" + question.xpath(
#                 'img/@src').extract_first()
#             item['content'] = question.xpath(
#                 'img/@alt').extract_first()
#             item['audio'] = "https://0.tqn.com/z/g/japanese/library/media/audio/"+ question.xpath(
#                 'img/@alt').extract_first()+".mp3" 
#             yield item