# Tipos de Métodos da Classe


## Métodos Comuns ou Métodos da Instância


- São métodos que acessam as propriedades da instância através do parâmetro ``self``.
- Operam especificamente sobre os dados de uma instância.
- São métodos que pertencem à instância, diferente dos que veremos abaixo, que pertencem à classe.


## Métodos da Classe


- Um método de classe (``@classmethod``) recebe como seu primeiro argumento uma classe (``cls``) ao invés de um objeto (``self``) e pode ser acessado diretamente pela classe, sem a necessidade de criarmos um objeto.
- São úteis em cenários específicos, como por exemplo, quando precisamos alterar a classe em si, criando construtores personalizados (ver exemplo dos computadores abaixo)


## Métodos Estáticos


- Um método estático (``@staticmethod``), não receberá uma classe (``cls``) nem um objeto (``self``) como argumento.
- Assim como no método de classe também podemos acessar esse método diretamente pela classe sem a necessidade de criarmos um objeto.
- São úteis para criar uma classe onde serão agrupadas funcionalidades relacionadas à um tema específico.


```python
class Computador:
    sistema_operacional = 'Windows 11'

    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    # Método Comum (Método da Instância)
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