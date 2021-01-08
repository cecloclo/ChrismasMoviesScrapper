#import scrapy
#from scrapy import Request

#class AlloSpider(scrapy.Spider):
#    name = "Films de noël"
  #  start_urls = ['https://www.allocine.fr/recherche/movie/?q=no%C3%ABl',]

    #def parse(self, response):
   #     for cit in response.xpath('.html > head.description > countent"noël'):
  #          title_value = cit.xpath('.title::text').extract()
 #           description_value = cit.xpath('.description::text').extract()
 #           image = cit.xpath('.html > head > link.shortcut_icon & .image > x-icon').extract()
 #           all_links = title_value + description_value + image
#            yield { 'document' : all_links}
       # for link in all_links.values():

import scrapy

class AlloSpider(scrapy.Spider):
    name = "Filmsdenoel"
    start_urls = ["https://www.allocine.fr/recherche/movie/?q=no%C3%ABl",]

    def parse(self, response):
        for cit in response.xpath('//a[@class="xXx meta-title-link"]'):
            text_value = cit.xpath('a/text()').extract_first()
            yield { 'text' : text_value }