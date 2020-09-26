
import scrapy


class comment(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content = scrapy.Field()
    user_id = scrapy.Field()
    created_at = scrapy.Field()
    blog_id = scrapy.Field()