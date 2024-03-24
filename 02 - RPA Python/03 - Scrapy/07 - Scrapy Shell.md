# Scrapy Shell


- O **Scrapy Shell** é uma ferramenta interativa que permite aos desenvolvedores testar e experimentar com expressões XPath e CSS Selectors.
- Verifica se os seletores estão selecionando os elementos desejados corretamente.
- Facilita o desenvolvimento e depuração de spiders no Scrapy.


## Iniciando a Sessão:
```
scrapy shell [url_do_site]
```


## Obtendo o Texto do Primeiro Ítem:
```
response.xpath("//span[@class='text']/text()").get()
```

Retorna o Primeiro Valor:
```
'“The world as we have created it is a process of our thinking. It cannot 
be changed without changing our thinking.”'
```


## Obtendo o Texto de Todos os Itens:
```
response.xpath("//small[@class='author']/text()").getall()
```

Retorna uma lista:
```
['Albert Einstein', 'J.K. Rowling', 'Albert Einstein', 'Jane Austen',
 'Marilyn Monroe', 'Albert Einstein', 'André Gide', 'Thomas A. Edison',
 'Eleanor Roosevelt', 'Steve Martin']
```

