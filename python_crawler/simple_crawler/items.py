import scrapy


class ProductItem(scrapy.Item):

    # define the fields 
    brand = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    image_urls= scrapy.Field()
