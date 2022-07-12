from cmath import nan
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "spinneys"
    start_urls = [
        'https://www.spinneyslebanon.com/'
    ]

    def parse(self, response):
        urls = response.css(".view-all::attr(href)").getall()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_category)
    def parse_category(self, response):
        urls = response.css(".product-item-info").css("::attr(href)").re(".*.html")
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_product)
    def parse_product(self, response):
        yield {
                'product_url': response.url,
                'product_name': response.css(".base::text").get(),
                'product_price':  response.css(".price::text").get(),
                'product_details': response.css('.value::text').get(),
                'product_image': response.css(".imgzoom::attr(data-zoom)").get() 
            }
        
