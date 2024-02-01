# Random


```python
import random


# gerar valor aleatório de 0.0 a 1.0
print(random.random())  # 0.2324734891891237
print(random.random())  # 0.08105672388048024

# gerar um valor aleatório DECIMAL entre 4 e 10
print(random.uniform(4, 10))  # 5.277825303869222
print(random.uniform(4, 10))  # 7.317717440661163

# gerar um valor aleatório INTEIRO entre 4 e 10
print(random.randint(4, 10))  # 5
print(random.randint(4, 10))  # 9

# sortear valor aleatório
cores = ['verde', 'vermelho', 'azul', 'amarelo', 'lilás']
print(random.choice(cores))  # verde
print(random.choice(cores))  # vermelho

# sortear múltiplos valores aleatórios
print(random.choices(cores, k=2))  # ['azul', 'amarelo']

# embaralhar valores
baralho = ['carta1', 'carta2', 'carta3', 'carta4', 'carta5']
random.shuffle(baralho)
print(baralho)  # ['carta1', 'carta3', 'carta2', 'carta5', 'carta4']
```