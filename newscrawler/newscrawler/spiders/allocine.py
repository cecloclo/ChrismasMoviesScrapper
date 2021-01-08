import scrapy

class AllocineSpider(scrapy.Spider):
    name = 'allocine'
    allowed_domains = ['https://www.allocine.fr/recherche/movie/?q=no%C3%ABl']
    start_urls = ['http://https://www.allocine.fr/recherche/movie/?q=no%C3%ABl/']

    def parse(self, response):
        title = response.css('title::text').extract_first()
        all_links = {
            name:response.urljoin(url) for name, url in zip(
            response.css("a.class=xXx meta-title-link")[3].css("a::text").extract(),
            response.css("a.class=xXx meta-title-link")[3].css("a::attr(href)").extract())
        }
        yield {
            "title":title,
            "all_links":all_links
        }
