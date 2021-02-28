import scrapy

class BestsellerSpiderSpider(scrapy.Spider):
    name = 'bestseller_spider'
    start_urls = ['https://www.amazon.com/s?rh=n%3A21102321011&fs=true&ref=lp_21102321011_sar']

    def parse(self, response):
        pass