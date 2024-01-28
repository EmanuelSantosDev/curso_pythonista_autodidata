# Múltiplas Exceções


try:
    divisor = int(input('Digite um Divisor: '))
    print(10 / divisor)
except ZeroDivisionError as erro:
    print('Não é possível dividir por Zero')
except ValueError as erro:
    print('Digite um número válido')
finally:
    print('Programa Encerrado')
