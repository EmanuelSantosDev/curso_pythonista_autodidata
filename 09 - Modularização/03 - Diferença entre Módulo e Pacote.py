'''
DIFERENÇA ENTRE MÓDULO E PACOTE
===============================


MÓDULO:

* Um módulo é simplesmente um arquivo Python que contém definições de classes, 
funções, variáveis ou outras declarações de código.
* Ele geralmente tem a extensão .py.
* Um módulo pode ser importado em outros arquivos Python para reutilização de código.

PACOTE:

* Um pacote é uma coleção de módulos organizados em um diretório hierárquico.
* Ele também contém um arquivo especial chamado __init__.py, que indica que o 
diretório deve ser tratado como um pacote Python.
* Os pacotes podem conter outros subpacotes, bem como módulos individuais.
* Eles são usados para organizar e modularizar grandes projetos Python, dividindo-os 
em unidades menores e mais gerenciáveis.
'''


# Importando um Pacote


from pacote_teste.modulo2 import nome_do_modulo


nome_do_modulo()  # Sou o Módulo 2 do Pacote de Testes
