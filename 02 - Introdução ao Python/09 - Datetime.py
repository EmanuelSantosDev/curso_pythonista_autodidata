# Datetime


from datetime import datetime

print(datetime.now())  # 2024-01-22 23:13:33.675344
print(datetime.now().day)  # 22
print(datetime.now().month)  # 1
print(datetime.now().year)  # 2024


# Criando uma Data


data_nascimento = datetime(1986, 6, 2)
print(data_nascimento)  # 1986-06-02 00:00:00


# Usuário Definindo uma Data


data_nasc = datetime.strptime(
    input('Digite sua data de nascimento: '), '%d/%m/%Y')

print(type(data_nasc))  # <class 'datetime.datetime'>
print(data_nasc)  # 1986-06-02 00:00:00


# Calculando Intervalo entre Datas


intervalo = datetime.now() - data_nasc
print(intervalo.days)  # 13748
