# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VanguardCardItem(scrapy.Item):
    name = scrapy.Field()
    card_type = scrapy.Field()
    group = scrapy.Field()
    race = scrapy.Field()
    nation = scrapy.Field()
    grade = scrapy.Field()
    power = scrapy.Field()
    critical = scrapy.Field()
    shield = scrapy.Field()
    skill = scrapy.Field()
    gift = scrapy.Field()
    effect = scrapy.Field()
    flavor = scrapy.Field()
    regulation = scrapy.Field()
    number = scrapy.Field()
    rarity = scrapy.Field()
    illustrator = scrapy.Field()
    image = scrapy.Field()
