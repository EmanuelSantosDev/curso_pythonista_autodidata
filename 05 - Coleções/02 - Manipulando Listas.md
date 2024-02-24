# Manipulando Listas


```python
# adicionando itens ao final da lista
valores.append(11)


# adicionando itens em um índice específico
anos.insert(2, 2031)


# unindo listas (a primeira lista recebe os valores da segunda)
valores.extend(anos)


# unindo listas (gera uma nova lista)
nova_lista = valores + anos


# removendo itens com base no ÍNDICE e RETORNANDO O VALOR
# (retorna 'None' se o índice estiver fora dos limites)
item_extraido = anos.pop(3)


# removendo a primeira ocorrência com base no valor
anos.remove(2020)


# removendo com base no índice SEM RETORNAR O VALOR
del anos[1]


# com 'del' podemos REMOVER UMA FAIXA DE VALORES
del valores[2:11]


# contando a recorrência de valores
print(valores.count(2020))


# resetando uma lista
valores.clear()
```