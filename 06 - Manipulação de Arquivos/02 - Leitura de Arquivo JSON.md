# Leitura de Arquivo JSON


- ``json.load()`` utiliza um arquivo (objeto de arquivo aberto) como entrada.
- Converte os dados em um Dicionário ou uma Lista.


## Exemplo 1


#### app.py
```python
import json

with open(usuarios.json, encoding='utf-8') as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados['nome'])  # Carol
```


#### usuarios.json
```json
{
    "nome": "Carol",
    "telefone": "47-99224-8852",
    "permissões": "basico",
    "admin": true
}
```


## Exemplo 2


#### app.py
```python
import json

with open(usuarios.json, encoding='utf-8') as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados['permissões'][1])  # intermediário

missões'][1])  # intermediário
```


#### usuarios.json
```json
{
    "nome": "Carol",
    "telefone": "47-99224-8852",
    "permissões": [
        "basico",
        "intermediário",
        "administrador"
    ],
    "admin": true
}
```


## Exemplo 3


#### app.py
```python
import json

with open(usuarios.json, encoding='utf-8') as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados['usuários'][1]['plano']['preco'])  # R$50,00
```


#### usuarios.json
```json
{
    "usuários": [
        {
            "nome": "Carol",
            "telefone": "47-99224-8852",
            "permissões": [
                "basico",
                "intermediário",
                "administrador"
            ],
            "admin": true,
            "plano": {
                "nome": "basico",
                "preco": "R$20,00"
            }
        },
        {
            "nome": "Douglas",
            "telefone": "47-99224-8852",
            "permissões": [
                "basico",
                "intermediário"
            ],
            "admin": true,
            "plano": {
                "nome": "pro",
                "preco": "R$50,00"
            }
        }
    ]
}
```