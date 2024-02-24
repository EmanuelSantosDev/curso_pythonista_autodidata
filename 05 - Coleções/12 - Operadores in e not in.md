# Operadores in e not in


São operadores de pertencimento que verificam se um valor está presente em uma sequência, como uma lista, tupla, conjunto ou string.


```python
# EXEMPLO 1: verificando se um elemento está presente em uma lista


lista = [1, 2, 3, 4, 5]

print(3 in lista)      # Saída: True
print(6 not in lista)  # Saída: True
print(5 not in lista)  # Saída: False


# EXEMPLO 2: verificando se uma substring está presente em uma string


texto = "Python é uma linguagem de programação poderosa"

print("linguagem" in texto)  # Saída: True
print("Java" not in texto)   # Saída: True
print("sql" in texto)        # Saída: False
```