# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class NewAmazingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Source = scrapy.Field()
    GrupCd = scrapy.Field()
    GrupSnm = scrapy.Field()
    LeavDt = scrapy.Field()
    GrupLn = scrapy.Field()
    SaleAm = scrapy.Field()
    SaleYqt = scrapy.Field()
    EstmTotqt = scrapy.Field()
    HotTpNm = scrapy.Field()
    SubCdAnm = scrapy.Field()

class ShiPangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Source = scrapy.Field()
    GrupCd = scrapy.Field()
    GrupSnm = scrapy.Field()
    LeavDt = scrapy.Field()
    GrupLn = scrapy.Field()
    SaleAm = scrapy.Field()
    SaleYqt = scrapy.Field()
    EstmTotqt = scrapy.Field()
    HotTpNm = scrapy.Field()
    SubCdAnm = scrapy.Field()

class NewAmazingDetailItem(scrapy.Item):
    Source = scrapy.Field()
    GrupCd = scrapy.Field()
    GrupLn = scrapy.Field()
    diposit = scrapy.Field()
    fee_explanation = scrapy.Field()
    main_chara = scrapy.Field()
    include_item = scrapy.Field()
    not_include_item = scrapy.Field()

class ShiPangDetailItem(scrapy.Item):
    Source = scrapy.Field()
    GrupCd = scrapy.Field()
    GrupLn = scrapy.Field()
    diposit = scrapy.Field()
    fee_explanation = scrapy.Field()
    main_chara = scrapy.Field()
    include_item = scrapy.Field()
    not_include_item = scrapy.Field()