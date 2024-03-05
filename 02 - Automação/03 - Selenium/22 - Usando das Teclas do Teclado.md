# Usando as Teclas do Teclado


```python
# importando a classe Keys
from selenium.webdriver.common.keys import Keys

# localizando o elemento e selecionado
botao = driver.find_element(By.ID, 'WindowsRadioButton')
botao.click()

# utilizando as teclas
botao.send_keys(Keys.ARROW_DOWN)
botao.send_keys(Keys.TAB)
botao.send_keys(Keys.BACKSPACE)
botao.send_keys(Keys.ENTER)
```