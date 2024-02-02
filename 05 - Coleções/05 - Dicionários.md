# Dicionários


```python
# trabalha com pares chave x valor
pessoa = {'nome': 'Carol', 'idade': 18, 'altura': 1.60}
print(pessoa)  # {'nome': 'Carol', 'idade': 18, 'altura': 1.6}


# utilizando a função dict()
pessoa2 = dict(nome='Emanuel', idade=37, sexo='masculino')
print(pessoa2)  # {'nome': 'Emanuel', 'idade': 37, 'sexo': 'masculino'}


# acessando propriedades específicas
print(pessoa2['sexo'])  # masculino


# descobrindo as chaves disponíveis em um dicionário
chaves = pessoa2.keys()
print(chaves)  # dict_keys(['nome', 'idade', 'sexo'])
for k in chaves:
    print(k)
    # nome
    # idade
    # sexo


# descobrindo os valores disponíveis em um dicionário
valores = pessoa2.values()
print(valores)  # dict_values(['Emanuel', 37, 'masculino'])
for v in valores:
    print(v)
    # Emanuel
    # 37
    # masculino


# descobrindo chaves + valores disponíveis em um dicionário
elementos = pessoa2.items()
print(elementos)  # dict_items([('nome', 'Emanuel'), ('idade', 37), ('sexo', 'masculino')])
for e in elementos:
    print(e)
    # ('nome', 'Emanuel')
    # ('idade', 37)
    # ('sexo', 'masculino')

    # imprimindo somente as chaves
    print(e[0])
    # nome
    # idade
    # sexo
```