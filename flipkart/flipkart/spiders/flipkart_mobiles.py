# -*- coding: utf-8 -*-
import scrapy

class FlipkartMobilesSpider(scrapy.Spider):
    name = 'flipkart_mobiles'
    allowed_domains = ['https://www.flipkart.com/']
    start_urls = ['https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off','https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=2']
   
    def parse(self, response):
        mobile_name =  response.css('._3wU53n::text').getall()
        features = response.css('.vFw0gD .tVe95H::text').getall()
        price = response.css('._1vC4OE::text').getall()
        offer = response.css('.VGWI6T span::text').getall()
        filpkart = zip(mobile_name,features,price,offer)
        for item in filpkart:
            scraped_data = {
                'mobile_name' : item[0],  
                'features' : item[1],
                'price' : item[2],
                'offer':item[3]
            }
            yield scraped_data

