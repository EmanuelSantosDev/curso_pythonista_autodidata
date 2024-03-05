# Interagindo com RADIO BUTTONS


```python
# operando sobre um único radio button
linux_radio_button = driver.find_element(
    By.XPATH, "//input[@id='WindowsRadioButton']")
linux_radio_button.click()

# operando sobre uma lista de radio buttons
radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
radio_buttons[1].click()

# verificando se o radio button já está selecionado
print(radio_buttons[1].is_selected())  # True ou False
```