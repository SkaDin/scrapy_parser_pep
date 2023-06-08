import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """Класс 'пaука'."""

    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/', ]

    def parse(self, response):
        """Метод, загружающий и обрабатывающий ссылки на PEP."""
        pep_links = response.xpath(
            '//table//tbody//a[@class="pep reference internal"]/@href'
        )
        for pep_link in pep_links:
            url = response.urljoin(pep_link.get())
            if not url.endswith('/'):
                url += '/'
            yield response.follow(
                pep_link,
                callback=self.parse_pep
            )

    def parse_pep(self, response):
        """Метод парсинга содержимого ссылок."""
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
