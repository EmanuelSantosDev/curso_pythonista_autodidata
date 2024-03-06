# Alertar e Pedir Informações ao Usuário


### Emitindo Alertas para os Usuários
```python
pyautogui.alert(
    text='Inicializando o Bot de Automação',
    title='Automação de Login',
    button='Ok'
)
```


### Solicitando Informações ao Usuário
```python
email = pyautogui.prompt(
    text='Digite seu e-mail',
    title='Informações Obrigatórias'
)
```


### Solicitando Senha para o Usuário
```python
senha = pyautogui.password(
    text='Digite a sua senha:',
    title='Dados de Login',
    mask='*'
)
```


### Solicitando uma Confirmação ao Usuário
```python
resposta = pyautogui.confirm(
    text='Continuar rodando o Bot?',
    title='Confirmação',
    buttons=['Sim', 'Não', 'Cancelar']
)

if resposta == 'Sim':
    print('Codificação para a resposta SIM')
elif resposta == 'Não':
    print('Codificação para a resposta NÃO')
else:
    print('Codificação para a resposta CANCELAR')
```