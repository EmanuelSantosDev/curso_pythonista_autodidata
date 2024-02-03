# Herança Multinível


- EVITE Herança Multinível!!!
- O excesso de níveis é igual a alta complexidade, porque o nível abaixo depende das regras dos níveis superiores.


```python
class Veiculo:
    pass

class VeiculodeRodas(Veiculo):  
    pass

class Carro(VeiculodeRodas):
    pass

class CarroEletrico(Carro):
    pass
   
class CarroEletricoDuasPortas(CarroEletrico):
    pass
```