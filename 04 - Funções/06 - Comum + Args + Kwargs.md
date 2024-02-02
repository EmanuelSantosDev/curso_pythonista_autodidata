# Argumento Comum + Args + Kwargs


```python
def fazer_calculo(nome, *args, **kwargs):
    print(nome)  # Emanuel
    print(args)  # (1, 2, 3, 4)
    print(kwargs)  # {'a': 11, 'b': 12, 'c': 13, 'd': 14}
    for arg in args:
        print(arg) # 1 2 3 4
    for kwarg in kwargs.values():
        print(kwarg)  # 11 12 13 14


fazer_calculo('Emanuel', 1, 2, 3, 4, a=11, b=12, c=13, d=14)
```