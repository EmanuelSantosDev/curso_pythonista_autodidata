# Arrays


- Armazenam elementos de um tipo de dado específico.
- Atualmente foram criadas bibliotecas específicas para trabalhar com listas.
- Arrays normalmente serão encontrados em programas legados.


```python
from array import array


numeros = array('i', [1, 2, 3, 4, 5, 6])
print(numeros)  # array('i', [1, 2, 3, 4, 5, 6])


# utiliza os mesmos métodos que listas


numeros.append(10)
print(numeros)  # array('i', [1, 2, 3, 4, 5, 6, 10])

numeros.insert(5, 200)
print(numeros)  # array('i', [1, 2, 3, 4, 5, 200, 6, 10])

numeros.pop(1)
print(numeros)  # array('i', [1, 3, 4, 5, 200, 6, 10])

numeros.remove(5)
print(numeros)  # array('i', [1, 3, 4, 200, 6, 10])

del numeros[1]
print(numeros)  # array('i', [1, 4, 200, 6, 10])
```