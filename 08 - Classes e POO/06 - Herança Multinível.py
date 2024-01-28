# Herança Multinível


# EVITE Herança Multinível!!!
# Vários níveis de herança é igual a alta complexidade, porque
# o nível abaixo depende das regras dos níveis acima


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