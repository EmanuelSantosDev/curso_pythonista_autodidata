# Argumentos Posicionais e Argumentos Nomeados


```python
def exibir_preco(nome_produto, preco):
    print(f'{nome_produto} está no valor de: {preco}')


# Argumentos Posicionais


exibir_preco('Iphone', 5000)


# Argumentos Nomeados (não estão na ordem)


exibir_preco(preco='937', nome_produto='Samsung')


# Obrigando que Todos os Argumentos Devem ser Nomeados a partir do '*'


def exibir_preco_v2(nome_produto, *, preco):
    print(f'{nome_produto} está no valor de: {preco}')


# exibir_preco_v2('Iphone', 5000)
# TypeError: exibir_preco_v2() takes 1 positional argument but 2 were given


exibir_preco_v2('Iphone', preco=5000)
# Iphone está no valor de: 5000
```