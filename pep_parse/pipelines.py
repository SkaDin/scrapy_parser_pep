# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import datetime as dt


class PepParsePipeline:

    def open_spider(self, spider):
        now = dt.datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
        self.file = open(f'results/status_summary_{now}.csv', 'w', encoding='utf-8', newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['Статус', 'Количество'])
        self.status_count = {
            'Active': 0,
            'Accepted': 0,
            'Deferred': 0,
            'Final': 0,
            'Provisional': 0,
            'Rejected': 0,
            'Superseded': 0,
            'Withdrawn': 0,
            'Draft': 0
        }
        self.total_count = 0

    def process_item(self, item, spider):
        if 'status' in item:
            status = item['status']
            if status in self.status_count:
                self.status_count[status] += 1
                self.total_count += 1
        return item

    def close_spider(self, spider):
        for status, count in self.status_count.items():
            self.writer.writerow([status, count])
        self.writer.writerow(['Total', self.total_count])
        self.file.close()
