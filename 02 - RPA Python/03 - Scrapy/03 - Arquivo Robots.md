# Arquivo Robots


O que é um arquivo ``robots.txt``?
- Um arquivo de texto usado para controlar o comportamento de rastreamento de bots de mecanismos de busca e outros crawlers da web.
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