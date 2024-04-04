# Varrendo Página Única


### Extraindo Frases, Autores e Tags de uma Página:
```python
import scrapy

class QuotesToScrapeSpider(scrapy.Spider):
   
    name = 'frasebot'

    def start_requests(self):
        urls = ['https://quotes.toscrape.com/']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)    

    def parse(self, response):
        for elemento in response.xpath("//div[@class='quote']"):
            yield {
                'frase': elemento.xpath(".//span[@class='text']/text()").get(),
                'autor': elemento.xpath(".//small[@class='author']/text()").get(),
                'tags': elemento.xpath(".//a[@class='tag']/text()").getall()
            }
```