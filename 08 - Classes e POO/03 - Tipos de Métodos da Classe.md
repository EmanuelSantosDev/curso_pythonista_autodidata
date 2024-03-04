# Tipos de Métodos da Classe


## Métodos Comuns


- Acessam as propriedades da instância através do parâmetro ``self``.


## Métodos da Classe


- Úteis em cenários específicos, como por exemplo, modificar  como uma classe é instanciada, através de novos construtores personalizados. 
- Exemplos de uso para uma classe de computador:
   - Configuração para Cliente de Escritório
   - Configuração para Clientes de Trabalho Pesado
- Utilizamos o parâmetro ``cls`` por convenção, informando que estamos passando
a classe inteira e não a instância.
- Utilizamos também o decorador ``@classmethod`` para converter uma função em um
método da classe.


## Métodos Estáticos


- São os métodos que não utilizam a instância da classe através do ``self`` e também não modificam as propriedades da classe através do ``cls``. 
- São úteis para criar uma classe onde serão agrupadas funcionalidades relacionadas à um tema específico.
- São configuradas utilizando o decorador ``@staticmethod``.


```python
class Computador:
    sistema_operacional = 'Windows 11'

    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    # Método Comum
    def exibir_dados_do_computador(self):
        print(f'Computador marca {self.marca}, com {
              self.memoria_ram} de memória RAM, {
              self.placa_de_video} e sistema operacional {
               self.sistema_operacional}')

    # Métodos da Classe
    @classmethod
    def computador_escritorio(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Vídeo de Baixo Custo')

    @classmethod
    def computador_trabalho_pesado(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Vídeo Alto Nível')

    # Método Estático
    @staticmethod
    def roda_programas_pesados(memoria_ram):
        if memoria_ram >= 8:
            return True
        else:
            return False


# Instanciando Computadores Personalizados a partir dos Métodos da Classe
computador_backoffice = Computador.computador_escritorio('8gb')
computador_hardcore = Computador.computador_trabalho_pesado('32gb')

computador_backoffice.exibir_dados_do_computador()
# Computador marca Dell, com 8gb de memória RAM, Placa de 
# Vídeo de Baixo Custo e sistema operacional Windows 11

computador_hardcore.exibir_dados_do_computador()
# Computador marca Dell, com 32gb de memória RAM, Placa de 
# Vídeo Alto Nível e sistema operacional Windows 11


# Utilizando o Método Estático
print(Computador.roda_programas_pesados(10))  # True
print(Computador.roda_programas_pesados(4))  # False
```