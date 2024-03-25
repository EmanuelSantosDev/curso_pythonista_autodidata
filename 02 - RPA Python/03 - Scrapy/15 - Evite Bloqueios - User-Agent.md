# Evite Bloqueios - User-Agent


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