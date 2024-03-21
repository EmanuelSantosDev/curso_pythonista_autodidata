# Clonando uma Página HTML


### Os Spiders são criados no diretório `/spiders`:
```python
import scrapy


class QuotesToScrapeSpider(scrapy.Spider):

    # Identidade
    name = 'frasebot'

    # Request
    def start_requests(self):
        urls = ['https://quotes.toscrape.com/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Response
    def parse(self, response):
        with open('pagina.html', 'wb') as arquivo:
            arquivo.write(response.body)
```


### Rodando o Scrapy:
```
cd <diretorio_do_projeto>
scrapy crawl <nome_do_bot>
```