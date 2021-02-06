import scrapy
from scrapy import Request


class AllocineSpider(scrapy.Spider):
    name = 'allocinespi'
    start_urls = ['https://www.senscritique.com/liste/Films_de_Noel/386874#page-1/order-default/']

    def clean_spaces(self, string):
        if string:
            return " ".join(string.split())

    def scrap(self, response):

        for doc in response.css('.d-grid-main'):

            title_value = doc.css('.elli').css('li.elli-item').css('h3.d-heading2').css('a::text').extract()  
            #description_value = doc.css('.content-layout').css('.section-wrap').css('ul').css('li').css(".synopsis").css(".content-txt").extract()
            eval_spect = doc.css('.elli').css('li.elli-item').css('.erra-main').css('.erra-ratings').css('a.erra-global ::text').extract()
            image_urls = doc.css('.elli').css('li.elli-item').css('.elli-media').css('.d-link').css('.lazy ::attr(data-original)').extract()

            yield {
                'titre' : title_value,
                'Evaluation spectateur' : eval_spect,
                'image_urls' : image_urls
             }

        

    def parse(self, response):
        next_page_link = 'https://www.senscritique.com/liste/Films_de_Noel/386874#page-1/order-default/'
        yield scrapy.Request(url=next_page_link, callback=self.scrap)
        
