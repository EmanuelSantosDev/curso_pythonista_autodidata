# ``if __name__ == '__main__'``


* É uma construção usada para determinar se um script está sendo executado como o programa principal ou se está sendo importado como um módulo por outro script.
* Permite que você defina instruções ou funções que devem ser executadas apenas quando o script é executado como o programa principal, e não quando é importado como um módulo.
* ``__name__`` é uma variável especial em Python que contém o nome do módulo atual.
* Quando um arquivo Python é executado diretamente, ``__name__`` é definido como ``'__main__'``.
* Quando um arquivo Python é importado como um módulo em outro arquivo, ``__name__`` é definido como o nome do próprio módulo.


```python
''' 
EXEMPLO: Suponha que você tenha um módulo chamado calculadora.py que contém algumas
funções matemáticas úteis. Você deseja usá-lo em diferentes scripts para realizar
cálculos, mas também deseja poder executar alguns testes ou demonstrações quando 
o módulo calculadora.py é executado diretamente como um programa.
'''

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def main():
    print("Calculadora - Exemplo de Uso")
    print("Soma:", soma(5, 3))
    print("Subtração:", subtracao(10, 4))

if __name__ == '__main__':
    main()
```