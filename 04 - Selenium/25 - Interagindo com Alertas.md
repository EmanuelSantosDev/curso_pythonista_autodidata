# Interagindo com ALERTAS


```python
# SITUAÇÃO #1 => Alerta Padrão (aguarda OK)
alerta_padrao = browser.switch_to.alert
alerta_padrao.accept()


# SITUAÇÃO #2 => Confirmação (aguarda OK ou CANCELAR)
alerta_confirmacao = browser.switch_to.alert
alerta_confirmacao.accept()
alerta_confirmacao.dismiss()  # caso queira cancelar


# SITUAÇÃO #3 => Prompt (aguarda TEXTO + OK ou CANCELAR + OK)
alerta_prompt = browser.switch_to.alert
alerta_prompt.send_keys('25 de Janeiro')  # o Selenium não mostra na tela
alerta_prompt.accept()
alerta_prompt.dismiss()  # caso queira cancelar
alerta_prompt.dismiss()  # fecha a 2ª janela que abre após a confirmação
```