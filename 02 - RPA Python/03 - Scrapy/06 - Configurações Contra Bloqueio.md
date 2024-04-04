# Configurando o ``robots.txt``


- A variável ``ROBOTSTXT_OBEY`` é uma configuração que determina se o spider do Scrapy deve obedecer as regras do arquivo ``robots.txt`` dos sites que ele acessa. 
- Por padrão, essa configuração é definida como ``True`` para garantir um comportamento ético e respeitoso com os sites que estão sendo rastreados.
- No entanto, em certos casos, você pode querer desativar essa configuração, especialmente se estiver ciente das políticas do site e deseja ignorar o arquivo ``robots.txt``.


**No arquivo ``settings.py``:**
```python
ROBOTSTXT_OBEY = False
```


# Delay de Download


- A variável ``DOWNLOAD_DELAY`` é uma configuração que determina o atraso (em segundos) entre as requisições sucessivas feitas pelo spider durante o scraping.
- Esse atraso é útil para evitar sobrecarregar o servidor alvo com muitas requisições em um curto período de tempo, o que pode ser interpretado como comportamento malicioso.


**No arquivo ``settings.py``:**
```python
DOWNLOAD_DELAY = 3
```


# User-Agent


- Um **user-agent** é uma string de identificação enviada por um cliente (como um navegador da web) a um servidor web durante uma solicitação HTTP.
- Ele fornece informações sobre o cliente, como o tipo de navegador, o sistema operacional, a versão do software, entre outros detalhes.
- O servidor web usa essas informações para fornecer conteúdo otimizado ou adaptado para o cliente, além de rastrear o tráfego e realizar análises.
- Por padrão o Scrapy não define um navegador padrão, como Chrome, Firefox e Edge.
- O Scrapy possui um navegador próprio, que pode ser detectado como um bot.


### Como verificar o User-Agent no Browser:
1. Aba Network
1. Name (da requisição)
1. Headers
1. Rolar até o final
1. User-Agent


### Gerando Fake User-Agents


- A biblioteca ``scrapy-fake-useragent`` proporciona uma maneira simples de configurar e utilizar user-agents aleatórios em suas solicitações para evitar a detecção e o bloqueio por parte dos servidores web.
- A biblioteca fornece um _**middleware**_ que pode ser facilmente adicionado à configuração do Scrapy.
- No contexto do Scrapy, um _**middleware**_ é um componente que intercepta as solicitações HTTP feitas pelo Scrapy e pode modificar ou adicionar funcionalidades a elas antes de serem enviadas para o servidor.


**Instalação:**
```
pip install scrapy-fake-useragent
```


**configuração arquivo ``settings.py``:**
```python
# inserir logo depois de DOWNLOAD_DELAY = 3

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
}

FAKEUSERAGENT_PROVIDERS = [
     # This is the first provider we'll try
    'scrapy_fake_useragent.providers.FakeUserAgentProvider',  
    # If FakeUserAgentProvider fails, we'll use faker to generate a user-agent string for us
    'scrapy_fake_useragent.providers.FakerProvider', 
    # Fall back to USER_AGENT value 
    'scrapy_fake_useragent.providers.FixedUserAgentProvider',  
]

## Set Fallback User-Agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
```


# Proxy


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