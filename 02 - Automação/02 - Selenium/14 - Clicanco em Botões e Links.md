# Clicando em Botões e Links


```python
# Localizando o Elemento
botao_dropdown = driver.find_element(By.ID, 'btn')

# Forma #1
botao_dropdown.click()

# Forma #2 (utilizando código Javascript)
# normalmente o click() padrão não funciona em botões de novas janelas
driver.execute_script('arguments[0].click()', botao_abrir_janela)
```