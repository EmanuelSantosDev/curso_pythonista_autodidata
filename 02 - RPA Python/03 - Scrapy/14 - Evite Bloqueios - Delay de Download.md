# 14 - Evite Bloqueio - Delay de Download


- A variável ``DOWNLOAD_DELAY`` é uma configuração que determina o atraso (em segundos) entre as requisições sucessivas feitas pelo spider durante o scraping.
- Esse atraso é útil para evitar sobrecarregar o servidor alvo com muitas requisições em um curto período de tempo, o que pode ser interpretado como comportamento malicioso.


**No arquivo ``settings.py``:**
```python
DOWNLOAD_DELAY = 3
```