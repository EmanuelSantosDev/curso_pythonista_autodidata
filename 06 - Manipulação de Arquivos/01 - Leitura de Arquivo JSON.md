# Leitura de Arquivo JSON


### Exemplo 1
```python
# app.py
import json


# json.load() é um método que é usado para carregar dados de um arquivo JSON
with open(usuarios.json, encoding='utf-8') as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados['nome'])  # Carol
```
```json
// usuarios.json
{
    "nome": "Carol",
    "telefone": "47-99224-8852",
    "permissões": "basico",
    "admin": true
}
```


### Exemplo 2
```python
# app.py
import json


with open(usuarios.json, encoding='utf-8') as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados['permissões'][1])  # intermediário

missões'][1])  # intermediário
```
```json
// usuarios.json
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


### Exemplo 3
```python
# app.py
import json


with open(usuarios.json, encoding='utf-8') as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados['usuários'][1]['permissões'][0])  # basico
```
```json
// usuarios.json
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
            "admin": true
        },
        {
            "nome": "Douglas",
            "telefone": "47-99224-8852",
            "permissões": [
                "basico",
                "intermediário"
            ],
            "admin": false
        }
    ]
}
```


### Exemplo 4
```python
# app.py
import json


with open(usuarios.json, encoding='utf-8') as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados['usuários'][1]['plano']['preco'])  # R$50,00
```
```json
// usuarios.json
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


### Exemplo 5
```python
# app.py
import json


with open(usuarios.json, encoding='utf-8') as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados[1]['permissões'][1])  # intermediário
```
```json
// usuarios.json
[
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
        "admin": false,
        "plano": {
            "nome": "pro",
            "preco": "R$50,00"
        }
    }
]
```