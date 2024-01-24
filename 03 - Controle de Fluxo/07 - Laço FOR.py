# Loop 'for'


# range() é uma função geradora
for numero in range(5):
    print(f'carregando #{numero}')

'''
carregando #0
carregando #1
carregando #2
carregando #3
carregando #4
'''


# delimitando inicio e fim do range()
for numero in range(1, 6):
    print(f'carregando #{numero}')

'''
carregando #1
carregando #2
carregando #3
carregando #4
carregando #5
'''


# range() com step
for numero in range(1, 21, 2):
    print(f'carregando #{numero}')

'''
carregando #1
carregando #3
carregando #5
carregando #7
carregando #9
carregando #11
carregando #13
carregando #15
carregando #17
carregando #19
'''


# utilizando um iterável
clubes = ['Chelsea', 'United', 'City', 'Liverpool', 'Arsenal']
for clube in clubes:
    print(f'Clube: {clube}')

'''
Clube: Chelsea
Clube: United
Clube: City
Clube: Liverpool
Clube: Arsenal
'''
