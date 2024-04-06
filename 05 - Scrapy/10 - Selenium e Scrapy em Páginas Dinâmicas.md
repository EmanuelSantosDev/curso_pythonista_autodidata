# Selenium + Scrapy - Páginas com Javascript


- Há uma situação específica em sites que rodam 100% ou parcialmente em Javascript.
- O Scrapy não consegue acessar os dados desses sites porque ele não possui um motor JavaScript integrado.
- O Scrapy funciona fazendo solicitações HTTP e analisando o HTML retornado.
- Se um site depende de JavaScript para carregar seu conteúdo ou interagir com o usuário, o Scrapy não conseguirá processar essas partes dinâmicas da página. 
- Em alguns sites a paginação não muda a URL.
- Para solucionar isso usamos um navegador que consegue carregar javascript: o **Webdriver do Selenium**.
- Usamos o `logging` do Python e o `LOGGER` do Selenium para configurar a saída a partir de **_WARNING_** e assim deixar o terminal mais clean e de fácil visualização.
- A classe `Selector` cria objetos que representam documentos HTML ou XML e fornecem métodos para realizar seleções XPath e CSS nesses documentos.
- ``browser.page_source`` contém o HTML da página carregada pelo WebDriver.
- O parâmetro ``meta={'proximo_url': url}`` passa o link para o WebDriver. É utilizado para passar informações adicionais para a próxima requisição.


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
from selenium import webdriver
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector
from time import sleep


def iniciar_driver():

    chrome_options = Options()

    LOGGER.setLevel(logging.WARNING)

    arguments = ['--lang=pt-BR', '--window-size=1920,1080', '--headless']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    browser = webdriver.Chrome(options=chrome_options)

    wait = WebDriverWait(
        browser,
        20,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )

    return browser, wait


class ProductScraperSpider(scrapy.Spider):

    name = 'precobot'

    def start_requests(self):
        urls = ['https://dadosdinamicos.netlify.app/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={'proximo_url': url})

    def parse(self, response):
        browser, wait = iniciar_driver()
        browser.get(response.meta['proximo_url'])
        sleep(10)
        response_webdriver = Selector(text=browser.page_source)
        for produto in response_webdriver.xpath("//table/tr[@class='pro-list-info']"):
            yield {
                'Produto': produto.xpath("./td[1]/text()").get(),
                'Preço': produto.xpath("./td[2]/text()").get(),
                'Nota': produto.xpath("./td[3]/text()").get(),
            }
        browser.quit()
```