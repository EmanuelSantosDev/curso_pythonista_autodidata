# Upload de Arquivos


```python
# encontrando o botão de escolher arquivo
botao_escolher_arquivo = browser.find_element(By.ID, "botao_selecionar")

# digitando o caminho do arquivo
botao_escolher_arquivo.send_keys('C:\\Users\\euema\\Downloads\\arquivo_teste.pdf')

# encontrando o botão de enviar
botao_enviar = browser.find_element(By.ID, "botao_enviar")

# clicando no botão de enviar
botao_enviar.click()
```