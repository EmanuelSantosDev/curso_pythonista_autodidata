# Dicionários


```python
# trabalha com pares chave x valor
pessoa = {'nome': 'Carol', 'idade': 18, 'altura': 1.60}


# criando um dicionário através da função dict()
pessoa = dict(nome='Emanuel', idade=37, sexo='masculino')
print(pessoa)  # {'nome': 'Emanuel', 'idade': 37, 'sexo': 'masculino'}


# acessando o valor de uma propriedade
print(pessoa['sexo'])  # masculino


# acessando as chaves de um dicionário
chaves = pessoa.keys()
print(chaves)  # dict_keys(['nome', 'idade', 'sexo'])
for k in chaves:
   print(k)  # nome idade sexo


# acessando os valores de um dicionário
valores = pessoa.values()
print(valores)  # dict_values(['Emanuel', 37, 'masculino'])
for valor in valores:
   print(valor)  # Emanuel 37 masculino


# acessando chaves + valores de um dicionário
elementos = pessoa.items()
print(elementos)  
# dict_items([('nome', 'Emanuel'), ('idade', 37), ('sexo', 'masculino')])
for elemento in elementos:
    print(elemento)
    # ('nome', 'Emanuel')
    # ('idade', 37)
    # ('sexo', 'masculino')
    print(elemento[0])
    # nome
    # idade
    # sexo
```