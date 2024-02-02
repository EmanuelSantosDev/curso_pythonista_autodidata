# Criando Arquivos Diversos Vazios


```python
arquivos = ['musica.mp3', 'foto.jpg', 'senhas.txt', 'relatorio.pdf']


for arquivo in arquivos:
    with open(arquivo, 'w') as arquivo:
        pass
```