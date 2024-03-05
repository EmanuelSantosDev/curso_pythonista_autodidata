# ActionChains e Clique com o Botão Direito


- ``ActionChains`` é uma classe que permite:
   - combinar várias ações simples para realizar ações mais complexas
   - clicar com o botão direito do mouse em um elemento
   - mover o mouse para um elemento específico
   - arrastar e soltar elementos
   - pressionar e soltar teclas do teclado
- O método ``context_click()`` é usado para simular um clique com o botão direito do mouse
- O método ``perform()`` é o responsável por executar todas as ações encadeadas em sequência


### ActionChains Interagindo com o Botão Direito do Mouse
```python
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


# encontrando o elemento
botao = driver.find_element(By.ID, 'botao-direito')

# realizando o encadeamento
chain = ActionChains(driver)
chain.context_click(botao).pause(3).send_keys(Keys.DOWN).pause(3).send_keys(
    Keys.DOWN).pause(3).send_keys(Keys.DOWN).pause(3).click().perform()
```


### ActionChains Interagindo com Radio Buttons
```python
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


# encontrando o elemento
radio_windows = driver.find_element(By.ID, 'WindowsRadioButton')

# encontrando o elemento
chain = ActionChains(driver)
chain.click(radio_windows).pause(1).send_keys(Keys.DOWN).pause(1).send_keys(
    Keys.DOWN).pause(1).send_keys(Keys.UP).pause(1).send_keys(Keys.UP).perform()
```