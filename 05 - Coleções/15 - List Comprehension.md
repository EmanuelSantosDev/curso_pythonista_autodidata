# List Comprehension


- **List Comprehension** é uma forma concisa e elegante de criar listas em Python. 
- Ela permite criar uma lista a partir de qualquer tipo de iterável (como listas, tuplas, conjuntos, etc.) aplicando uma expressão a cada item do iterável.


```python
# [expressão for item in iterável]
dobros = [x * 2 for x in range(1, 6)]
print(dobros)  # [2, 4, 6, 8, 10]


# [expressão for item in iterável]
nomes = ['César', 'Emanuel', 'Luana', 'Tatiana']
nome_com_sobrenome = [nome + ' dos Santos' for nome in nomes]
print(nome_com_sobrenome)
# ['César dos Santos', 
# 'Emanuel dos Santos', 
# 'Luana dos Santos', 
# 'Tatiana dos Santos']


# [função(item) for item in iterável]
def sobrenome_almeida(nome):
    return nome + ' de Almeida'

nome_com_sobrenome = [sobrenome_almeida(nome) for nome in nomes]
print(nome_com_sobrenome)
# ['César de Almeida', 
# 'Emanuel de Almeida', 
# 'Luana de Almeida', 
# 'Tatiana de Almeida']


# [[i for i in iterável] for x in iterável] => MATRIZ
matriz = [[i for i in range(1, 6)] for x in range(5)]
print(matriz)
# [[1, 2, 3, 4, 5], 
# [1, 2, 3, 4, 5], 
# [1, 2, 3, 4, 5], 
# [1, 2, 3, 4, 5], 
# [1, 2, 3, 4, 5]]


# [expressao for membro in iterável (condicional if)]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [n for n in numeros if n % 2 == 0]
print(pares)  # [2, 4, 6, 8, 10]


# [expressao (condicional if + condicional else) for item in iterável]
participantes = ['Larissa', 'Rafael', 'Marcus', 'John']
ganhadores = ['Marcus', 'John']
lista_final = [nome + ' GANHADOR' if nome in ganhadores else nome +
               ' NÃO SELECIONADO' for nome in participantes]
print(lista_final)
# ['Larissa NÃO SELECIONADO', 
# 'Rafael NÃO SELECIONADO', 
# 'Marcus GANHADOR', 
# 'John GANHADOR']
```