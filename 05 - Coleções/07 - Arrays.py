# Arrays


# armazena elementos de um tipo de dado específico
# foram criadas bibliotecas específicas para trabalhar com listas
# arrays normalmente serão encontrados em programas legados


from array import array


numeros = array('i', [1, 2, 3, 4, 5, 6])
print(numeros)  # array('i', [1, 2, 3, 4, 5, 6])

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
