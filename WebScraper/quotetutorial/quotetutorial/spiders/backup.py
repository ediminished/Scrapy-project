# def akshay(response):
#         items = QuotetutorialItem()
#
#         all_div_quotes = response.css("div.quote")
#         for quotes in all_div_quotes:
#             title = quotes.css('.text::text').extract()
#             author = quotes.css('.author::text').extract()
#             tag = quotes.css('.tag::text').extract()
#
#             items['title'] = title
#             items['author'] = author
#             items['tag'] = tag
#
#             yield items
#
#         # next_page = response.css('li.next a::attr(href)').get()
#         # print(next_page)
#         # if next_page is not None:
#         #     yield response.follow(next_page, callback=self.parse)
#
#         next_page = 'https://quotes.toscrape.com/page/'+str(QuoteSpider.page_number)+'/'
#         while QuoteSpider.page_number<11:
#             yield response.follow(next_page, callback=self.parse)
#             QuoteSpider.page_number += 1