# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class alloItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    description = scrapy.Field()
    image_urls = scrapy.Field()

allo_item = alloItem(title="Aled", description="C'est pas tres drole ca", image_urls='https://fr.web.img5.acsta.net/r_1920_1080/pictures/20/10/02/12/08/4145841.jpg')
