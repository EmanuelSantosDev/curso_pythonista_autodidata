# Salvar Informações em Arquivo

### As 4 Operações Básicas:

- ``r`` - Leitura
- ``w`` - Escrita (apaga e reescreve se houver sobreposição)
- ``r+`` - Leitura e Escrita
- ``a`` - Acrescentar

### Módulo ``os``

O módulo ``os`` fornece uma interface para interagir com o sistema operacional para: 

- manipulação de arquivos
- leitura
- definição de variáveis de ambiente
- operações de diretório
- entre outras.

### Instruções Importantes

- ``newline=''``: garante que o Python não adicione ou converta automaticamente os  caracteres de nova linha, deixando o controle da formatação de linha totalmente  nas mãos do programador.
- ``os.linesep``:  é uma constante definida no módulo ``os`` que representa o caractere de fim de linha do sistema operacional atual garantindo que suas strings tenham  o caractere de fim de linha apropriado.


```python
import os


# Escrita (w)
with open('celulares.txt', 'w') as arquivo:
    arquivo.write('Celular 1')


# Acrescentar (a)
nomes = ['Emanuel', 'Amanda', 'Susi', 'Roberto', 'Tiago']

with open('nomes.txt', 'a', newline='') as arquivo:
    for nome in nomes:
        arquivo.write(nome + os.linesep)


# Números precisam ser convertidos para Strings
numeros = [1, 2, 3, 4, 5, 6]

with open('numeros.txt', 'a', newline='') as arquivo:
    for n in numeros:
        arquivo.write(str(n) + os.linesep)


# Leitura (r)
with open('nomes.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)


# Leitura e Escrita (r+)
with open('nomes.txt', 'r+', newline='') as arquivo:
    for linha in arquivo:
        print(linha)
    arquivo.write('América do Sul' + os.linesep)
    arquivo.write('São João' + os.linesep)
```