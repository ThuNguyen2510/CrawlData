# from scrapy.spiders import Spider
# from scrapy.selector import Selector
# from DataJapanese.grammar import grammar


# class CrawlerSpider(Spider):
#     name = "DataJapanese"
#     allowed_domains = ["lophoctiengnhat.com"]
#     start_urls = [
#         "https://lophoctiengnhat.com/50-bai-minnano-nihongo-bai-02_N5.html/1", ]

#     def parse(self, response):
#         i = 0
#         for row in response.xpath('//*[@class="khung-base "]'):
#             item = grammar()
#             i = str(i)
#             item['name'] = response.xpath('//div[@id="tab_0_'+i+'"]')[0].xpath('//tbody/tr[1]/td').extract_first()
#             item['lesson_id'] = 4
#             item['content'] = row.xpath('tbody').extract_first()           
#             item['description'] = response.xpath('//*[@class="khung-full"]//tbody').extract_first()
#             i = int(i) +1 
#             yield item
