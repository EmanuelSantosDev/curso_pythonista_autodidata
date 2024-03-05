# Funções


```python
# sem parâmetros


def dar_boas_vindas():
    print('Bem-vindo!')

dar_boas_vindas()  # Bem-vindo!


# com parâmetros


def dar_boas_vindas_personalizada(nome):
    print(f'Seja bem-vindo(a) {nome}')

dar_boas_vindas_personalizada('Emanuel')  # Seja bem-vindo(a) Emanuel


# com valor padrão


def nome_cidade(cidade='Porto Alegre'):
    print(f'Você está em {cidade}')

nome_cidade('São Paulo')  # Você está em São Paulo
nome_cidade()  # Você está em Porto Alegre


# sem valor padrão + com valor padrão


def pedir_lanche(quantidade, lanche='Hamburguer'):
    print(f'Você pediu: {lanche} x {quantidade} unidades')

pedir_lanche(3)  # Você pediu: Hamburguer x 3 unidades
pedir_lanche(4, 'Sorvete')  # Você pediu: Sorvete x 4 unidades
```