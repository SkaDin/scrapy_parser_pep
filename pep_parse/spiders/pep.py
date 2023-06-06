import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_links = response.xpath('//a[@class="pep reference internal"]/@href')
        for pep_link in range(1, len(pep_links) - 2, 2):
            yield response.follow(pep_links[pep_link], callback=self.parse_pep)

    def parse_pep(self, response):
        pep_title = response.xpath('//h1[@class="page-title"]/text()').get()
        status_pep = response.css(
            'dt:contains("Status") + dd abbr::text'
        ).get()
        pep_num = pep_title.split(' ')[1]
        name = pep_title.split(' – ')[1]
        data = {
            'number': pep_num,
            'name': name,
            'status': status_pep

        }
        yield PepParseItem(data)