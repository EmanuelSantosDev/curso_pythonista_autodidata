# Criando Arquivo JSON


```python
# app.py
import json


string_computador_json = '''{
    "marca": "Dell",
    "preço": 15000
}'''


# json.loads() converte uma string com dados 
# no formato JSON em um Dicionário
dados = json.loads(string_computador_json)
print(dados)  # {'marca': 'Dell', 'preço': 15000}


# Salvando uma String JSON em um Arquivo JSON
# json.dump() escreve string de formato JSON em um arquivo
with open('computador.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(string_computador_json, arquivo_json)


# Lendo o arquivo criado
with open('computador.json', encoding='utf-8') as arquivo_json:
    dados_formato_string = json.load(arquivo_json)
    dados_formato_dicionario = json.loads(dados_formato_string)
    print(dados_formato_dicionario)  # {'marca': 'Dell', 'preço': 15000}
    print(dados_formato_dicionario['marca'])  # Dell
```
```json
// computador.json
{
    "marca": "Dell",
    "preço": 15000
}
```