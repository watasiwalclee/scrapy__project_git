# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import urllib

class WnacgPipeline:

    def open_spider(self, spider):
        if not os.path.exists('figs'):
            os.mkdir('figs')
            os.chdir('figs')
        else:
            os.chdir('figs')
        print('='*40)

    def process_item(self, item, spider):
        if not os.path.exists(item['title']): os.mkdir(item['title'])
        # 遇到http 403，需要增加header才能跑
        opener = urllib.request.URLopener()
        opener.addheader('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36')
        opener.retrieve(item['fig'], os.path.join(item['title'],item['file_name']+'.jpg'))
        return item

    def close_spider(self, spider):
        print('='*40)