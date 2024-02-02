# Operadores Boleanos


```python
idade = 21
possui_convite = False
filho_do_dono = True


# operador 'and'
print(idade >= 21 and possui_convite == True) # False


# operador 'or'
print(idade >= 21 or possui_convite == True) # True


# maior de 21 'E' possui convite 'OU' seja filho do dono
print(idade >= 21 and possui_convite or filho_do_dono) # True


# operador 'not'
possui_carteira_trabalho = True
possui_veiculo_proprio = False
print(possui_carteira_trabalho and not possui_veiculo_proprio) # True
```