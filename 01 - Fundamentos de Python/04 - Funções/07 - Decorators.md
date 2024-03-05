# Decorators



- é uma construção que permite modificar ou estender a funcionalidade de funções ou métodos sem alterar seu código interno.
- o decorator _envolve_ a função alvo.
- é uma forma elegante de reutilização de código.


```python
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
# Antes
# Parabéns
# Depois
```