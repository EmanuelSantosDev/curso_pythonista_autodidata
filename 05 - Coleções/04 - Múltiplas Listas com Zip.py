# Múltiplas Listas com Zip


'''
A função zip() é utilizada para combinar elementos 
de iteráveis (como listas, tuplas, etc.) em pares ordenados.

Ela retorna um objeto zip, que é um iterador de tuplas.
'''


from itertools import zip_longest


lista_a = ['A', 'B', 'C', 'D', 'E']
lista_b = [1, 2, 3, 4, 6]


for a, b in zip(lista_a, lista_b):
    print(f'{a}: {b}')
'''
A: 1
B: 2
C: 3
D: 4
E: 6
'''


# Operando sobre Listas de tamanhos diferentes
# importamos a classe 'zip_longest' do módulo 'itertools'
# assim garantimos que será interado sobre a lista completa


titulos = ['Titulo 1', 'Titulo 2', 'Titulo 3', 'Titulo 4']
descricoes = ['Descricao 1', 'Descricao 2', 'Descricao 3']

# sem zip_longest
for a, b in zip(titulos, descricoes):
    print(f'{a}: {b}')
'''
Titulo 1: Descricao 1
Titulo 2: Descricao 2
Titulo 3: Descricao 3
'''

# com zip_longest
for a, b in zip_longest(titulos, descricoes):
    print(f'{a}: {b}')
'''
Titulo 1: Descricao 1
Titulo 2: Descricao 2
Titulo 3: Descricao 3
Titulo 4: None
'''
