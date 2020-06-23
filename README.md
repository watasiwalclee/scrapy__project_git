# scrapy_project

專案名稱house591為爬取全台591房屋交易新建案的資料
目標網站為https://newhouse.591.com.tw/housing-list.html
補充:
網站傳送數據方式為以json傳輸，故對請求的網址傳送相關參數即可得到相對應資訊
爬蟲範圍為列表資訊以及每個建案的詳細內容並儲存至MySql
同時也擔心短時間內請求數量過多，故在middleware上設置proxy

!! 以下專案請慎入
專案名稱wnacg為爬取漫畫專案
目標網站為https://www.wnacg.org/albums.html
補充:
由於該網站下一頁網址從reponse中就能獲得，故採crawlspider的方式進行爬蟲。
下載完儲存在figs資料夾中