# Criando Arquivo JSON

import json


computador_json = '''{
    "marca": "Dell",
    "preço": 15000
}'''


# json.loads() converte uma string com dados no formato JSON
# em estruturas de dados Python
dados = json.loads(computador_json)
print(dados)  # {'marca': 'Dell', 'preço': 15000}


# Salvando um String JSON -> Arquivo JSON
# json.dump() escreve dados Python em um formato JSON em um arquivo.
with open('06 - Manipulação de Arquivos\\computador.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(computador_json, arquivo_json)


# Lendo o arquivo criado
with open('06 - Manipulação de Arquivos\\computador.json', encoding='utf-8') as arquivo_json:
    dados_formato_string = json.load(arquivo_json)
    dados_formato_dicionario = json.loads(dados_formato_string)
    print(dados_formato_dicionario)  # {'marca': 'Dell', 'preço': 15000}
    print(dados_formato_dicionario['marca'])  # Dell
