# Executando o Scrapy a partir de um Script


- Você pode executar o Scrapy a partir de um script, em vez da maneira típica de executar o Scrapy via ``scrapy crawl``.
- ``CrawlerProcess`` é uma classe usada para criar e executar instâncias de crawlers.
- É uma maneira conveniente de iniciar e controlar a execução de um ou mais spiders Scrapy em um único processo.
- Com ela podemos executar uma spider sem precisar criar um projeto completo do scrapy.
- Permite também executar spiders em outros módulos e scripts do Python.


## Rodando o Scrapy sem Toda a Estrutura do Framework
```python
import scrapy
# importando CrawlerProcess
from scrapy.crawler import CrawlerProcess


class ProxyListSpider(scrapy.Spider):

    name = 'proxylist'

    def start_requests(self):
        urls = ['https://free-proxy-list.net/web-proxy.html']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        contador = 1
        for linha in response.xpath("//table[@class='table table-striped table-bordered']/tbody/tr"):
            yield {
                'Seq': contador,
                'Proxy Name': linha.xpath("./td[1]/a/text()").get(),
                'Domain': linha.xpath("./td[2]/text()").get(),
                'Country': linha.xpath("./td[3]/text()").get(),
                'Speed': linha.xpath("./td[4]/text()").get(),
                'Anonymity': linha.xpath("./td[5]/div/div[@class='progress-bar']/text()").get(),
            }
            contador += 1


# Criando um processo do Scrapy com configurações especificadas
bot = CrawlerProcess(
    settings={
        "FEEDS": {
            "itens.csv": {"format": "csv"},
            "itens.json": {"format": "json"}
        }
    }
)

# Configurando o spider que será executado
bot.crawl(ProxyListSpider)
# Inicia o processo do Crawler
bot.start()
```


## Rodando em Outro Arquivo Python


```python
from app import ProxyListSpider, CrawlerProcess

resposta = input('Devo iniciar a automação? (s/n)')

if resposta == 's':
   bot = CrawlerProcess(
      settings={
            "FEEDS": {
            "livros.json": {"format":"csv"}
         }
      }
   )
   bot.crawl(QuotesToScrapeSpider)
   bot.start()
else:
   print('Não será iniciado a automação')
```