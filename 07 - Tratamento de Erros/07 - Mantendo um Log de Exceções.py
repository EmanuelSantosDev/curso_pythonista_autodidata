# Mantendo um Log de Exceções


import logging


logging.basicConfig(level=logging.DEBUG,
                    filename='07 - Tratamento de Erros\\software.log',
                    filemode='a',
                    format='%(levelname)s - %(message)s - %(asctime)s')

email = None

try:
    email = input('Digite seu E-mail: ')
    senha = int(input('Digite sua Senha: '))
    if senha == 1234:
        print('Login feito com sucesso!')
        logging.info(f'{email} - entrou em sua conta bancária')
    else:
        print('Senha inválida')
        logging.info(f'{email} - digitou uma SENHA INVÁLIDA')
except ValueError as erro:
    print('Digite apenas números')
    logging.info(f'{email} - {erro}')
