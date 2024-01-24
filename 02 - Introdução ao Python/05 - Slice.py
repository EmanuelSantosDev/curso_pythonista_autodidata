# <<< Slice (extraindo partes de um string) >>>


equipamento = 'Teclado Ergonômico'


print(equipamento[2])  # c
print(equipamento[-1])  # o
print(equipamento.index('l'))  # 3
print(equipamento[equipamento.index('l')])  # l


# acessando partes de um string


link = 'facebook.com/emanuelsantos'


print(link[0])  # f
print(link[-1])  # s
print(link[0:5])  # faceb
print(link[0:])  # facebook.com/emanuelsantos
print(link[10:])  # om/emanuelsantos
print(link[-5:])  # antos
print(link[5:])  # ook.com/emanuelsantos
print(link[:-5])  # facebook.com/emanuels


# retornando o índice da última ocorrência de uma substring


frase = 'Clean Code'
print(frase.rindex('C'))  # 6
