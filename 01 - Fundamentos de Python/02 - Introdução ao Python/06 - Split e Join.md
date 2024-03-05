# split() 


Divide uma string em substrings com base em um delimitador específico:
```python
# Dividir uma string com base nos espaços entre as palavras:
frase = "Python é uma linguagem de programação"
palavras = frase.split()
print(palavras)  # Saída: ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']


# Dividir uma string com base em um caractere específco:
frase = "Python,Java,C++,JavaScript"
linguagens = frase.split(",")
print(linguagens)  # Saída: ['Python', 'Java', 'C++', 'JavaScript']


# Dividir uma string em um número máximo de partes:
frase = "Python é uma linguagem de programação"
palavras = frase.split(maxsplit=2)
print(palavras)  # Saída: ['Python', 'é', 'uma linguagem de programação']
```


# join() 


Concatena elementos de uma sequência em uma única string:
```python
palavras = ['music', 'guitar', 'gamer', 'coder', 'python']

print(','.join(palavras))  # music,guitar,gamer,coder,python
print('.'.join(palavras))  # music.guitar.gamer.coder.python
print(' | '.join(palavras))  # music | guitar | gamer | coder | python
```