# Exportando para JSON, XML e CSV


- ``-O`` para sobrescrever arquivos existentes
- ``-o`` para acrescentar dados a arquivos existentes(não funciona com json)


```
scrapy crawl nomebot -O dados.csv
scrapy crawl nomebot -O dados.xml
scrapy crawl nomebot -O dados.json
```