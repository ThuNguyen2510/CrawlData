
import scrapy


class blog(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    user_id = scrapy.Field()
    created_at = scrapy.Field()
    image = scrapy.Field()
    type_id = scrapy.Field()