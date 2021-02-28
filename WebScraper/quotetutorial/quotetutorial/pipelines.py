# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# scraped data -> Item containers -> json/csv files
# scraped data -> Item containers -> Pipeline -> SQL/Mongo
import pymongo
class QuotetutorialPipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['myquotes']
        self.collection = db['quotes_tb']

    def process_item(self, item, spider):
        # print("Pipeline: ", item["title"])
        self.collection.insert(dict(item))
        return item
