# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
from scrapy.item import Item, Field


class IherbItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()
    brand = Field()
    desc = Field()
    price = Field(default="1000")
