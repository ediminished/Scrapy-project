import scrapy
from ..items import AmazonItem

def stripper(el):
    return el.strip()

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    page_number = 0
    start_urls = [
        'https://www.amazon.com/gp/bestsellers/books/173507/ref=s9_acsd_obs_hd_bw_bj8V_clnk/ref=s9_acsd_obs_hd_bw_bj8V_c2_x_c2cl?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-11&pf_rd_r=6ZYEMJY5VYNGCTHPWH58&pf_rd_t=101&pf_rd_p=97613fec-d659-51f0-8e66-f6794071e8cc&pf_rd_i=173507'
    ]

    def parse(self, response):
        items = AmazonItem()
        name_helper = map(stripper, response.css('#zg-ordered-list > li:nth-child(n) > span > div > span > a > div').css(
            '::text').extract())
        name = [item for item in  name_helper]
        author = response.css('.a-link-normal+ .a-size-small .a-size-small').css('::text').extract()
        cover = response.css('.a-spacing-small img').css('::attr(src)').extract()

        items['name'] = name
        items['author'] = author
        items['cover'] = cover

        self.page_number +=1
        print("Scraped page...", self.page_number)
        yield items

        next_page = response.css('.a-last a').css('::attr(href)').extract_first()

        if next_page:
            yield response.follow(next_page, callback=self.parse)