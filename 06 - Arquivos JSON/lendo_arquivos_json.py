import json


caminho_arquivo_1 = '06 - Arquivos JSON\\usuarios1.json'
caminho_arquivo_2 = '06 - Arquivos JSON\\usuarios2.json'
caminho_arquivo_3 = '06 - Arquivos JSON\\usuarios3.json'
caminho_arquivo_4 = '06 - Arquivos JSON\\usuarios4.json'
caminho_arquivo_5 = '06 - Arquivos JSON\\usuarios5.json'


with open(caminho_arquivo_1, encoding='utf-8') as arquivo_json:
    dados = json.load(arquivo_json)  # convertendo arquivo JSON para Dicionário
    print(dados['nome'])  # Carol


with open(caminho_arquivo_2, encoding='utf-8') as arquivo_json2:
    dados = json.load(arquivo_json2)
    print(dados['permissões'][1])  # intermediário


with open(caminho_arquivo_3, encoding='utf-8') as arquivo_json3:
    dados = json.load(arquivo_json3)
    print(dados['usuários'][1]['permissões'][0])  # basico


with open(caminho_arquivo_4, encoding='utf-8') as arquivo_json4:
    dados = json.load(arquivo_json4)
    print(dados['usuários'][1]['plano']['preco'])  # R$50,00


with open(caminho_arquivo_5, encoding='utf-8') as arquivo_json5:
    dados = json.load(arquivo_json5)
    print(dados[1]['permissões'][1])  # intermediário
