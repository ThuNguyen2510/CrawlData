import scrapy


class question(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content = scrapy.Field()
    test_id = scrapy.Field()