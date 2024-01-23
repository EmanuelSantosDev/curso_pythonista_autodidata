# <<< Métodos de Strings >>>


nome_curso = 'Pythonista Autodidata'
frase = '   Frase com Recuos    '


print(nome_curso.upper())
# PYTHONISTA AUTODIDATA

print(nome_curso.lower())
# pythonista autodidata

print(frase.strip())
# Frase com Recuos

print(frase.lstrip())
# Frase com Recuos

print(frase.rstrip())
#    Frase com Recuos

print(nome_curso.find('didata'))
# 15

print(nome_curso.replace('Pythonista', 'Javista'))
# Javista Autodidata

print('Emanuel Joaquim dos Santos'.replace('Joaquim', 'Olivio'))
# Emanuel Olivio dos Santos
