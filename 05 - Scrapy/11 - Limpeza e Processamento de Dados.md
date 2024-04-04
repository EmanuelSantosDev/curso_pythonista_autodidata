# Limpeza e Processamento de Dados


- Como formatar um dado quando ele é retornado?
- O local do Scrapy onde fazemos estas configurações é o arquivo `items.py`.
- Ferramenta de consulta de caracteres especiais: [Unicode Code Converter](https://r12a.github.io/app-conversion/?_gl=1*2kjo17*_ga*OTAwMDE2OTc2LjE3MDg3NDMyNDM.*_ga_37GXT4VGQK*MTcxMDU5MzcyMy42OS4xLjE3MTA1OTU2MzUuMC4wLjA.).


## Arquivo spider.py

- O ``ItemLoader`` é uma classe do Scrapy que facilita a extração e o pré-processamento de dados de uma página da web.
- Após adicionar todas as informações ao ``ItemLoader``, o método ``load_item()`` é chamado para finalizar o preenchimento do item e retorná-lo.

```python
import scrapy
from scrapy.loader import ItemLoader
from varredor_de_sites.items import CitacaoItem


class ObterFrases(scrapy.Spider):

    name = 'peter_park'

    def start_requests(self):
        urls = ['https://www.goodreads.com/quotes']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for elemento in response.xpath("//div[@class='quote']"):
            loader = ItemLoader(item=CitacaoItem(),
                                selector=elemento,
                                response=response)
            loader.add_xpath('frase', ".//div[@class='quoteText']/text()")
            loader.add_xpath('autor', ".//span[@class='authorOrTitle']/text()")
            loader.add_xpath('tags', ".//div[@class='greyText smallText left']/a/text()")
            yield loader.load_item()
```


## Arquivo items.py


- ``scrapy.Item`` é uma classe base que você usa para definir seus próprios itens personalizados.
- ``scrapy.Field`` é usado dentro de uma classe ``scrapy.Item`` para definir os campos que serão extraídos.
- ``input_processor`` informa como que o dado que está entrando no processador será tratado. Podem existir campos que não precisam deste argumento, pois o dado já está vindo corretamente.
- ``output_processor`` informa como que o dado que está saindo do processador será exportado.
- ``MapCompose`` é um processador usado para aplicar uma função (ou uma lista de funções) a cada valor extraído de um campo.
- ``TakeFirst`` é um processador que seleciona o primeiro valor não nulo de uma lista de valores extraídos de um campo. É semelhante à utilização do `get()`.
- ``Join`` é um processador usado para juntar uma lista de valores em uma única string, separando-os por um delimitador específico.


```python
import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join


def tirar_espaco_em_branco(valor):
    return valor.strip()


def processar_caracteres_especiais(valor):
    return valor.replace(u'\u201c', '').replace(u'\u201d', '').replace(u'\u2014', '—')


class CitacaoItem(scrapy.Item):
    frase = scrapy.Field(
        input_processor=MapCompose(
            tirar_espaco_em_branco, processar_caracteres_especiais),
        output_processor=TakeFirst()
    )
    autor = scrapy.Field(
        input_processor=MapCompose(tirar_espaco_em_branco),
        output_processor=TakeFirst()
    )
    tags = scrapy.Field(
        output_processor=Join(',')
    )
```