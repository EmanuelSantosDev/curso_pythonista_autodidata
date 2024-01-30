'''
Função max()
============

- Retorna o item com o valor mais alto ou o item com o valor mais alto em um iterável.
- Se os valores forem strings, será feita uma comparação em ordem alfabética.
'''


x = max(5, 10)
print(x)  # 10


x = max("Mike", "Vicky", "John")
print(x)  # Vicky


a = (1, 5, 9, 3)
x = max(a)
print(x)  # 9


'''
Função min()
============

- Retorna o item com o valor mais baixo ou o item com o valor mais baixo em um iterável.
- Se os valores forem strings, será feita uma comparação em ordem alfabética.
'''

x = min(5, 10)
print(x)  # 5

x = min("Mike", "John", "Vicky")
print(x)  # John

a = (5, 1, 3, 9)
x = min(a)
print(x)  # 1


'''
Função sum()
============

- Retorna a soma de todos os itens em um iterável.
'''


a = (1, 2, 3, 4, 5)
x = sum(a)
print(x)  # 15

a = (1, 2, 3, 4, 5)
x = sum(a, 7)
print(x)  # 22
