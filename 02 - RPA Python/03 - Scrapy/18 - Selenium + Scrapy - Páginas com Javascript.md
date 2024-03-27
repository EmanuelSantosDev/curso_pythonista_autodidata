# Selenium + Scrapy - Páginas com Javascript


- Há uma situação específica em sites que rodam 100% ou parcialmente em Javascript.
- O Scrapy não consegue acessar os dados desses sites porque ele não possui um motor JavaScript integrado.
- O Scrapy funciona fazendo solicitações HTTP e analisando o HTML retornado.
- Se um site depende de JavaScript para carregar seu conteúdo ou interagir com o usuário, o Scrapy não conseguirá processar essas partes dinâmicas da página. 
- Em alguns sites a paginação não muda a URL.
- Para solucionar isso usamos um navegador que consegue carregar javascript: o **Webdriver do Selenium**.


**Exemplo prático de erro:**
```
scrapy shell 'https://dadosdinamicos.netlify.app/'
response.body

# Irá retornar scripts Javascript e não HTML
```


### Passo #1:
- Instalar o **Selenium**
- Instalar o **Webdriver-Manager**


### Passo #2:
```python
import scrapy
# o logging e o LOGGER serão utilizados para limitar os dados que
# serão mostrados no terminal e assim facilitar a leitura do mesmo
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
# o restante são as configurações padrão do Selenium
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as CondicaoExperada
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# cria objetos que representam documentos HTML ou XML e fornecem
# métodos para realizar seleções XPath e CSS nesses documentos
from scrapy.selector import Selector
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    # definindo o nível de informação que é exibida no console
    LOGGER.setLevel(logging.WARNING)
    # vamos carregar em Português, Full-HD para carregar as páginas
    # corretamente e o navegador aberto em 2º plano
    arguments = ['--lang=pt-BR', '--window-size=1920,1080', '--headless']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )

    return driver, wait


class ProductScraperSpider(scrapy.Spider):

    # identidade
    name = 'precobot'

    # Request
    def start_requests(self):
        # não esqueça de setar ROBOTSTXT_OBEY = False dentro do arquivo settings.py
        urls = ['https://dadosdinamicos.netlify.app/']
        for url in urls:
            # meta={'proximo_url': url} => passa o link para o WebDriver
            # É utilizado para passar informações adicionais para a próxima requisição
            yield scrapy.Request(url=url, callback=self.parse, meta={'proximo_url': url})

    # Response
    def parse(self, response):
        driver, wait = iniciar_driver()
        # acessando a URL com o WebDriver
        driver.get(response.meta['proximo_url'])
        # aguardar carregar a página
        sleep(10)
        # O driver.page_source contém o HTML da página carregada pelo WebDriver
        # e o Selector permite que você faça seleções XPath ou CSS nesse HTML.
        response_webdriver = Selector(text=driver.page_source)
        for produto in response_webdriver.xpath("//table/tr[@class='pro-list-info']"):
            yield {
                'Produto': produto.xpath("./td[1]/text()").get(),
                'Preço': produto.xpath("./td[2]/text()").get(),
                'Nota': produto.xpath("./td[3]/text()").get(),
            }
        driver.quit()
```