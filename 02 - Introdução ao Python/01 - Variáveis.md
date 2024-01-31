# Variáveis em Python


```python
# Atribução de Valor à Variável / Alocando Memória
velocidade_internet = 10

# Números
velocidade_internet = 20

# Valores Boleanos
velocidade_internet = True

# Strings
velocidade_internet = 'Dez'

# Unpacking
# descompactação de conteúdo de uma sequência em variáveis separadas de maneira eficiente
a, b, c, d = 1, 2, 3, 4

lista = [1, 2, 3]
a, b, c = lista
print(a)  # Saída: 1
print(b)  # Saída: 2
print(c)  # Saída: 3

tupla = ('a', 'b', 'c')
x, y, z = tupla
print(x)  # Saída: 'a'
print(y)  # Saída: 'b'
print(z)  # Saída: 'c'

dicionario = {'nome': 'João', 'idade': 30}
nome, idade = dicionario.values()
print(nome)  # Saída: 'João'
print(idade)  # Saída: 30
```