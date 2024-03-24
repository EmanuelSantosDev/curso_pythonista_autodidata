# Varrendo Múltiplas Páginas


### Extraindo Frases, Autores e Tags de Múltiplas Páginas:
```python
import scrapy


class QuotesToReadSpider(scrapy.Spider):
   
    name = 'citacao'

    def start_requests(self):
        urls = ['https://quotes.toscrape.com/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                'frase': quote.xpath('.//span[@class="text"]/text()').get(),
                'autor': quote.xpath('.//small[@class="author"]/text()').get(),
                'tags': quote.xpath('.//div[@class="tags"]/a/text()').getall()
            }
        try:
            href_proxima_pagina = response.xpath("//li[@class='next']/a/@href").get()
            if href_proxima_pagina is not None:
                url_proxima_pagina = response.urljoin(href_proxima_pagina)
                yield scrapy.Request(url=url_proxima_pagina, callback=self.parse)
        except:
            print('Chegamos na última página')
```