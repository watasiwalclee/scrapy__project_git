# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# 建立回傳物件
class House591Item(scrapy.Item):
    address = scrapy.Field()
    area = scrapy.Field()
    benefit_str = scrapy.Field()
    bid = scrapy.Field()
    build_article = scrapy.Field()
    build_name = scrapy.Field()
    build_type = scrapy.Field()
    call_num = scrapy.Field()
    cover = scrapy.Field()
    event_click = scrapy.Field()
    event_click_url = scrapy.Field()
    event_show = scrapy.Field()
    event_show_url = scrapy.Field()
    hid = scrapy.Field()
    is_full = scrapy.Field()
    is_full_720 = scrapy.Field()
    is_full_sky = scrapy.Field()
    is_video = scrapy.Field()
    isvip = scrapy.Field()
    native_orderno = scrapy.Field()
    phone = scrapy.Field()
    phone_ext = scrapy.Field()
    price = scrapy.Field()
    price_unit = scrapy.Field()
    purpose_str = scrapy.Field()
    region = scrapy.Field()
    regionid = scrapy.Field()
    room = scrapy.Field()
    section = scrapy.Field()
    sectionid = scrapy.Field()
    house_status = scrapy.Field()
    tag = scrapy.Field()
    updatetime = scrapy.Field()
    video_pic = scrapy.Field()

class HouseDetailItem(scrapy.Item):
    hid = scrapy.Field()
    company = scrapy.Field()
    deal_complete = scrapy.Field()
    deal_date = scrapy.Field()
    open_sell = scrapy.Field()