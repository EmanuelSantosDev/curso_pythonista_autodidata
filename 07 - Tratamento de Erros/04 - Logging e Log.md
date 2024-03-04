# Logging


- **Logging** é uma forma de documentar o que já aconteceu e o que está acontecendo  na aplicação.
- Maneira flexível de armazenar mensagens de registro em diferentes níveis de gravidade.


## Níveis de Logging


- ``debug`` - quando quero passar informações para os desenvolvedores. Geralmente úteis apenas durante o desenvolvimento e depuração do código.
- ``info`` - quando quero informar algo que está acontecendo no programa, mas não é um erro. Exemplos: inicialização bem-sucedida, conclusão de tarefas, etc.
- ``warning`` - quando quero alertar algo que está acontecendo, possivelmente fora do esperado, porém, ainda não é um erro, mas pode gerar futuramente.
- ``error`` - um erro que ocorreu na aplicação.
- ``critical`` - um erro com consequências graves.


# Gerando um Log


```python
import logging


logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    filemode='a',
                    format='%(levelname)s - %(message)s - %(asctime)s')

email = None

try:
    email = input('Digite seu E-mail: ')
    senha = int(input('Digite sua Senha: '))
    if senha == 1234:
        print('Login feito com sucesso!')  # Output Usuário
        logging.info(f'{email} - entrou em sua conta bancária')  # Output Log
    else:
        print('Senha inválida')  # Output Usuário
        logging.info(f'{email} - digitou uma SENHA INVÁLIDA')  # Output Log
except ValueError as erro:
    print('Digite apenas números')  # Output Usuário
    logging.error(f'{email} - {erro}')   # Output Log
```


### Saída no Arquivo app.log


```
INFO - emanuel.santos.developer@gmail.com - entrou em sua conta bancária - 2024-01-27 22:29:14,474
INFO - thalita@escola.com.br - digitou uma SENHA INVÁLIDA - 2024-01-27 22:29:25,851
ERROR - antonieta@hotmail.com - invalid literal for int() with base 10: 'trezentosevinte' - 2024-01-27 22:29:41,227
INFO - suelen.borba@bol.com.br - entrou em sua conta bancária - 2024-01-27 22:29:56,309
```