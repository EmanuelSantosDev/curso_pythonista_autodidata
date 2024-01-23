# split() divide uma string em substrings com base em um delimitador específico.


frase = 'Olá, bem-vindo a este treinamento!'

print(frase.split())
# ['Olá,', 'bem-vindo', 'a', 'este', 'treinamento!']
print(frase.split(','))
# ['Olá', ' bem-vindo a este treinamento!']
print(frase.split('-'))
# ['Olá, bem', 'vindo a este treinamento!']


nomes = 'Emanuel, Susi, Yasmin, Rafaela,Samuel'

print(nomes.split())
# ['Emanuel,', 'Susi,', 'Yasmin,', 'Rafaela,Samuel']
print(nomes.split(','))
# ['Emanuel', ' Susi', ' Yasmin', ' Rafaela', 'Samuel']


hashtags = 'music #guitar #gamer #coder #python'
print(hashtags.split())
# ['music', '#guitar', '#gamer', '#coder', '#python']
print(hashtags.split('#'))
# ['music ', 'guitar ', 'gamer ', 'coder ', 'python']
print(hashtags.split('#', 3))
# ['music ', 'guitar ', 'gamer ', 'coder #python']


# join() concatena elementos de uma sequência em uma única string


hashtags_espaco = hashtags.split(' ')
print(hashtags_espaco)
# ['music', '#guitar', '#gamer', '#coder', '#python']


print(','.join(hashtags_espaco))
# music,#guitar,#gamer,#coder,#python
print('.'.join(hashtags_espaco))
# music.#guitar.#gamer.#coder.#python
print(' '.join(hashtags_espaco))
# music #guitar #gamer #coder #python
