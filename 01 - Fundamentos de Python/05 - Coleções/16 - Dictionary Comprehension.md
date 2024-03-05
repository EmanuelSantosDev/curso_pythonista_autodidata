# Dictionary Comprehension


É uma forma concisa e eficiente de criar dicionários em Python a partir de qualquer iterável, de forma mais sucinta e legível.


```python
from pprint import pprint


# {expressão: expressão for item in iterável}
pprint({i: i for i in range(6)})
'''
{0: 0,
 1: 1,
 2: 2,
 3: 3,
 4: 4,
 5: 5}
'''


# {expressão: expressão for item in iterável}
produtos = ['Arroz', 'Feijão', 'Massa', 'Molho de Tomate', 'Vinagre']
pprint({indice + 1: produto + ' adicionado' for indice,
       produto in enumerate(produtos)})
'''
{1: 'Arroz adicionado',
 2: 'Feijão adicionado',
 3: 'Massa adicionado',
 4: 'Molho de Tomate adicionado',
 5: 'Vinagre adicionado'} '''


# {expressão: [expressão for membro in iterável] for membro in iterável} ==> MATRIZ
pprint({produto: [i for i in range(1, 6)] for produto in produtos})
'''
{'Arroz': [1, 2, 3, 4, 5],
 'Feijão': [1, 2, 3, 4, 5],
 'Massa': [1, 2, 3, 4, 5],
 'Molho de Tomate': [1, 2, 3, 4, 5],
 'Vinagre': [1, 2, 3, 4, 5]} '''
```