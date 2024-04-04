# Clonando uma Página HTML


- As _spiders_ são criados no diretório `/spiders`.
- Para rodar uma _spider_ é necessário primeiro entrar no diretório do projeto.
- O comando `yield` é equivalente ao `return`. Porém, quando uma função atinge uma instrução ``yield``, ela retorna temporariamente o valor especificado e suspende sua execução, mantendo seu estado interno. Quando a função é chamada novamente, ela retoma a execução a partir do ponto onde foi suspensa.
- Abrir um arquivo no modo binário (``wb``) é necessário quando você está lidando com tipos de dados que não são estritamente texto, como imagens, áudio, vídeo, entre outros, o que é importante para preservar a integridade dos dados.


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