# Função pprint


- ``pprint`` é um módulo que fornece a função ``pprint()`` (**pretty print**), projetada para imprimir estruturas de dados de forma mais legível, especialmente estruturas de dados aninhadas, como dicionários e listas.
- Formata a saída de uma maneira que facilita a leitura e a compreensão, especialmente quando lidamos com estruturas de dados complexas.
- Útil para depuração, visualização de dados e apresentação de resultados em um formato mais legível.


```python
from pprint import pprint


aluno = {
    'nome': 'Alice',
    'idade': 25,
    'curso': 'Engenharia de Software',
    'matricula': '2022001',
    'disciplinas': {
        'Matemática': {'nota': 9.5, 'faltas': 2},
        'Programação': {'nota': 8.0, 'faltas': 0},
        'Banco de Dados': {'nota': 7.5, 'faltas': 1}
    },
    'endereco': {
        'rua': 'Rua das Flores',
        'numero': '123',
        'bairro': 'Centro',
        'cidade': 'Cidade A',
        'estado': 'Estado X',
        'cep': '12345-678'
    },
    'contato': {
        'telefone': '(11) 98765-4321',
        'email': 'alice@example.com'
    }
}


pprint(aluno)
'''
{'contato': {'email': 'alice@example.com', 'telefone': '(11) 98765-4321'},
 'curso': 'Engenharia de Software',
 'disciplinas': {'Banco de Dados': {'faltas': 1, 'nota': 7.5},
                 'Matemática': {'faltas': 2, 'nota': 9.5},
                 'Programação': {'faltas': 0, 'nota': 8.0}},
 'endereco': {'bairro': 'Centro',
              'cep': '12345-678',
              'cidade': 'Cidade A',
              'estado': 'Estado X',
              'numero': '123',
              'rua': 'Rua das Flores'},
 'idade': 25,
 'matricula': '2022001',
 'nome': 'Alice'}
'''
```