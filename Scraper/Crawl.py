from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
<<<<<<< HEAD
#from newcrawler.newcrawler.spiders import applescrap
=======
import Allospider
>>>>>>> a5d6b7d0b320e73418873c68f85cf33ca1052633
import os


class Scraper:
    def __init__(self):
        settings_file_path = 'newcrawler.newcrawler.settings'
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
        self.settings = get_project_settings()
        self.process = CrawlerProcess(self.settings)
<<<<<<< HEAD
       # self.spider = applescrap.AlloSpider 
=======
        #self.spider = AlloSpider 
>>>>>>> a5d6b7d0b320e73418873c68f85cf33ca1052633

    def run_spider(self):
        #self.process.crawl(self.spider)
        self.process.start()  # le script se bloque ici jusqu'a la fin