# Métodos Mais Comuns do Webdriver


```python
# Maximiza a janela
browser.maximize_window() 

# Recarrega página atual
browser.refresh()  

# Recarrega página atual (versão 2)
browser.get(browser.current_url) 

# Volta à página anterior
browser.back()  

# Avança para a próxima página no histórico de navegação
browser.forward()  

# Obtém título da página
titulo = browser.title

# Obtém o URL(endereço) da página atual
endereco = browser.current_url  

# Obtém o código-fonte HTML da página atual
codigo_fonte = browser.page_source

# Obtém o texto dentro de um elemento
texto_do_elemento = browser.find_element(By.TAG_NAME, 'h1').text

# Obtém o valor de um atributo
valor_do_atributo = browser.find_element(By.TAG_NAME, 'h1').get_attribute("style")
```