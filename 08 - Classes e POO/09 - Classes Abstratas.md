# Classes Abstratas


- São classes que não podem ser instanciadas diretamente, mas são projetadas  para serem subclasses de outras classes
- Fornecem uma maneira de definir um contrato comum para várias subclasses,  garantindo(e obrigando) que certos métodos sejam implementados por todas elas.
- Uma classe abstrata pode conter métodos abstratos, que são métodos sem  implementação definida na classe abstrata, mas que devem ser implementados  pelas subclasses.
- A biblioteca ``abc`` (Abstract Base Classes) fornece suporte para a criação de classes abstratas. 
- Para definir uma classe abstrata, você pode herdar da classe ``ABC`` e usar o  decorador ``@abstractmethod``.


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
# animal = Animal() resultaria em um erro


# Instanciando as subclasses
cachorro = Cachorro()
gato = Gato()


# Chamando os métodos das subclasses
cachorro.fazer_som()  # Output: Au au
gato.fazer_som()      # Output: Miau
```