# Enumerate


'''
É utilizada para iterar sobre uma sequência, enquanto acompanha 
o índice de cada elemento. 

É possível configurar o valor inicial do índice.

Sintaxe:
enumerate(iteravel, start=0)
'''


# Enumerate sobre uma Lista
frutas = ['Maça', 'Banana', 'Melão', 'Morango']
for indice, fruta in enumerate(frutas):
    print(f'{indice} - {fruta}')
    # 0 - Maça
    # 1 - Banana
    # 2 - Melão
    # 3 - Morango


# Enumerate sobre um Range com índice 1000
for i, n in enumerate(range(30, 50, 3), 1000):
    print(f'{i} - {n}')
    # 1000 - 30
    # 1001 - 33
    # 1002 - 36
    # 1003 - 39
    # 1004 - 42
    # 1005 - 45
    # 1006 - 48
