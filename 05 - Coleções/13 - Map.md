# Map


A função ``map()`` é utilizada para aplicar uma função a cada elemento de uma ou mais sequências (como listas, tuplas, etc.) e retornar um iterador dos resultados.


```python
nomes = ['Larissa', 'Rafael', 'Marcus', 'John']
nomes_com_sobrenome = list(map(lambda nome: nome + ' Santos', nomes))
print(nomes_com_sobrenome)
# ['Larissa Santos', 'Rafael Santos', 'Marcus Santos', 'John Santos']
```