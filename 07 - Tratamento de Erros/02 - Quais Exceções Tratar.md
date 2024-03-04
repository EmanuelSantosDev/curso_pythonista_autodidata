# Quais Exceções Tratar?


- Você pode realizar testes e experimentar diferentes entradas para ver quais exceções são lançadas.
- Leia o **Traceback** para entender melhor qual exceção ocorreu e em que parte do código.
- Um **Traceback** é uma saída detalhada que o interpretador Python gera quando ocorre uma exceção durante a execução de um programa. 


```python
try:
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun',
             'jul', 'ago', 'set', 'out', 'nov', 'dez']
    print(meses[15])
except IndexError as erro:
    print('Favor acesser um índice válido')
    print(erro)  # list index out of range


# Traceback do Código Acima antes de incluir o bloco Try-Except:
'''
Traceback (most recent call last):
  File "c:\\repositorios\\curso_pythonista_autodidata\\app.py", line 28, in <module>
    print(meses[15])
          ~~~~~^^^^
IndexError: list index out of range '''
```