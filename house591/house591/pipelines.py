# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from house591 import items

class House591Pipeline:
    def open_spider(self, spider):
        conf = {
            'host':'',
            'port':'',
            'user':'',
            'passwd':'',
            'database':''
        }
        self.conn = pymysql.connect(**conf)
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        if not isinstance(item,items.House591Item):
            #print('='*20+'不符合屬性'+'='*20,type(item))
            return item
        # 確認是否有相同資料
        self.cur.execute("select * from houselist where hid=%s",(item['hid'],))
        row_count = self.cur.rowcount
        
        if row_count == 0: # 若無相同hid，則將資料寫入mysql
            cols = list(item)
            col_ctring = ','.join(cols)
            values = tuple([item[col] for col in cols])
            values_string = ','.join(['%s']*len(cols))
            sql_string = "insert into houselist ({}) values ({})".format(col_ctring,values_string)
            self.cur.execute(sql_string,values)
            self.conn.commit()
        else:  # 若有相同hid，則跳過
            print('='*10+'已有相同資料'+'='*10)

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

class HouseDetailPipeline:
    def open_spider(self, spider):
        conf = {
            'host':'192.168.0.102',
            'port':3307,
            'user':'lclee',
            'passwd':'secret10524',
            'database':'house591'
        }
        self.conn = pymysql.connect(**conf)
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        if not isinstance(item,items.HouseDetailItem):
            #print('='*10+'不符合屬性'+'='*10)
            return item
        
        self.cur.execute("select * from housedetail where hid=%s",(item['hid'],))
        row_count = self.cur.rowcount
        if row_count == 0:
            cols = list(item)
            values = tuple([item[key] for key in cols])
            cols_string = ','.join(cols)
            value_string = ','.join(['%s']*len(cols))
            sql_string = "insert into housedetail ({cols_string}) values ({value_string})".format(cols_string=cols_string,value_string=value_string)
            self.cur.execute(sql_string,values)
            self.conn.commit()
        else:
            print('='*20+'已有相同資料'+'='*20)

        return item
    
    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

