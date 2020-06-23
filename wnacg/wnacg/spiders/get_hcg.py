# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GetHcgSpider(CrawlSpider):
    name = 'get_hcg'
    allowed_domains = ['www.wnacg.org']
    start_urls = ['https://www.wnacg.org/albums.html']

    rules = (
        Rule(LinkExtractor(allow=r'albums-index-page-[1-3].html'), follow=True),
        Rule(LinkExtractor(allow=r'photos-index-aid-\d+.html'), follow=True),
        Rule(LinkExtractor(allow=r'photos-index-page-\d+-aid-\d+.html'), follow=True),
        Rule(LinkExtractor(allow=r'photos-view-id-\d+.html'), callback='get_fig', follow=False),
    )

    # def get_info(self, response):
    #     title = response.xpath("//div[@id='bodywrap']/h2/text()").get()
    #     intro = response.xpath("//div[@class='asTBcell uwconn']/p/text()").getall()
    #     print(title,intro)

    def get_fig(self, response):
        item = {}
        title = response.xpath("//div[@class='png bread']//a/text()").getall()[-1]
        file_name = response.xpath("//div[@class='png bread']/text()").getall()[-1].strip()
        fig = response.xpath("//img[@id='picarea']/@src").get()
        item['title'] = title
        item['file_name'] = file_name
        item['fig'] = response.urljoin(fig)
        yield item

        # figs = response.xpath("//ul[@class='cc']//li/div[@class='pic_box tb']/a/img/@src").getall()

