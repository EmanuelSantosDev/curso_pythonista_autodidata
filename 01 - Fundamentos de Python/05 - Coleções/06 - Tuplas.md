# Tuplas


- É uma estrutura de dados imutável e ordenada.
- Ao contrário das listas, as tuplas não podem ser modificadas após a criação,  o que as torna adequadas para representar coleções de valores constantes, como coordenadas ou informações relacionadas.


```python
sites = ('globo.com', 'youtube.com', 'facebook.com')
valores = (23, 43, 65)


print(sites[1])    # youtube.com
print(valores[2])  # 65


# união de tuplas
dados_unidos = sites + valores
```