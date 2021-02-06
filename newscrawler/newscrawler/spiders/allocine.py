import scrapy
from scrapy import Request

class AllocineSpider(scrapy.Spider):
    name = 'allocinespi'
    start_urls = ['https://www.allocine.fr/recherche/movie/?q=no%C3%ABl']

    def clean_spaces(self, string):
        if string:
            return " ".join(string.split())


    def parse(self, response):

        for doc in response.xpath('//div[@class="sub-body"]'):
            description_value = doc.css("div .synopsis ::text").extract()
            title_value = doc.css(".entity-card .meta-title ::text").extract()
            eval_spect = doc.css("span.stareval-note ::text").extract()
            image_urls = doc.css('.thumbnail img::attr(data-src)').getall()
        

            yield {'description' : description_value,
            'titre' : title_value,
            'image_urls' : image_urls,
            'Evaluation spectateur' : eval_spect 
            }

        """for i in range (1,35):
            next_page_link = 'https://www.allocine.fr/recherche/movie/?q=no%C3%ABl&page='+str(i)
            yield scrapy.Request(url=next_page_link, callback=self.parse)"""
