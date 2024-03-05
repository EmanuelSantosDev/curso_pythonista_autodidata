# Importação


```python
from modulo_teste import sou_uma_variavel, sou_uma_funcao, SouUmaClase


print(sou_uma_variavel)  # Sou uma variável
sou_uma_funcao()  # Sou uma função
classe = SouUmaClase()
classe.sou_uma_clase()  # Sou uma classe
```



### Arquivo modulo_teste.py
```python
sou_uma_variavel = 'Sou uma variável'


def sou_uma_funcao():
    print('Sou uma função')


class SouUmaClase:
    def sou_uma_clase(self):
        print('Sou uma classe')
```