import scrapy
#from items import alloItem
from scrapy import Request

class AllocineSpider(scrapy.Spider):
    name = 'allocinespi'
    #allowed_domains = ['allocine.fr']
    start_urls = ['https://www.allocine.fr/recherche/movie/?q=no%C3%ABl']


    def parse(self, response):

        for doc in response.xpath('//div[@class="sub-body"]'):
          #  description_value = doc.css("div .synopsis ::text").extract()
            title_value = doc.css(".entity-card .meta-title ::text").extract()

            eval_spect = doc.css("div.rating-item-content div.stareval.stareval-medium.stareval-theme-default span.stareval-note")

            #raw_image_urls = doc.css(".entity-card .thubnail ::attr(scr)").getall()
            #raw_image_urls = doc.css("img::attr(xXx thumbnail-container thumbnail-link)").extract_first()

            #clean_image_urls = []
            #for image_url in raw_image_urls:
                #clean_image_urls.append(doc.urljoin(image_url))

            yield {#'description' : description_value,
            'titre' : title_value,
            #'image_urls' : clean_image_urls,
            'Evaluation spectateur' : eval_spect 
            }

        for i in range (1,35):
            next_page_link = 'https://www.allocine.fr/recherche/movie/?q=no%C3%ABl&page='+str(i)
            yield scrapy.Request(url=next_page_link, callback=self.parse)



def clean_spaces(self, string):
    if string:
        return " ".join(string.split())
