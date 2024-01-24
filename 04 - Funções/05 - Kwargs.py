# Kwargs


# '**kwargs' (keyword arguments)


# '**kwargs' é um dicionário
def concatenar(**palavras):
    print(palavras)
    # {'a': 'Nós', 'b': 'Somos', 'c': 'Pythonistas', 'd': 'Profissionais'}
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)


concatenar(a='Nós', b='Somos', c='Pythonistas', d='Profissionais')
# Nós Somos Pythonistas Profissionais
