# -*- coding: utf-8 -*-
import scrapy
import json
from house591 import items

class GetSaleHouseSpider(scrapy.Spider):
    name = 'get_sale_house'
    allowed_domains = ['newhouse.591.com.tw']

    global rid
    global page
    rid = 1
    page = 1
    
    def request_url(self,rid,page):
        return 'https://newhouse.591.com.tw/home/housing/search?rid={rid}&page={page}'.format(rid=rid,page=page)
    
    def detail_url(self,hid):
        return 'https://newhouse.591.com.tw/home/housing/detail?hid={hid}'.format(hid=hid)

    def start_requests(self):
        global rid
        global page
        formdata = {
            'rid': str(rid),
            'page': str(page)
        }
        yield scrapy.FormRequest(url=self.request_url(rid,page) ,callback=self.parse)

    def parse(self, response):
        print('='*10+str(response.headers)+'='*10)
        global rid
        global page
        res = json.loads(response.text)
        next_page = response.xpath("//div[@class='pageBar']/a[@class='pageNext']").get()
        for data in res['data']['items']:
            data['house_status'] = data['status']
            data['tag'] = ','.join(data['tag'])
            del data['status']

            data_items = items.House591Item()
            for key in data: data_items[key] = data[key]
            yield data_items
            yield scrapy.Request(url=self.detail_url(data['hid']),
            callback=self.parse_detail,
            meta={'hid':data['hid']},
            cookies={})
        
        if len(res['data']['items']) == res['data']['per_page']:
            page += 1
            yield scrapy.Request(url=self.request_url(rid, page),callback=self.parse)
        else:
            # 區域ID過26則停止爬取
            if rid > 26:
                return
            else:
                rid += 1
                page = 1
                yield scrapy.Request(url=self.request_url(rid, page),callback=self.parse)
                
    # 進入詳細頁面爬取細部資訊
    def parse_detail(self,response):
        print('='*10+str(response.headers)+'='*10)
        hid = response.meta['hid']
        company = ''.join(response.xpath("//p[@class='company stonefont']/text()").getall()).strip()
        deal_complete = response.xpath("//p[@class='deal_date stonefont']/strong/text()").get()
        deal_date = ''.join(response.xpath("//p[@class='deal_date stonefont']/text()").getall()).strip()
        open_sell = ''.join(response.xpath("//p[@class='open_sell stonefont']/text()").getall()).strip()

        data_item = items.HouseDetailItem(hid=hid,
                                        company=company,
                                        deal_complete=deal_complete,
                                        deal_date=deal_date,
                                        open_sell=open_sell)
        yield data_item

        
