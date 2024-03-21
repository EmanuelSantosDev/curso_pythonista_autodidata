# Evite Bloqueio - Robots.txt


- A variável ``ROBOTSTXT_OBEY`` é uma configuração que determina se o spider do Scrapy deve obedecer as regras do arquivo ``robots.txt`` dos sites que ele acessa. 
- Por padrão, essa configuração é definida como ``True`` para garantir um comportamento ético e respeitoso com os sites que estão sendo rastreados.
- No entanto, em certos casos, você pode querer desativar essa configuração, especialmente se estiver ciente das políticas do site e deseja ignorar o arquivo ``robots.txt``.


**No arquivo ``settings.py``:**
```python
ROBOTSTXT_OBEY = False
```