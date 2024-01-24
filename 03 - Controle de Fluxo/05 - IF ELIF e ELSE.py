# IF


trabalho_terminado = False

if trabalho_terminado:
    print('Bora dar uma saida!')


# ELSE


if trabalho_terminado:
    print('Bora dar uma saida!')
else:
    print('Não posso sair agora.')


# ELIF


numero_atrasos = 2

if numero_atrasos >= 3:
    print('Vá para a Diretoria')
elif numero_atrasos == 2:
    print('Essa é sua segunda falta')
elif numero_atrasos == 1:
    print('Essa é sua primeira falta')
else:
    print('Pode entrar')


# Chaining


velocidade = 76

if velocidade <= 50:
    print('Não foi multado')
elif 51 <= velocidade <= 60:
    print('Levou multa de 2 pontos')
elif 61 <= velocidade <= 75:
    print('Levou multa de 3 pontos')
else:
    print('Levou multa de 7 pontos')
