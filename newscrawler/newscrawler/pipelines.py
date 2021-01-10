# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class NewscrawlerPipeline:
    def process_item(self, item, spider):
        if item['title']:
            item["title"] = clean_spaces(item["title"])
            return item
     #   else:
        #    raise ItemAdapter("Missing title in %s" % item)


def clean_spaces(string):
    if string:
        return " ".join(string.split())