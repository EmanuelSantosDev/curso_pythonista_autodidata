# Ordenando Coleções Através de Propriedades


```python
# importando a função 'itemgetter'
from operator import itemgetter


pessoas = [
    {'nome': 'John', 'idade': 32, 'nivel_acesso': 2},
    {'nome': 'Emanuel', 'idade': 37, 'nivel_acesso': 3},
    {'nome': 'Maria', 'idade': 24, 'nivel_acesso': 1},
    {'nome': 'Ana', 'idade': 44, 'nivel_acesso': 4},
    {'nome': 'Simaria', 'idade': 19, 'nivel_acesso': 1},
    {'nome': 'Patricia', 'idade': 27, 'nivel_acesso': 3}
]


pessoas.sort(key=itemgetter('nome'))
print(pessoas)
# [{'nome': 'Ana', 'idade': 44, 'nivel_acesso': 4},
# {'nome': 'Emanuel', 'idade': 37, 'nivel_acesso': 3},
# {'nome': 'John', 'idade': 32, 'nivel_acesso': 2},
# {'nome': 'Maria', 'idade': 24, 'nivel_acesso': 1},
# {'nome': 'Patricia', 'idade': 27, 'nivel_acesso': 3},
# {'nome': 'Simaria', 'idade': 19, 'nivel_acesso': 1}]


pessoas.sort(key=itemgetter('idade'))
print(pessoas)
# [{'nome': 'Simaria', 'idade': 19, 'nivel_acesso': 1},
# {'nome': 'Maria', 'idade': 24, 'nivel_acesso': 1},
# {'nome': 'Patricia', 'idade': 27, 'nivel_acesso': 3},
# {'nome': 'John', 'idade': 32, 'nivel_acesso': 2},
# {'nome': 'Emanuel', 'idade': 37, 'nivel_acesso': 3},
# {'nome': 'Ana', 'idade': 44, 'nivel_acesso': 4}]


# Ordenando uma Lista de Tuplas (passamos o índice)
# serve também para ordenar uma Matriz (lista de listas)
produtos = [
    ('Celular', 750),
    ('Bicicleta', 1500),
    ('Microfone', 550)
]
produtos.sort(key=itemgetter(1))
print(produtos)  
# [('Microfone', 550), 
# ('Celular', 750), 
# ('Bicicleta', 1500)]
produtos.sort(key=itemgetter(0))
print(produtos)  
# [('Bicicleta', 1500), 
# ('Celular', 750), 
# ('Microfone', 550)]


# Ordem DECRESCENTE
produtos.sort(key=itemgetter(0), reverse=True)
print(produtos)  
# [('Microfone', 550), 
# ('Celular', 750), 
# ('Bicicleta', 1500)]
```