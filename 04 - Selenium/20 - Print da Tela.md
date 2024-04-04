# Print da Tela


```python
# tirando print da tela
driver.save_screenshot('C:\\Users\\euema\\Downloads\\tela1.jpg')

# rolando a tela
driver.execute_script('window.scrollTo(0, 2000)')

# tirando o print da nova região do site
driver.save_screenshot('C:\\Users\\euema\\Downloads\\tela2.jpg')
```