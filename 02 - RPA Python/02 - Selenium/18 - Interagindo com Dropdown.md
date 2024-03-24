# Interagindo com DROPDOWN


```python
# importando o módulo Select
from selenium.webdriver.support.select import Select


# localizando o elemento 'select'
paises_dropdown = driver.find_element(By.ID, 'paisselect')

# extraindo a lista de opções do elemento select
opcoes = Select(paises_dropdown)

# acessando por índice (inicia em 1)
opcoes.select_by_index(2)

# acessando pelo atributo 'value'
opcoes.select_by_value('brasil')

# acessando pelo texto visivel
opcoes.select_by_visible_text('Estados Unidos')
```