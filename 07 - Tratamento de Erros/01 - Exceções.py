'''
EXCEÇÕES
========


As exceções são eventos que ocorrem durante a execução de um programa e interrompem 
o fluxo normal de execução devido a algum erro ou condição inesperada. 

Exemplos de exceções comuns:

    - ZeroDivisionError
    - TypeError
    - FileNotFoundError
    - ValueError
    - IOError


ESTRUTURA DE EXCEÇÃO
====================


try:
    # Código que pode gerar uma exceção
except Excecao1:
    # Tratamento para Excecao1
except Excecao2:
    # Tratamento para Excecao2
else:
    # Executado se nenhum erro ocorrer no bloco try
finally:
    # Sempre executado, independentemente de ocorrer exceção ou não

    
    - O bloco 'try' é usado para envolver o código onde uma exceção pode ocorrer.
    - O bloco 'except' é usado para capturar exceções específicas e fornecer 
      tratamento para elas.
    - Você pode usar múltiplos blocos 'except' para tratar diferentes tipos de 
      exceções de maneira diferente.
    - O bloco 'else' é opcional e é executado se nenhum erro ocorrer no bloco 'try'.
    - O bloco 'finally' é opcional e é sempre executado, independentemente de 
      ocorrer uma exceção ou não.
'''
