'''
MAGIC METHODS / DUNDER METHODS / DOUBLE UNDERSCORE
==================================================


São métodos em Python que têm nomes especiais e são chamados automaticamente 
em circunstâncias específicas.

Permitem que as classes definam comportamentos personalizados para operações comuns, 
como inicialização de objetos, representação de objetos como strings, comparação de 
objetos e muito mais.

O método '__init__' é um dos métodos mágicos mais comuns e é usado para inicializar 
um objeto quando ele é criado.

O método '__repr__' retorna uma representação oficial do objeto em formato de string. 
Geralmente utilizado para debugging e logging.

O método '__str__' retorna uma representação informal do objeto em formato de string, 
que será chamado sempre que for feito um 'print()' diretamente na instância da classe.

    Em resumo, '__repr__' é mais focado em oferecer uma representação detalhada e 7
    precisa do objeto, enquanto '__str__' é mais focado em oferecer uma representação 
    simplificada.

O método '__len__' indica o que deve ser mensurado para determinar o comprimento
daquela classe quando for utilizada a função 'len()'
'''


class Pessoa:
    def __init__(self):
        self.nome = 'Lucas'
        self.idade = 24
        self.habilidades = ['Andar', 'Correr', 'Nadar']

    def __repr__(self):
        return f'Pessoa(nome={self.nome}, idade={self.idade})'

    def __str__(self):
        return f'{self.nome} tem {self.idade} anos'

    def __len__(self):
        return len(self.habilidades)


pessoa = Pessoa()


# Exibindo a representação oficial do objeto
print(repr(pessoa))  # Pessoa(nome=Lucas, idade=24)

# Exibindo a representação informal do objeto
print(pessoa)  # Lucas tem 24 anos

# Exibindo o comprimento do objeto com base no nº de habilidades
print(len(pessoa))  # 3
