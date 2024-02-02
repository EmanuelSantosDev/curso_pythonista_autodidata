# Range (Geradores)


```python
# range() é uma função geradora
for numero in range(5):
    print(f'carregando #{numero}')
# carregando #0
# carregando #1
# carregando #2
# carregando #3
# carregando #4


# range() com argumento inicial e final
for numero in range(5, 11):
    print(f'carregando #{numero}')
# carregando  #5
# carregando  #6
# carregando  #7
# carregando  #8
# carregando  #9
# carregando  #10


# range() com step
for numero in range(1, 21, 2):
    print(f'carregando #{numero}')
# carregando #1
# carregando #3
# carregando #5
# carregando #7
# carregando #9
# carregando #11
# carregando #13
# carregando #15
# carregando #17
# carregando #19


# Criando listas rapidamente utilizando range()
minha_lista = list(range(0, 201, 10))
print(minha_lista)
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
# 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
```