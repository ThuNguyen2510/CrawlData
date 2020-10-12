# from scrapy.spiders import Spider
# from scrapy.selector import Selector
# from DataJapanese.vocabulary import vocabulary


# class CrawlerSpider(Spider):
#     name = "DataJapanese"
#     allowed_domains = ["lophoctiengnhat.com"]
#     start_urls = [
#         "https://lophoctiengnhat.com/50-bai-minnano-nihongo-bai-02_N5.html/0", ]

#     def parse(self, response):
#         for row in response.xpath('//*[@class="khungTuVung6C xanh"]//tbody//tr'):
#             item = vocabulary()
#             item['lesson_id'] = 4
#             item['content'] = row.xpath('td[2]//text()').extract_first()
#             path = row.xpath('td[3]').extract_first()
#             if row.xpath('td[3]').extract_first() == "<td></td>":
#                 path = row.xpath('td[4]').extract_first()
#             start = path.find('/public')
#             end = path.find('.mp3') + 4
#             item['audio'] = None
#             if path[start: end] != "":
#                 item['audio'] = "https://lophoctiengnhat.com" + path[start: end]
#             item['kanji'] = row.xpath('td[5]//text()').extract_first()
#             item['means'] = row.xpath('td[7]//text()').extract_first()
#             yield item
