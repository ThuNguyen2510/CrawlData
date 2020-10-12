import scrapy


class vocabulary(scrapy.Item):
    # define the fields for your item here like:
    means = scrapy.Field()
    content = scrapy.Field()
    lesson_id = scrapy.Field()
    audio = scrapy.Field()
    kanji = scrapy.Field()
