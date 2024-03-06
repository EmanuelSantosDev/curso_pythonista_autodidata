# Configurações do Selenium


## Chromium Command Line Switches

- São uma série de opções que podem ser passadas como argumentos ao 
iniciar o navegador Chromium ou seus derivados, como o Google Chrome.
- Permitem controlar diversos aspectos do comportamento do navegador.


#### Links Úteis

- [chrome_switches.cc](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/chrome_switches.cc)
- [List of Chromium Command Line Switches](https://peter.sh/experiments/chromium-command-line-switches/)


#### Principais Comandos

|Comando                      |Ação                                               |
|-----------------------------|---------------------------------------------------|
| ``--start-maximized``       | Inicia maximizado                                 |
| ``--lang=pt-BR``            | Define o idioma de inicialização, # en-US , pt-BR |
| ``--incognito``             | Usar o modo anônimo                               |
| ``--window-size=800,800``   | Define a resolução da janela em largura e altura  |
| ``--headless``              | Roda em segundo plano (com a janela fechada)      |
| ``--disable-notifications`` | Desabilita notificações                           |
| ``--disable-gpu``           | Desabilita renderização com GPU                   |


## Opções Experimentais

- É usada para adicionar uma opção experimental.
- É geralmente uma configuração que ainda está em 
desenvolvimento e pode não estar disponível ou ser estável 
na versão padrão do navegador.

#### Links Úteis

- [pref_names.cc](https://chromium.googlesource.com/chromium/src/+/32352ad08ee673a4d43e8593ce988b224f6482d3/chrome/common/pref_names.cc?_gl=1*13j3oql*_ga*MTgyNjczODM2NS4xNzA3ODY2OTcz*_ga_37GXT4VGQK*MTcwODQ3MzczMS4xNy4xLjE3MDg0NzUyMDIuMC4wLjA.)

#### Principais Comandos

- Ver no código abaixo


## Configurando o Selenium
```python
# Importa o módulo 'webdriver' do Selenium, que fornece uma API para 
# interagir com os navegadores web.
from selenium import webdriver
# Importa o serviço do Chrome para controle do navegador.
from selenium.webdriver.chrome.service import Service as ChromeService
# Importa o gerenciador de drivers do Chrome para facilitar a 
# instalação e gerenciamento do driver do Chrome.
from webdriver_manager.chrome import ChromeDriverManager
# Importa as opções do Chrome para configurar o comportamento do navegador.
from selenium.webdriver.chrome.options import Options
# Importa a classe WebDriverWait para esperas explícitas.
from selenium.webdriver.support.ui import WebDriverWait
# Importa as exceções comuns do Selenium.
from selenium.common.exceptions import *
# Importa as condições esperadas do Selenium para espera explícita.
from selenium.webdriver.support import expected_conditions
# Importa o seletor de elementos By para localizar elementos na página.
from selenium.webdriver.common.by import By
# Importa a classe Keys para interação com o teclado.
from selenium.webdriver.common.keys import Keys
# Importa a classe Select para interação com elementos do tipo select.
from selenium.webdriver.support.select import Select
# Importa a classe ActionChains para realizar ações complexas e encadeadas.
from selenium.webdriver import ActionChains
# Importa a função sleep do módulo time para introduzir pausas no script.
from time import sleep
# Importa o módulo random para geração de números aleatórios.
import random


def iniciar_driver():

   # Configurando as opções de Inicialização do Google Chrome
   chrome_options = Options()

   # Chromium Command Line Switches
   arguments = ['--lang=pt-BR', '--window-size=1200,600', '--incognito']
   for argument in arguments:
      chrome_options.add_argument(argument)

   # Opções Experimentais
   chrome_options.add_experimental_option('prefs', {
      # Alterar o local padrão de download de arquivos
      'download.default_directory': 'D:\\Storage\\Desktop\\projetos_selenium\\downloads',
      # Notificar o Google Chrome sobre essa alteração
      'download.directory_upgrade': True,
      # Desabilitar a confirmação de download (não vai perguntar sobre o download)
      'download.prompt_for_download': False,
      # Desabilitar as notificações do navegador
      'profile.default_content_setting_values.notifications': 2,
      # Permitir multiplos downloads simultâneos
      'profile.default_content_setting_values.automatic_downloads': 1,
   })

   # Configurando o webdriver
   driver = webdriver.Chrome(service=ChromeService(
      ChromeDriverManager().install()), options=chrome_options)

   # Configurando o objeto wait
   wait = WebDriverWait(
       driver,
       10,
       poll_frequency=1,
       ignored_exceptions=[
           NoSuchElementException,
           ElementNotVisibleException,
           ElementNotSelectableException
       ]
   )

   return driver, wait


# Inicializando o driver e o wait
driver, wait = iniciar_driver()


# CÓDIGO AQUI


input('digite algo para fechar... ')
driver.close()
```