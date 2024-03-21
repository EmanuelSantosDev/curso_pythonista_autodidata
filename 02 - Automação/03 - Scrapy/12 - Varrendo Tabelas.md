# Varrendo Tabelas


```python
import scrapy


class ProxyScraperSpier(scrapy.Spider):

    name = 'proxyscraper'

    def start_requests(self):
        urls = ['https://us-proxy.org/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        contador = 1
        # Passo 1 - montar um XPATH que retorna cada uma das linhas da tabela
        for linha in response.xpath("//table[@class='table table-striped table-bordered']/tbody/tr"):
            yield {
                # Passo 2 - montar um XPATH que retorna cada uma das células da linha
                'Seq': contador,
                'IP Address': linha.xpath("./td[1]/text()").get(),
                'Port': linha.xpath("./td[2]/text()").get(),
                'Code': linha.xpath("./td[3]/text()").get(),
                'Country': linha.xpath("./td[4]/text()").get(),
                'Anonymity': linha.xpath("./td[5]/text()").get(),
                'Google': linha.xpath("./td[6]/text()").get(),
                'HTTPS': linha.xpath("./td[7]/text()").get(),
                'Last Checked': linha.xpath("./td[8]/text()").get()
            }
            contador += 1
```