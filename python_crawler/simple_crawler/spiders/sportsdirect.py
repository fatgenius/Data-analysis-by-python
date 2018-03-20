#-*- coding: utf-8 -*-
import scrapy
from ..items import ProductItem #import from items


class SportsdirectSpider(scrapy.Spider):
    name = 'sportsdirect'
    allowed_domains = ['sportsdirect.com']
    start_urls = ['https://www.sportsdirect.com/mens/mens-rugby-boots']
  

    def parse(self, response):
    	products =response.css('.s-productthumbbox')#using css file select or response.xpath()
    	for p in products:
    		brand = p.css('.productcdescriptionbrand::text').extract_first()
    		productName =p.css('.productdescriptionname::text').extract_first()
    		price =  (p.css('.curprice::text').extract_first())
    		productUrl =p.css('a::attr(href)').extract_first()
    		#print(brand,productName,price) #test it
    		item=ProductItem() #create new iteam 
    		item['brand'] =brand #assign the attribute
    		item['name']  = productName
    		item['price'] = price
    		item['url'] =response.urljoin(productUrl)
    		yield item # return the generator
    		r = scrapy.Request(url =response.urljoin(productUrl),callback=self.parseProduct)
    		r.meta['item'] =item
    		yield r
    		#return 
    	nextPageLinkSelctor =response.css('.NextLink::attr("href")')
    	if nextPageLinkSelctor:
    		nextPageLink =nextPageLinkSelctor[0].extract()
    		yield scrapy.Request(url =response.urljoin(nextPageLink))


    def parseProduct(self,response):
    	item =response.meta['item']
    	imageUrl = response.css('a::attr(srczoom)').extract()
    	item['image_urls']=imageUrl
    	yield item
    	#print(imageUrl)