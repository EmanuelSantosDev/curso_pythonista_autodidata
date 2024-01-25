# Encontrando e Manipulando Itens da Lista


valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
anos = [2020, 2030, 2040, 2020]


# adicionando itens ao final da lista
valores.append(11)
print(valores)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


# adicionando itens pelo índice
anos.insert(2, 2031)
print(anos)  # [2020, 2030, 2031, 2040, 2020]


# unindo listas
valores.extend(anos)
print(valores)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2020, 2030, 2031, 2040, 2020]


# unindo listas, porém, em uma nova lista sem alterar as originais
nova_lista = valores + anos
print(nova_lista)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2020, 2030, 2031, 2040, 2020,
# 2020, 2030, 2031, 2040, 2020]


# removendo com base no índice e RETORNANDO O VALOR
# retorna 'None' se o índice estiver fora dos limites
item_extraido = anos.pop(3)
print(item_extraido)  # 2040
print(anos)  # [2020, 2030, 2031, 2020]


# removendo a primeira ocorrência com base no valor
anos.remove(2020)
print(anos)  # [2030, 2031, 2020]


# removendo com base no índice SEM RETORNAR O VALOR
# gera um 'IndexError' (exceção)
# 'del': É uma declaração do Python e não uma função.
# Pode ser usado para remover elementos de diferentes tipos de objetos,
# não apenas listas.
del anos[1]
print(anos)  # [2030, 2020]


# com 'del' podemos REMOVER UMA FAIXA DE VALORES
print(valores)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2020, 2030, 2031, 2040, 2020]
del valores[2:11]
print(valores)
# [1, 2, 2020, 2030, 2031, 2040, 2020]


# contando a ocorrência de valores
print(valores.count(2020))  # 2


# resetando uma lista
valores.clear()
print(valores)  # []
