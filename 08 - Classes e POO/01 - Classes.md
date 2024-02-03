# Classes


- **Classe** é uma estrutura que serve como um modelo para criar objetos que  compartilham características comuns e comportamentos específicos.
- O método ``__init__`` é também conhecido como construtor e é chamado  automaticamente quando um novo objeto da classe é criado.
- O parâmetro ``self`` é uma referência ao objeto atual. Ele é usado para  acessar e manipular os  atributos e  métodos  do objeto dentro dos métodos  da classe.


```python
class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video


# criando uma instância da classe Computador
computador = Computador('Asus', '8gb', 'NVIDIA')

# imprimindo informações da instância
print(computador.marca)  # Asus
print(computador.memoria_ram)  # 8gb
print(computador.placa_de_video)  # NVIDIA
```