# Pausas com WAIT EXPLÍCITO


- As **esperas explícitas** são técnicas que além do tempo, aguardam também *determinadas condições* antes de executar as próximas etapas da automação/teste.
- A classe ``WebDriverWait`` é usada para implementar esperas explícitas no Selenium WebDriver.
- O objeto ``wait`` representa o período de tempo que o WebDriver aguardará até que uma determinada condição seja atendida. 
- A espera é realizada utilizando o método ``until``.
- **Condições**:
   - ``element_to_be_clickable``: espera até que um **ÚNICO** elemento específico seja clicável na página da web. 
   - ``visibility_of_all_elements_located``: espera até que todos os elementos especificados estejam visíveis na página. É útil quando você deseja garantir que todos os elementos de uma determinada **LISTA** estejam visíveis antes de realizar ações.
   - ``visibility_of_any_elements_located``: espera até que pelo menos um elemento específico seja visível na página da web. É útil quando você deseja garantir que pelo menos um elemento de uma determinada **LISTA** esteja visível antes de realizar ações.


#### Configuração
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions


# o trecho abaixo deve ser incluído na função que inicializa o driver
wait = WebDriverWait(
    browser,
    10,
    poll_frequency=1,
    ignored_exceptions=[
        NoSuchElementException,
        ElementNotVisibleException,
        ElementNotSelectableException
    ]
)

return browser, wait
```


#### Utilização
```python
# situação 1 (retorna 1 elemento apenas)
formulario_de_destino = wait.until(expected_conditions.element_to_be_clickable(
    (By.XPATH, "//input[@placeholder='Para onde?']")))

formulario_de_destino.send_keys('Porto Alegre')


# situação 2 (retorna uma lista de elementos)
sugestoes_de_voo = wait.until(expected_conditions.visibility_of_all_elements_located(
    (By.XPATH, '//ol[@jsname="H4aYKc"]//li')))

sugestoes_de_voo[2].click()


# situação 3 (retorna uma lista de elementos)
sugestoes_de_voo = wait.until(expected_conditions.visibility_of_any_elements_located(
    (By.XPATH, '//ol[@jsname="H4aYKc"]//li')))

sugestoes_de_voo[2].click()
```