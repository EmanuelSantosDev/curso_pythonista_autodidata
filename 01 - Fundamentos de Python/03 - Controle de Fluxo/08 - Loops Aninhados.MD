# Loops Aninhados


```python
paises = ['Brasil', 'Argentina', 'Inglaterra', 'Itália', 'Alemanha', 'França']
estacoes = ['Verão', 'Outono', 'Inverno', 'Primavera']


for pais in paises:
    for estacao in estacoes:
        print(f'{pais}: {estacao}')

'''
Brasil: Verão
Brasil: Outono
Brasil: Inverno
Brasil: Primavera
Argentina: Verão
Argentina: Outono
Argentina: Inverno
Argentina: Primavera
Inglaterra: Verão
Inglaterra: Outono
Inglaterra: Inverno
Inglaterra: Primavera
Itália: Verão
Itália: Outono
Itália: Inverno
Itália: Primavera
Alemanha: Verão
Alemanha: Outono
Alemanha: Inverno
Alemanha: Primavera
França: Verão
França: Outono
França: Inverno
França: Primavera
'''


# utilizando range()


for x in range(1, 6):
    for y in range(20, 26):
        print(f'x: {x}, y: {y}')

'''
x: 1, y: 20
x: 1, y: 21
x: 1, y: 22
x: 1, y: 23
x: 1, y: 24
x: 1, y: 25
x: 2, y: 20
x: 2, y: 21
x: 2, y: 22
x: 2, y: 23
x: 2, y: 24
x: 2, y: 25
x: 3, y: 20
x: 3, y: 21
x: 3, y: 22
x: 3, y: 23
x: 3, y: 24
x: 3, y: 25
x: 4, y: 20
x: 4, y: 21
x: 4, y: 22
x: 4, y: 23
x: 4, y: 24
x: 4, y: 25
x: 5, y: 20
x: 5, y: 21
x: 5, y: 22
x: 5, y: 23
x: 5, y: 24
x: 5, y: 25
'''
```