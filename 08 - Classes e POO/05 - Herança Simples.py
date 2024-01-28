'''
HERANÇA SIMPLES
===============


A herança é um conceito fundamental da programação orientada a objetos, 
que permite que uma classe herde atributos e métodos de outra classe. 

Quando uma classe herda de outra, ela é chamada de "classe filha" ou "subclasse", 
e a classe da qual ela herda é chamada de "classe pai" ou "superclasse".

A principal vantagem da herança é a reutilização de código.

A função 'super' é usada para acessar métodos e atributos da classe pai a partir de 
uma classe filha.

É possível sobrescrever métodos da classe pai.

A função 'issubclass()' é usada para verificar se uma classe é uma subclasse de 
outra classe.
'''


class Camera:
    def __init__(self, marca, megapixels):
        self.marca = marca
        self.megapixels = megapixels

    def tirar_foto(self):
        print(f'Foto tirada com a camera {self.marca} de {
              self.megapixels} megapixels')

    def upar_fotos(self):
        print('Fotos enviadas para o Google Fotos')


class CameraCelular(Camera):
    def __init__(self, marca, megapixels, quantidade_de_cameras):
        super().__init__(marca, megapixels)
        self.quantidade_de_cameras = quantidade_de_cameras

    # método da classe filha
    def aplicar_filtro(self, filtro):
        print(f'Aplicando filtro {filtro}')

    # sobrescrevendo método da classe pai
    def upar_fotos(self):
        print('Fotos enviadas para a Rede Interna')


celular = CameraCelular('Sony', '25mp', 4)

# chamando função da classe filha
celular.aplicar_filtro('AZUL')  # Aplicando filtro AZUL

# chamando função da classe pai
celular.tirar_foto()  # Foto tirada com a camera Sony de 25mp megapixels

# utilizando o método sobrescrito da classe pai
celular.upar_fotos()  # Fotos enviadas para a Rede Interna

# Verificando se uma classe é instância de outra
print(issubclass(CameraCelular, Camera))  # True
print(issubclass(Camera, CameraCelular))  # False
