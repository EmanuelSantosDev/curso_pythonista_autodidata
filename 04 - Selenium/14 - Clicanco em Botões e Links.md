# Clicando em Botões e Links


```python
# Localizando o Elemento
botao_dropdown = browser.find_element(By.ID, 'btn')

# Forma #1
botao_dropdown.click()

# Forma #2 (utilizando código Javascript)
# normalmente o click() padrão não funciona em botões de novas janelas
browser.execute_script('arguments[0].click()', botao_abrir_janela)
```