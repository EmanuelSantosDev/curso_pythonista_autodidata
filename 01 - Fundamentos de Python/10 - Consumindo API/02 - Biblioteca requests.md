# Biblioteca ``requests``


- A biblioteca ``requests`` é uma biblioteca HTTP elegante e simples para Python, projetada para tornar o trabalho com solicitações HTTP fácil e intuitivo.
- Suporte a métodos HTTP como GET, POST, PUT, DELETE, etc.


## Instalação 


```
pip install requests
```


## Como Usar os 4 Principais Verbos HTTP


- Site utilizado para os testes: [JSONPlaceholder](https://jsonplaceholder.typicode.com/).
- A função ``.json()`` é um método da biblioteca ``Requests`` que é usado para decodificar o conteúdo de uma resposta HTTP no formato JSON para um objeto Python. 

```python
import requests
from pprint import pprint


#  GET 


resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
print(resultado_get)  # <Response [200]>
pprint(resultado_get.json())  # Resposta no formato dicionário de todos os itens


#  GET com ID 


resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos/2')
print(resultado_get)  # <Response [200]>
pprint(resultado_get.json())  # Resposta no formato dicionário de um único item


#  POST 


novo_recurso = {
    'completed': True,
    'title': 'Cortar a Grama no Domingo',
    'userId': 1
}

resultado_post = requests.post(
    'https://jsonplaceholder.typicode.com/todos', novo_recurso)

print(resultado_post)  # <Response [201]>

pprint(resultado_post.json())
'''
{'completed': 'True',
 'id': 201,
 'title': 'Cortar a Grama no Domingo',
 'userId': '1'}
'''


#  PUT 


recurso_alteracao = {
    'completed': False,
    'title': 'Passear com o Cachorro',
    'userId': 3
}

resultado_put = requests.put(
    'https://jsonplaceholder.typicode.com/todos/5', recurso_alteracao)

print(resultado_put)  # <Response [200]>

pprint(resultado_put.json())
'''
{'completed': 'False',
 'id': 5,
 'title': 'Passear com o Cachorro',
 'userId': '3'}
'''


#  DELETE 


resultado_delete = requests.delete(
    'https://jsonplaceholder.typicode.com/todos/11')
print(resultado_delete)  # <Response [200]>
print(resultado_delete.json())  # {}

```