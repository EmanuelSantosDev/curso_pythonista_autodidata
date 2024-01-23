from datetime import datetime
import random


nome = input('Digite seu NOME: ')
idade = int(input('Digite sua IDADE: '))
data_cadastro = datetime.now()
dia = data_cadastro.day
mes = data_cadastro.month
ano = data_cadastro.year
cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
cartao_sorteado = random.choice(cartoes)
data_aniversario = datetime.strptime(
    input('Digite sua DATA DE NASCIMENTO [dd/mm/aaaa]: '), '%d/%m/%Y')


print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {
      dia}/{mes}/{ano}.')
print(f'Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {
      cartao_sorteado}.')
