# Descobrindo se um Elemento está Habilitado


```python
# localizando o elemento
botao = browser.find_element(By.ID, "botao")

# checando se está habilitado
print(botao.is_enabled())  # True ou False
```