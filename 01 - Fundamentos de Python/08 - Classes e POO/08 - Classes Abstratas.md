# Classes Abstratas


- São classes que não podem ser instanciadas diretamente, mas servem como modelos para outras classes derivadas. 
- Fornecem uma maneira de definir um contrato comum para várias subclasses, garantindo(e obrigando) que certos métodos sejam implementados por todas elas.
- Elas geralmente contêm métodos abstratos, que são métodos declarados, mas não implementados.
- A biblioteca ``abc`` (Abstract Base Classes) fornece suporte para a criação de classes abstratas. 
- Para definir uma classe abstrata, ela deve herdar a classe ``ABC`` e usar o  decorador ``@abstractmethod`` em seus métodos.


```python
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass


class Cachorro(Animal):
    def fazer_som(self):
        print("Au au")


class Gato(Animal):
    def fazer_som(self):
        print("Miau")


# Não é possível instanciar diretamente uma classe abstrata
animal = Animal() resultaria em um erro


# Instanciando as subclasses
cachorro = Cachorro()
gato = Gato()


# Chamando os métodos das subclasses
cachorro.fazer_som()  # Output: Au au
gato.fazer_som()      # Output: Miau
```