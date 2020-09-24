
import scrapy


class hiragana(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    alphabet_id = scrapy.Field()
    content = scrapy.Field()
    audio = scrapy.Field()
    image = scrapy.Field()
    