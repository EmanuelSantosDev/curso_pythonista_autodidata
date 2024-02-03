# Herança Múltipla

- É um recurso da programação orientada a objetos que permite que uma classe  herde atributos e métodos de mais de uma classe pai. 
- Em outras palavras, uma classe pode herdar características de várias classes pai.
- Oferece grande flexibilidade, permitindo que você reutilize código de várias fontes e crie classes com funcionalidades combinadas de várias classes pai.
- O método ``mro()`` é usado para descobrir qual é a ordem em que as classes são percorridas para resolver a chamada de método ou proprieades em herança múltipla. 
- Havendo classes pai com mesmo atributo e método, o ``mro()`` irá nos mostrar qual é a sequência de prioridade.


```python
class Animal:
    def fazer_som(self):
        print("Som genérico de animal")


class Mamifero:
    def amamentar(self):
        print("Mamífero amamentando")


class Ave:
    def voar(self):
        print("Ave voando")


class Cachorro(Animal, Mamifero):
    def fazer_som(self):
        print("Au au")


class Morcego(Animal, Mamifero, Ave):
    def fazer_som(self):
        print("Eco... eco...")


class Pato(Animal, Ave):
    def fazer_som(self):
        print("Quack quack")


# Criando instâncias das classes
cachorro = Cachorro()
morcego = Morcego()
pato = Pato()


# Chamando métodos das instâncias
cachorro.fazer_som()  # Output: Au au
cachorro.amamentar()  # Output: Mamífero amamentando

morcego.fazer_som()   # Output: Eco... eco...
morcego.voar()        # Output: Ave voando

pato.fazer_som()      # Output: Quack quack
pato.voar()           # Output: Ave voando


# MRO (Method Resolution Order)
print(Morcego.mro())
# [<class '__main__.Morcego'>, <class '__main__.Animal'>,
# <class '__main__.Mamifero'>, <class '__main__.Ave'>, <class 'object'>]
```