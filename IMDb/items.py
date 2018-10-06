# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    collection = 'IMDB'
    # define the fields for your item here like:
    # name = scrapy.Field()
    Name = scrapy.Field()
    Director = scrapy.Field()
    Writers = scrapy.Field()
    Stars = scrapy.Field()
    Score = scrapy.Field()
    Time = scrapy.Field()
    Description = scrapy.Field()
    URL = scrapy.Field()
