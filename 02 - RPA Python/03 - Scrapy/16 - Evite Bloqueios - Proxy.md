# Evite Bloqueios - Proxy


- Um proxy é um servidor que age como um intermediário entre o seu dispositivo e a internet.
- Pode rotear o tráfego da internet por meio de endereços IP diferentes.
- Ao ocultar o endereço IP original do spider, um proxy pode tornar mais difícil para os servidores alvo detectarem e bloquearem os acessos repetidos do spider.
- Alguns proxies permitem selecionar a localização do servidor intermediário, permitindo que o spider simule acessos de diferentes regiões geográficas, o que pode ajudar a evitar bloqueios baseados em localização.


### ScrapeOps


- Serviço de Proxy Pago
- Vamos utilizar a solução **Proxy Aggregator**.
- Obter o ``Account API Key``.
- Documentação [neste link](https://scrapeops.io/docs/proxy-aggregator/integration-examples/python-scrapy-example/).



### 


**Instalação:**
```
pip install scrapeops-scrapy-proxy-sdk
```


**configuração arquivo ``settings.py``:**
```python
# inserir abaixo da configuração do User-Agent

SCRAPEOPS_API_KEY = 'YOUR_API_KEY'

SCRAPEOPS_PROXY_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}
```