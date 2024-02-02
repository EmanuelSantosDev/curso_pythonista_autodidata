'''
# Log e Logging


- **Logging** é uma forma de documentar o que já aconteceu e o que está acontecendo  na aplicação.
- Maneira flexível de armazenar mensagens de registro em diferentes níveis de gravidade.


## Níveis de Logging


- ``debug`` - quando quero passar informações para os desenvolvedores. Geralmente úteis apenas durante o desenvolvimento e depuração do código.
- ``info`` - quando quero informar algo que está acontecendo no programa, mas não é um erro. Exemplos: inicialização bem-sucedida, conclusão de tarefas, etc.
- ``warning`` - quando quero alertar algo que está acontecendo, possivelmente fora do esperado, porém, ainda não é um erro, mas pode gerar futuramente.
- ``error`` - um erro que ocorreu na aplicação.
- ``critical`` - um erro com consequências graves.

## Padrão do Módulo Logging


- Por padrão, o módulo ``logging`` irá exibir apenas as mensagens de ``warning`` 'para cima'.
- Para alterar este comportamento padrão utilizamos a função ``basicConfig``.


```python
# importando o módulo logging
import logging


# configurando o nível de logging para DEBUG
logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    filemode='a',
                    format='%(levelname)s - %(message)s')


logging.debug('Logging no nível debug')
logging.info('Logging no nível info')
logging.warning('Loggin no nível warning')
logging.error('Logging no nível error')
logging.critical('Logging no nível critical')
```


### app.log


```
DEBUG - Logging no nível debug
INFO - Logging no nível info
WARNING - Loggin no nível warning
ERROR - Logging no nível error
CRITICAL - Logging no nível critical
```