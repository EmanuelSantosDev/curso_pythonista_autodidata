# Números e Operações Matemáticas


```python
# Tipos de Números


a = 20
b = 20.5
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>


# Operações Matemáticas


print(10 + 6)  # 16
print(10 - 6)  # 4
print(10 * 6)  # 60
print(10 / 6)  # 1.6666666666666667
print(10 // 6)  # 1 (divisão de inteiro)
print(10 % 6)  # 4 (modulos / resto da divisão)
print(10 ** 6)  # 1000000 (exponenciação)


# Atribuições Mais Rápidas


a = 10
a = a + 5
a += 5

b = 20
b = b - 2
b -= 2


# Operações de Arredondamento


import math


# Arredondamento para um número inteiro mais próximo:
print(round(5.7))  # 6
print(round(5.4))  # 5

# Arredondamento para um número específico de casas decimais:
print(round(3.14159, 2))  # 3.14

# Arredondando para cima
print(math.ceil(2.2))  # 3

# Arredondando para baixo
print(math.floor(2.9))  # 2
```