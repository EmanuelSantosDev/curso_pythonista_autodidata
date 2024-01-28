'''
TIPOS DE VARIÁVEIS DA CLASSE
============================


VARIÁVEIS DA CLASSE - cria um "valor padrão" que pode ser modificado, e assim, 
todas as classes abaixo receberão esta propriedade atualizada)

VARIÁVEIS DA INSTÂNCIA - pertencem exclusivamente à instância
'''


class Computador:
    # Variávies da Classe
    sistema_operacional = 'Windows 11'

    def __init__(self, marca, memoria_ram, placa_de_video):
        # Variávies da Instância
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def exibir_dados_do_computador(self):
        print(f'Computador marca {self.marca}, com {
              self.memoria_ram} de memória RAM, placa de vídeo {
              self.placa_de_video} e sistema operacional {self.sistema_operacional}')


# acessando a propriedade da classe
print(Computador.sistema_operacional)  # Windows 11

# alterando o valor da variável da classe
Computador.sistema_operacional = 'Linux'

# instanciando objeto com novo valor da variável da classe
computador = Computador('DELL', '8gb', 'NVIDIA')
computador.exibir_dados_do_computador()
# Computador marca DELL, com 8gb de memória RAM,
# placa de vídeo NVIDIA e sistema operacional Linux
