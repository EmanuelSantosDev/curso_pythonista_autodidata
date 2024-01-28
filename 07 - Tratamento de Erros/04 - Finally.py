# Finally


internet = None


try:
    print('Fazendo conexão com a ' + internet)
except TypeError as erro:
    print('Não há conexão com a internet')
finally:
    print('Desfazendo a compra')


'''
Não há conexão com a internet
Desfazendo a compra
'''
