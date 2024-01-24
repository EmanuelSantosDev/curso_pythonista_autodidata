# Args


# '*args' é uma tupla
def somar(*valores, b):
    print(valores)  # (10, 3, 4, 3)
    for valor in valores:
        b += valor
    print(b)  # 30


somar(10, 3, 4, 3, b=10)
