import scrapy
#from items import alloItem
from scrapy import Request

class AllocineSpider(scrapy.Spider):
    name = 'allocine'
    #allowed_domains = ['allocine.fr']
    #start_urls = ['https://www.allocine.fr/recherche/?q=no%C3%ABl']
    start_urls = ['https://www.allocine.fr/recherche/movie/?q=no%C3%ABl']


    def parse(self, response):
        for doc in response.xpath('//div[@class="sub-body"]'):
          #  description_value = doc.css("div .synopsis ::text").extract()
           # title_value = doc.css(".entity-card .meta-title ::text").extract()
            image = doc.css("img .thumbnail-img b-loaded ::atr(scr)").getall()
            clean_image_urls = []
            for image_url in image:
                clean_image_urls.append(doc.urljoin(image_url))
            yield { #'description' : description_value,
         #   'titre' : title_value,
            'affiche' : image }
        for i in range (1,35):
            next_page_link = 'https://www.allocine.fr/recherche/movie/?q=no%C3%ABl&page='+str(i)
            yield scrapy.Request(url=next_page_link, callback=self.parse)


"""    def parse_category(self, response):
        for article in response.css("div .sub-body"):
            title = article.css("a .xXx meta-title-link").extract_first()
          #  image = article.css("img::attr(data-src)").extract_first()
            description = article.css("div .content-txt").extract_first()"""

"""   yield alloItem(
                title=title,
              #  image=image,
                description=description
            )
"""



       # next_page = response.xpath("//nav[@class='pagination cf']/a[@class='xXx button button-md button-primary-full button-right']/[@href='/recherche/movie/?q=no%C3%ABl&page=2'").extract_first()
        #next_page = response.xpath("//nav[@class='pagination cf']//a/@href").extract()      
       # if next_page is not None:
           # next_page_link = response.urljoin(next_page)

def clean_spaces(self, string):
    if string:
        return " ".join(string.split())
