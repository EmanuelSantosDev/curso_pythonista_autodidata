# Criando Arquivo JSON


- ``json.loads()`` utiliza uma string como entrada convertendo em um Dicionário, diferente de ``json.load()`` que utiliza um arquivo como entrada.
- ``json.dump()`` escreve uma STRING em formato JSON em um arquivo do tipo JSON. Como ele salva a informação em formato de string, é necessário utilizar ambos os métodos, ``json.load()`` e ``json.loads()`` quando for realizada a leitura deste arquivo.


#### app.py
```python
import json


# Convertendo uma string em formato JSON em um Dicionário
string_computador_json = '{"marca": "Dell","preço": 15000}'
dados = json.loads(string_computador_json)
print(dados)  # {'marca': 'Dell', 'preço': 15000}


# Salvando uma String JSON em um Arquivo JSON
with open('computador.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(string_computador_json, arquivo_json)


# Lendo o arquivo criado
with open('computador.json', encoding='utf-8') as arquivo_json:
    dados_string = json.load(arquivo_json)
    dados_dicionario = json.loads(dados_string)
    print(dados_dicionario)  # {'marca': 'Dell', 'preço': 15000}
    print(dados_dicionario['marca'])  # Dell
```


#### computador.json
```json
{
    "marca": "Dell",
    "preço": 15000
}
```