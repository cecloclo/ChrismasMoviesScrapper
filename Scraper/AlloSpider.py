import scrapy

class AlloSpider(scrapy.Spider):
    name = "Films de noël"
    start_urls = ['https://www.allocine.fr/recherche/movie/?q=no%C3%ABl',]

    def parse(self, response):
        for cit in response.xpath('//div[@class="figsco__quote__text"]'):
            text_value = cit.xpath('a/text()').extract_first()
            yield { 'text' : text_value }