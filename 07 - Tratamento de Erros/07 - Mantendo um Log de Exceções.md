# Mantendo um Log de Exceções


```python
import logging


logging.basicConfig(level=logging.DEBUG,
                    filename='software.log',
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
```


### software.log


```
INFO - emanuel.santos.developer@gmail.com - entrou em sua conta bancária - 2024-01-27 22:29:14,474
INFO - thalita@escola.com.br - digitou uma SENHA INVÁLIDA - 2024-01-27 22:29:25,851
INFO - antonieta@hotmail.com - invalid literal for int() with base 10: 'trezentosevinte' - 2024-01-27 22:29:41,227
INFO - suelen.borba@bol.com.br - entrou em sua conta bancária - 2024-01-27 22:29:56,309
```