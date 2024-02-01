# split() 


Divide uma string em substrings com base em um delimitador específico:
```python
frase = 'Olá, bem-vindo a este treinamento!'

print(frase.split())  # ['Olá,', 'bem-vindo', 'a', 'este', 'treinamento!']
print(frase.split(','))  # ['Olá', ' bem-vindo a este treinamento!']
print(frase.split('-'))  # ['Olá, bem', 'vindo a este treinamento!']


nomes = 'Emanuel, Susi, Yasmin, Rafaela,Samuel'

print(nomes.split())  # ['Emanuel,', 'Susi,', 'Yasmin,', 'Rafaela,Samuel']
print(nomes.split(','))  # ['Emanuel', ' Susi', ' Yasmin', ' Rafaela', 'Samuel']


hashtags = 'music #guitar #gamer #coder #python'

print(hashtags.split())  # ['music', '#guitar', '#gamer', '#coder', '#python']
print(hashtags.split('#'))  # ['music ', 'guitar ', 'gamer ', 'coder ', 'python']
print(hashtags.split('#', 3))  # ['music ', 'guitar ', 'gamer ', 'coder #python']
```


# join() 


Concatena elementos de uma sequência em uma única string:
```python
palavras = ['music', 'guitar', 'gamer', 'coder', 'python']

print(','.join(palavras))  # music,guitar,gamer,coder,python
print('.'.join(palavras))  # music.guitar.gamer.coder.python
print(' | '.join(palavras))  # music | guitar | gamer | coder | python
```