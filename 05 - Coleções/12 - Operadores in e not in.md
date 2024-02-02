# Operadores in e not in


São operadores de pertencimento que verificam se um valor está presente em uma
sequência (como uma lista, tupla, conjunto ou string) ou não.


```python
# EXEMPLO 1: verificando se um elemento está presente em uma lista


lista = [1, 2, 3, 4, 5]

# Verifica se o valor 3 está presente na lista
print(3 in lista)  # Saída: True

# Verifica se o valor 6 não está presente na lista
print(6 not in lista)  # Saída: True

# Verifica se o valor 5 não está presente na lista
print(5 not in lista)  # Saída: False


# EXEMPLO 2: verificando se uma substring está presente em uma string


texto = "Python é uma linguagem de programação poderosa"

# Verifica se a substring "linguagem" está presente no texto
print("linguagem" in texto)  # Saída: True

# Verifica se a substring "Java" não está presente no texto
print("Java" not in texto)  # Saída: True

# Verifica se a substring "sql" está presente no texto
print("sql" in texto)  # Saída: False
```