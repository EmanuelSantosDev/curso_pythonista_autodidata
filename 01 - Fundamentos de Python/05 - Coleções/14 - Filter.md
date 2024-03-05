# Filter


A função ``filter()`` é utilizada para filtrar elementos de uma sequência (como uma lista, tupla, etc.) com base em uma função de teste, que deve retornar ``True`` ou ``False``.



```python
# Sintaxe Básica:
filter(funcao, iteravel)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares) # Saída: [2, 4, 6, 8, 10]
```