import scrapy
from ..items import alloItem

class AllocineSpider(scrapy.Spider):
    name = 'allocine'
    allowed_domains = ['allocine.fr']
    start_urls = ['https://www.allocine.fr/recherche/?q=no%C3%ABl']

    def parse(self, response):
        title = response.css('.titlebar-title titlebar-title-lg').extract_first()
       # all_links = {
        #    name:response.urljoin(url) for name, url in zip(
         #   response.css("a.class=xXx meta-title-link")[3].css("a::text").extract(),
          #  response.css("a.class=xXx meta-title-link")[3].css("a::attr(href)").extract())
     #   }
        yield {
            "title":title#,
          #  "all_links":all_links
        }


    def parse_category(self, response):
        for article in response.css(".fleuve")[0].css("article"):
            title = self.clean_spaces(article.css("h3 a::text").extract_first())
            image = article.css("img::attr(data-src)").extract_first()
            description = article.css(".txt3::text").extract_first()

            yield alloItem(
                title=title,
                image=image,
                description=description
            )


    def clean_spaces(self, string):
        if string:
            return " ".join(string.split())