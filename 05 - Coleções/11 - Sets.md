# Sets


- Um conjunto (**set**) é uma coleção não ordenada e mutável de ELEMENTOS ÚNICOS. 
- Os conjuntos são utilizados quando a ordem dos elementos não é importante.
- A principal característica é que eles não permitem elementos duplicados.


```python
frutas = {'maçã', 'uva', 'banana', 'maçã', 'morango', 'banana', 'maçã'}


# Desconsiderou as duplicatas de 'maçã'
print(frutas)  # {'morango', 'maçã', 'banana', 'uva'}


# Adicionando valores
frutas.add('melância')
frutas.add('manga')
print(frutas)  # {'uva', 'maçã', 'manga', 'morango', 'banana', 'melância'}


# Convertendo Listas em Conjuntos
numeros1 = [2, 2, 5, 8]
numeros2 = [2, 2, 3, 9]
a = set(numeros1)
b = set(numeros2)


# Operações sobre Conjuntos
print(a.symmetric_difference(b))  # {3, 5, 8, 9}
print(a.intersection(b))  # {2}
print(a.union(b))  # {2, 3, 5, 8, 9}
```