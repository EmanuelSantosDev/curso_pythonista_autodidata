# Try Except


- Usar ``except`` sem uma exceção específica significa que este bloco  será executado para qualquer exceção que ocorra no bloco ``try``.
- Embora isso possa lidar com qualquer exceção que ocorra, é uma prática  recomendada capturar exceções específicas sempre que possível para lidar  com elas de maneira mais apropriada.


```python
try:
    valor = float(input('Digite o valor em Dólares: '))
    print(valor * 5.25)
except:
    print('Favor digitar apenas números')
```