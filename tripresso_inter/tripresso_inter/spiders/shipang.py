# -*- coding: utf-8 -*-
import scrapy
import json
from tripresso_inter.items import ShiPangItem, ShiPangDetailItem

class ShipangSpider(scrapy.Spider):
    name = 'shipang'
    allowed_domains = ['4p.com.tw']
    start_urls = ['https://4p.com.tw/']

    global page
    page = 1

    def post_data(self, page):
        data = {
            'pageALL': str(page),
            'beginDt': '2020/07/06',
            'endDt': '2021/07/06'
        }
        return data

    def start_requests(self):
        search_list_data_url = 'https://www.4p.com.tw/EW/Services/SearchListData.asp'
        global page
        data = self.post_data(page)
        yield scrapy.FormRequest(url=search_list_data_url, formdata=data, callback=self.parse_lsit)

    def parse_lsit(self, response):
        search_list_data_url = 'https://www.4p.com.tw/EW/Services/SearchListData.asp'
        res = json.loads(response.text)
        if len(res['All']) != 0:
            for data in res['All']:
                item = ShiPangItem()
                item['Source'] = '世邦旅行社'
                item['GrupCd'] = data['GrupCd']
                item['GrupSnm'] = data['GrupSnm']
                item['LeavDt'] = data['LeavDt'].replace('/','-')
                item['GrupLn'] = data['GrupLn']
                item['SaleAm'] = data['SaleAm']
                item['EstmTotqt'] = data['EstmTotqt']
                item['HotTpNm'] = data['HotTpNm']
                item['SubCdAnm'] = data['SubCdAnm']
                item['SaleYqt'] = data['SaleYqt']
                detail_url = 'https://www.4p.com.tw' + data['Url']
                yield item
                # 爬取細部內容網頁
                yield scrapy.Request(url=detail_url, callback=self.parse_detail,meta={'GrupCd':data['GrupCd'], 'Source':'世邦旅行社'})
            global page
            page += 1
            data = self.post_data(page)
            yield scrapy.FormRequest(url=search_list_data_url, formdata=data, callback=self.parse_lsit)

    def parse_detail(self, response):
        res = response.xpath("//div[@class='product_basic_info animatedParent article']/ul[@class='animated fadeInUpShort slow']//text()").getall()
        res = list(filter(None,[t.strip() for t in res]))
        item = ShiPangDetailItem()
        item['GrupCd'] = response.meta['GrupCd']
        item['Source'] = response.meta['Source']
        
        if '旅遊天數：' in res:
            index = res.index('旅遊天數：')
            if '：' not in res[index+1]: item['GrupLn'] = res[index+1]
        else:
            with open('error.txt','a+', encoding='utf-8') as f:
                f.write(str(item['GrupCd']) + '  ' + '沒有旅遊天數' + '\n')
        
        if '每人訂金：' in res:
            index = res.index('每人訂金：')
            if '：' not in res[index+1]: item['diposit'] = res[index+1]
        else:
            with open('error.txt','a+', encoding='utf-8') as f:
                f.write(str(item['GrupCd']) + '  ' + '沒有每人訂金' + '\n')

        if '包含項目：' in res:
            index = res.index('包含項目：')
            if '：' not in res[index+1]: item['include_item'] = res[index+1]
        else:
            with open('error.txt','a+', encoding='utf-8') as f:
                f.write(str(item['GrupCd']) + '  ' + '沒有包含項目' + '\n')

        if '不含項目：' in res:
            index = res.index('不含項目：')
            if '不含項目：' not in res[-1]: item['not_include_item'] = res[index+1]
        else:
            with open('error.txt','a+', encoding='utf-8') as f:
                f.write(str(item['GrupCd']) + '  ' + '沒有不含項目' + '\n')

        yield item
