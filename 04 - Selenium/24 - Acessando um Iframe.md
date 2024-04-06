# Acessando um IFRAME


- O ``<iframe>`` é um elemento HTML usado para incorporar outro documento HTML dentro de um documento principal.
- Cria uma janela retangular em uma página da web para exibir conteúdo de outra página da web.
- Primeiro é necessário entrar no iFrame, para depois poder interagir com ele.


```python
# localizando o iFrame
iframe = browser.find_element(
    By.XPATH, "//iframe[@src='https://cursoautomacao.netlify.app/desafios.html']")

# acessando o iFrame
browser.switch_to.frame(iframe)

# <<<< EXECUTA AS OPERAÇÕES NO IFRAME >>>>

# saindo do iframe e acessando a página principal novamente
browser.switch_to.default_content()
```