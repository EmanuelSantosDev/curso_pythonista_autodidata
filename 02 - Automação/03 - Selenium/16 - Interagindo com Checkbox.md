# Interagindo com CHECKBOX


```python
# encontrando os elementos de checkbox
checkbox_1 = driver.find_element(
    By.XPATH, "//input[@id='acessoNivel1Checkbox']")
checkbox_2 = driver.find_element(
    By.XPATH, "//input[@id='acessoNivel2Checkbox']")
checkbox_3 = driver.find_element(
    By.XPATH, "//input[@id='acessoNivel3Checkbox']")

# com checkbox é possível fazer múltiplas seleções
checkbox_1.click()
checkbox_2.click()
checkbox_3.click()

# verificando se o checkbox está selecionado
print(checkbox_1.is_selected())  # True ou False
```