# None


'''
'None' é um valor especial que representa a ausência de valor.

É frequentemente usado para indicar que uma variável ou objeto não 
possui um valor definido ou não retornou nenhum valor.


'''


# Verificando se uma variável foi incializada:
variavel = None
if variavel is None:
    print("A variável não foi inicializada ou possui valor None")


# Esta função não retorna nada explicitamente, então retorna implicitamente None
def funcao():
    pass


retorno = funcao()
print(retorno)  # None
