# Abrindo Páginas da Web


A biblioteca ``webbrowser`` é uma biblioteca padrão do Python que fornece uma interface simplificada para abrir páginas da web em navegadores da web padrão do sistema operacional. 


```python
import webbrowser


# Abre a URL no navegador padrão do sistema
webbrowser.open('https://www.globo.com/')

# Abre a URL em uma nova aba do navegador
webbrowser.open_new_tab('https://www.globo.com/')

# Abre a URL em uma nova janela do navegador
webbrowser.open_new('https://www.globo.com/')
```