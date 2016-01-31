from scrapy.spiders import Spider
from scrapy.selector import Selector
from iherb.items import IherbItem

class IherbSpider(Spider):
    name = "iherb"
    allowed_domains = ["iherb.cn"]
    
    start_urls = [
        "http://www.iherb.cn/Supplements#p=1"
                  ]
    
    def parse(self, response):
        