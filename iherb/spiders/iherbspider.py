import scrapy
import logging
from scrapy.spiders import Spider
from scrapy.selector import Selector
from iherb.items import IherbItem

class IherbSpider(Spider):
    name = "iherbspider"
    allowed_domains = ["iherb.cn"]
    max_page = 5
    cur_page = 1
    
    start_urls = [
        "http://www.iherb.cn/Supplements?oos=true&disc=false&p=1"
                  ]
    
    def parse(self, response):
        brands = response.xpath("//article[div[span[@itemprop='price']]]/a[1]/@title").extract()
        desc = response.xpath("//article[div[span[@itemprop='price']]]/a[1]/@title").extract()
        urls = response.xpath("//article[div[span[@itemprop='price']]]/a[1]/@href").extract()
        prices = response.xpath("//span[@itemprop='price']/@content").extract()
        
        items = []
        length = len(brands)
        for it in range(length):
            item = IherbItem()
            item['url'] = urls[it]
            item['brand'] = brands[it].split(',')[0]
            item['desc'] = brands[it].split(',')[1]
            item['price'] = prices[it][1:]
            #items.append(item)
            yield item
        
        if(self.cur_page <= 431):
            self.cur_page += 1
            self.logger.info("cur_page*********************************** %s", self.cur_page)
            yield scrapy.Request("http://www.iherb.cn/Supplements?oos=true&disc=false&p="+str(self.cur_page), self.parse) 
        
            