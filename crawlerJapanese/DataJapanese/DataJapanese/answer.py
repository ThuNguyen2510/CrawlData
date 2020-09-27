import scrapy


class answer(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content = scrapy.Field()
    question_id = scrapy.Field()
    is_true = scrapy.Field()