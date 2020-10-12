import scrapy


class grammar(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    description = scrapy.Field()
    content = scrapy.Field()
    lesson_id = scrapy.Field()
