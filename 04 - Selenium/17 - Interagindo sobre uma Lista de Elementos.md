# Interagindo sobre uma Lista de Elementos


#### Exemplo 1
```python
# encontrando os elementos com find_elements()
radio_buttons = browser.find_elements(By.ID, "paises")

# interagindo através do índice
radio_buttons[1].click()
```


#### Exemplo 2
```python
# encontrando os elementos com find_elements()
checkbox_motos = browser.find_elements(By.ID, 'motos')

# interagindo com toda a lista de elementos
for moto in checkbox_motos:
    moto.click()
```