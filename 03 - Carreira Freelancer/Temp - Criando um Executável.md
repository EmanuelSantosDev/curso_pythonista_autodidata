# Criando um Executável do Selenium


### Instruções para o Usuário Final do Bot:

- Baixar e instalar o Google Chrome
- Passar a pasta que contém o executável para a pessoa responsável pelo bot


### Instalando as Dependências Necessárias


<mark>**Está apresentando erro de compatibilidade com o Python 3.12. Testar com o Python 3.11**</mark>


```bash
pip install cx-freeze
```


### Configurações Iniciais do Projeto


- O **ícone** deve estar salvo em formato ``.ico`` na pasta raíz do programa.
- As configurações serão realizadas em um arquivo chamado ``setup.py``.


### Arquivo de Configurações (setup.py)


```python
from cx_Freeze import setup, Executable


# Lista de arquivos a serem incluídos no executável
arquivos = ['arquivo_exemplo.txt', 'musicas/']

# Configuração para o executável
configuracao = Executable(
    script='app.py',
    icon='meu_bot.ico',
)

# Configuração geral do setup
setup(
    name='Atomatizador de Login',
    version='1.0',
    description='Este programa automatiza o login deste site',
    author='Emanuel dos Santos',
    options={'build_exe': {
        'include_files': arquivos,
        'include_msvcr': True,  # Incluir as DLLs MSVCRT no pacote
    }},
    executables=[configuracao]  # Lista de executáveis a serem criados 
)
```


- **"Incluir as DLLs MSVCRT no pacote"** significa que as bibliotecas MSVCRT serão incluídas no pacote do executável. 
- Essas DLLs são necessárias para que o executável funcione corretamente em sistemas Windows que não tenham as bibliotecas MSVCRT instaladas. 
- Ao incluir essas DLLs no pacote, o executável se torna auto-suficiente e não depende da presença dessas bibliotecas no sistema em que é executado. - Isso garante que o executável possa ser distribuído e executado em diferentes sistemas Windows sem problemas de dependência de bibliotecas.


### Criando o Executável


- Irá gerar a pasta **'build'** que deverá ser entregue ao usuário final.
- Dentro desta pasta estará o arquivo **'.exe'**.
```bash
python .\setup.py build
```


