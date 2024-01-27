# Criando Arquivos Diversos Vazios


arquivos = ['musica.mp3', 'foto.jpg', 'senhas.txt', 'relatorio.pdf']


for arquivo in arquivos:
    with open('06 - Manipulação de Arquivos\\' + arquivo, 'w') as arquivo:
        pass
