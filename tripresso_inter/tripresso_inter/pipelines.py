# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from tripresso_inter import items

# 新魅力旅遊網清單pipeline
class NewAmazingPipeline:
    def open_spider(self, spider):
        info = {
            'host':'192.168.0.102',
            'port':3307,
            'user':'',
            'passwd':'',
            'database':''
        }
        self.conn = pymysql.connect(**info)
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        # 判斷是否為NewAmazingItem，若不是則跳過該pipeline。
        if isinstance(item, items.NewAmazingItem):
            # 查詢資料庫中相同ID的資料
            count = self.cur.execute("select * from GroupList where GrupCd='{}'".format(item['GrupCd']))
            if count == 0:  # 如果不存在相同ID，則將資料寫入MySql
                column_string = ','.join(list(item))
                values = tuple([item[key] for key in item])
                value_string = ','.join(['%s']*len(values))
                insert_string = "insert into GroupList({}) values ({})".format(column_string,value_string)
                self.cur.execute(insert_string, values)
                self.conn.commit()
                return item
            else:  # 如果已存在相同ID，則不進行任何動作將item
                print('='*20+" 已有相同資料 "+'='*20)
                return item
        else:
            return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

# 世邦旅行社清單pipeline
class ShiPangPipeline:
    def open_spider(self, spider):
        info = {
            'host':'192.168.0.102',
            'port':3307,
            'user':'',
            'passwd':'',
            'database':''
        }
        self.conn = pymysql.connect(**info)
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        # 判斷是否為ShiPangItem，若不是則跳過該pipeline。
        if isinstance(item, items.ShiPangItem):
            # 查詢資料庫中相同ID的資料
            count = self.cur.execute("select * from GroupList where GrupCd='{}'".format(item['GrupCd']))
            if count == 0:  # 如果不存在相同ID，則將資料寫入MySql
                column_string = ','.join(list(item))
                values = tuple([item[key] for key in item])
                value_string = ','.join(['%s']*len(values))
                insert_string = "insert into GroupList({}) values ({})".format(column_string,value_string)
                self.cur.execute(insert_string, values)
                self.conn.commit()
                return item
            else:  # 如果已存在相同ID，則不進行任何動作將item
                print('='*20+" 已有相同資料 "+'='*20)
                return item
        else:
            return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

#新魅力旅遊網詳細資料
class NewAmazingDetailPipeline:
    def open_spider(self, spider):
        info = {
            'host':'192.168.0.102',
            'port':3307,
            'user':'',
            'passwd':'',
            'database':''
        }
        self.conn = pymysql.connect(**info)
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        # 判斷是否為ShiPangItem，若不是則跳過該pipeline。
        if isinstance(item, items.NewAmazingDetailItem):
            # 查詢資料庫中相同ID的資料
            count = self.cur.execute("select * from Detail where GrupCd='{}'".format(item['GrupCd']))
            if count == 0:  # 如果不存在相同ID，則將資料寫入MySql
                column_string = ','.join(list(item))
                values = tuple([item[key] for key in item])
                value_string = ','.join(['%s']*len(values))
                insert_string = "insert into Detail({}) values ({})".format(column_string,value_string)
                self.cur.execute(insert_string, values)
                self.conn.commit()
                return item
            else:  # 如果已存在相同ID，則不進行任何動作將item
                print('='*20+" 已有相同資料 "+'='*20)
                return item
        else:
            return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

#世邦旅行社詳細資料
class ShiPangDetailPipeline:
    def open_spider(self, spider):
        info = {
            'host':'192.168.0.102',
            'port':3307,
            'user':'',
            'passwd':'',
            'database':''
        }
        self.conn = pymysql.connect(**info)
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        # 判斷是否為ShiPangItem，若不是則跳過該pipeline。
        if isinstance(item, items.ShiPangDetailItem):
            # 查詢資料庫中相同ID的資料
            count = self.cur.execute("select * from Detail where GrupCd='{}'".format(item['GrupCd']))
            if count == 0:  # 如果不存在相同ID，則將資料寫入MySql
                column_string = ','.join(list(item))
                values = tuple([item[key] for key in item])
                value_string = ','.join(['%s']*len(values))
                insert_string = "insert into Detail({}) values ({})".format(column_string,value_string)
                self.cur.execute(insert_string, values)
                self.conn.commit()
                return item
            else:  # 如果已存在相同ID，則不進行任何動作將item
                print('='*20+" 已有相同資料 "+'='*20)
                return item
        else:
            return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()