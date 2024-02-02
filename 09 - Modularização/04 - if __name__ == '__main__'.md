# ``if __name__ == '__main__'``


* Usado para determinar se o arquivo está sendo executado como um programa principal  ou se está sendo importado como um módulo em outro arquivo. 
* Essa técnica é útil para separar código que deve ser executado apenas quando o arquivo é o programa principal, de código que pode ser importado e reutilizado em outros contextos.
* ``__name__`` é uma variável especial em Python que contém o nome do módulo atual.
* Quando um arquivo Python é executado diretamente, ``__name__`` é definido como ``'__main__'``.
* Quando um arquivo Python é importado como um módulo em outro arquivo, ``__name__`` é definido como o nome do próprio módulo.


```python
def funcao():
    print("Esta é uma função.")


if __name__ == '__main__':
    # Este código será executado apenas quando 
    # o arquivo for executado diretamente
    print("Este arquivo está sendo executado como o programa principal.")
    funcao()
```