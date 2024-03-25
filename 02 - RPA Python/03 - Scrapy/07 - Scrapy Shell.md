# Scrapy Shell


- O **Scrapy Shell** é uma ferramenta que permite aos desenvolvedores testar e experimentar _Expressões XPath_ e _CSS Selectors_ via terminal.
- Facilita o desenvolvimento e depuração de spiders no Scrapy.


## Iniciando a Sessão:
```
scrapy shell [url_do_site]
```


## Testando um Ítem:
Ou o primeiro ítem se for retornada uma lista de itens.
```
response.xpath("//span[@class='text']/text()").get()
```


## Testando uma Lista de Itens:
Retornando uma lista.
```
response.xpath("//small[@class='author']/text()").getall()
```