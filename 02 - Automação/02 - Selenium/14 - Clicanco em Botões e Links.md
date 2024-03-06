# Clicando nos Elementos


```python
# Localizando o Elemento
botao_dropdown = driver.find_element(
    By.CSS_SELECTOR, '.btn.btn-success.dropdown-toggle')

# Forma #1
botao_dropdown.click()

# Forma #2 (utilizando código Javascript)
driver.execute_script('arguments[0].click()', botao_dropdown)
```