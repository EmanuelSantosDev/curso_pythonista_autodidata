# Conceituação Teórica


### O que é Web Scraping?
- Raspagem da Web
- Processo de "varrer" sites para obter dados


### Como isso pode ser feito?
- Selenium
- Scrapy
- BeautifulSoup
- Outros...


### O que é um Scraper/Crawler/Spider?
- Programa criado para varrer um determinado site
- Todos os termos estão falando da mesma coisa
- São basicamente bots


### O que pode ser varrido de um site?
- Texto
- Imagens
- Videos
- E-mails
- Telefones
- Endereços
- Links
- Basicamente qualquer coisa que está disponível dentro do código HTML


### Como posso varrer um site?
- Navegue até um site usando o Scrapy
- Determine o que quer extrair dentro do HTML
- Crie um código que extrai apenas o que é do seu interesse (usando XPATH ou Seletores CSS)
- Salve os dados


### Scrapy só varre sites?
- Sites
- Sitemaps
- CSV
- XML
- HTML


### Scrapy x BeautifulSoup
**BeautifulSoup**:
- Limitado a parte de extração de dados

**Scrapy**:
- Busca
- Processa
- Exporta


# Arquivo ``robots.txt``


- É um arquivo de texto usado para controlar o comportamento de rastreamento de bots de mecanismos de busca e outros crawlers da web.
- Localizado na raiz de um site (``https://www.globo.com/robots.txt``).
- Usado para instruir os bots sobre quais páginas podem ser acessadas e quais devem ser evitadas.
- Pode conter diretivas como "User-agent" para especificar quais bots são afetados e "Disallow" para indicar quais partes do site não devem ser rastreadas.
- Ajuda a evitar que bots acessem áreas sensíveis do site, reduzindo a carga do servidor e protegendo informações confidenciais.


**Exemplo**:
```txt
User-Agent: *
Disallow: /busca/
Disallow: /beta/
Disallow: /historico-home/
Disallow: *globo-cdn-src/*
Disallow: /alt-a/
Disallow: /alt-b/
Disallow: /alt-c/
Disallow: /alt-d/
Disallow: /recomendado/
Disallow: /explore/
Sitemap: http://www.globo.com/sitemap-image.xml

User-agent: CCBot
Disallow: /

User-agent: GPTBot
Disallow: /

User-agent: Google-Extended
Disallow: /
```