# Polimorfismo


- Se refere à capacidade de objetos de diferentes classes responderem ao mesmo  método de forma diferente.
- Isso significa que um método pode ter diferentes comportamentos dependendo do tipo do objeto que o está chamando.
- Isso é possível devido à capacidade das subclasses fornecerem implementações específicas para os métodos definidos em suas superclasses.
- Para algo ser polimórfico, ele deve ser capaz de se adaptar ao tipo de dado que está recebendo e pode ser utilizado de maneiras diferentes. 
- O operador ``+`` é um exemplo de polimorfismo, pois podemos passar para ele tanto números, como strings.


## Tipos de Polimorfismo


- **Polimorfismo de Sobrescrita (Overriding)**: ocorre quando uma classe filha redefine um método de sua classe pai.
- **Polimorfismo de Sobrecarga (Overloading)**: não é suportada da mesma forma que em linguagens como Java ou C++, onde você pode ter vários métodos com o mesmo nome, mas diferentes tipos ou números de parâmetros. Porém, podemos simulá-la de algumas maneiras.


### Polimorfismo de sobrescrita
```python
class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print("Au au")

class Gato(Animal):
    def fazer_som(self):
        print("Miau")

# Função que utiliza polimorfismo
def emitir_som(animal):
    animal.fazer_som()

# Criando instâncias das subclasses
cachorro = Cachorro()
gato = Gato()

# Chamando a função com diferentes tipos de objetos
emitir_som(cachorro)  # Output: Au au
emitir_som(gato)      # Output: Miau
```


### Polimorfismo de Sobrecarga (SIMULAÇÃO)


```python
class Calculadora:
    def soma(self, *args):
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return sum(args)

calc = Calculadora()

print(calc.soma(5, 3))         # Output: 8
print(calc.soma(5, 3, 10))     # Output: 18
```