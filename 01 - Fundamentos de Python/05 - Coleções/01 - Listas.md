# Listas


```python
precos = [10, 20, 30, 40, 50, 60, 100, 250, 230, 560, 23, 74]
print(precos[1])  # 20


# Descobrindo o índice de um valor
indice = precos.index(100)
print(indice)  # 6


# Listas no Python são dinâmicas (aceitam qualquer tipo de dado)
itens = [1, 3, 6, 'Grêmio', 'Inter', True, 10.6]
print(itens[5])  # True


# Criando Listas com Multiplicação (exemplo #1)
lista_de_noves = [9] * 10
print(lista_de_noves)   # [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]


# Criando Listas com Multiplicação (exemplo #2)
lista_de_testes = ['Teste'] * 4
print(lista_de_testes)  # ['Teste', 'Teste', 'Teste', 'Teste']


# Criando Listas com range()
lista_range = list(range(11))
print(lista_range)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Criando Listas com Strings
frase = list('Welcome')
print(frase)  # ['W', 'e', 'l', 'c', 'o', 'm', 'e']


# Criando uma Matriz
cadastros = [['Emanuel', 37], ['Yasmin', 32], ['Paulo', 27]]
print(cadastros[2][1])  # 27
```