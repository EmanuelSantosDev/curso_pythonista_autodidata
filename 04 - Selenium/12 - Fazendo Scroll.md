# Como Fazer Scroll


```python
# Rolar até o fim da página
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# Rolar até o topo da página
browser.execute_script("window.scrollTo(0, document.body.scrollTop)")

# Rolar X quantidade em pixels(descer)
browser.execute_script("window.scrollTo(0, 1500)")

# Rolar X quantidade em pixels(subir)
browser.execute_script("window.scrollTo(0, -1500)")
```