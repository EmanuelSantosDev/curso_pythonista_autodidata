# Métodos da Classe


```python
class Computador:
   def __init__(self, marca, memoria_ram, placa_de_video):
      self.marca = marca
      self.memoria_ram = memoria_ram
      self.placa_de_video = placa_de_video

   #  Métodos da Classe
   def ligar(self):
      print('Estou ligando o computador')

   def desligar(self):
      print('Estou desligando o computador')

   def exibir_dados_do_computador(self):
      print(f'Computador da marca {self.marca}, com {
            self.memoria_ram} de memória RAM e que usa a placa de vídeo {
            self.placa_de_video}')


computador = Computador('Asus', '32gb', 'NVIDIA')


computador.ligar()
computador.desligar()
computador.exibir_dados_do_computador()
# Estou ligando o computador
# Estou desligando o computador
# Computador da marca Asus, com 32gb de memória RAM e que usa a placa de vídeo NVIDIA
```