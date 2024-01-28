'''
CLASSES 
=======


CLASSE é uma estrutura que serve como um modelo para criar objetos que 
compartilham características comuns e comportamentos específicos.

O método '__init__' é também conhecido como construtor e é chamado 
automaticamente quando um novo objeto da classe é criado.

O parâmetro 'self' é uma referência ao objeto atual. Ele é usado para 
acessar e manipular os  atributos e  métodos  do objeto dentro dos métodos 
da classe.
'''


class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video


# criando instância da classe Computador
computador1 = Computador('Asus', '8gb', 'NVIDIA')

# imprimindo informações da instância
print(computador1.marca)  # Asus
print(computador1.memoria_ram)  # 8gb
print(computador1.placa_de_video)  # NVIDIA
