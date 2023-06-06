import scrapy


class PepParseItem(scrapy.Item):
    """Класс специального объекта Item."""

    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
