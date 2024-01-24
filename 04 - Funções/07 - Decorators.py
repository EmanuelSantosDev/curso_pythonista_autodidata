# Decorators


'''
    * é uma construção que permite modificar ou estender a funcionalidade 
      de funções ou métodos sem alterar seu código interno.
    * o decorator 'envolve' a função alvo.
    * são uma forma elegante de reutilização de código.
'''


# passa a referência da função
def meu_decorator(funcao):
    def wrapper():
        print('Antes')
        funcao()
        print('Depois')
    return wrapper


@meu_decorator
def parabenizar():
    print('Parabéns')


parabenizar()

'''
Antes
Parabéns
Depois
'''
