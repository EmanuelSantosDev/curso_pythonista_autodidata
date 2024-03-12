# Métodos Mais Comuns do Webdriver


```python
# Maximiza a janela
driver.maximize_window() 

# Recarrega página atual
driver.refresh()  

# Recarrega página atual (versão 2)
driver.get(driver.current_url) 

# Volta à página anterior
driver.back()  

# Avança para a próxima página no histórico de navegação
driver.forward()  

# Obtém título da página
titulo = driver.title

# Obtém o URL(endereço) da página atual
endereco = driver.current_url  

# Obtém o código-fonte HTML da página atual
codigo_fonte = driver.page_source

# Obtém o texto dentro de um elemento
texto_do_elemento = driver.find_element(By.TAG_NAME, 'h1').text

# Obtém o valor de um atributo
valor_do_atributo = driver.find_element(
   By.XPATH, '//a[@class="navbar-brand"]').get_attribute("style")
```