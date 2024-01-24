# Loop Whyle


contador = 0

while contador < 3:
    print('tente novamente')
    contador += 1

'''
tente novamente
tente novamente
tente novamente
'''


# Exemplo 2


senha = ''

while senha != '1234':
    senha = input('Digite sua senha: ')

print('Bem vindo!')


# Exemplo 3


nome = ''

while nome == '':
    nome = input('Digite seu nome: ')

print(f'Bem-vindo {nome}!')


# Exemplo 4


contador = 10

while contador >= 0:
    print(contador)
    contador -= 1

'''
10
9
8
7
6
5
4
3
2
1
0
'''
