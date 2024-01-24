# Operadores de Igualdade


a = 'Python'
b = 'Python'
c = 'python'


print(a == b)  # True
print(a == c)  # False


print(a is b)


# operador 'is'


# verifica se dois objetos têm o mesmo endereço de memória
# testa a identidade do objeto, não o valor

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
# True, porque a e b referenciam o mesmo objeto na memória
print(a is c)
# False, porque a e c são objetos diferentes, embora tenham valores iguais
