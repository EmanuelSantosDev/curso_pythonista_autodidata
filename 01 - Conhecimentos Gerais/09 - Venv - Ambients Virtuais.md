# Venv (Virtual Environment)

O `venv`, abreviação de *virtual environment* (ambiente virtual), é uma ferramenta integrada ao Python que permite criar ambientes isolados para projetos Python. Cada ambiente virtual possui sua própria instalação do Python e suas próprias bibliotecas, permitindo que você mantenha as dependências de diferentes projetos separadas e independentes umas das outras.

## Funcionalidades

- **Isolamento de Ambientes**: Cada ambiente virtual é independente, o que significa que as alterações feitas em um ambiente não afetam outros ambientes ou o sistema operacional em si.
- **Instalação de Dependências**: Você pode instalar pacotes Python em um ambiente virtual usando o pip, sem interferir na instalação global do Python ou em outros ambientes virtuais.

- **Ativação e Desativação Simples**: Os ambientes virtuais podem ser facilmente ativados e desativados, permitindo que você alterne entre diferentes ambientes conforme necessário.

- **Reprodução de Ambientes**: Os ambientes virtuais permitem que você compartilhe facilmente os requisitos de um projeto com outros desenvolvedores, pois você pode fornecer um arquivo `requirements.txt` que lista todas as dependências necessárias.


## Recomendações de Uso


- Crie um novo ambiente virtual para cada projeto Python que você desenvolver.
- Mantenha a lista de dependências atualizada usando um arquivo `requirements.txt`.
- Ative o ambiente virtual sempre que estiver trabalhando em um projeto específico e desative-o quando terminar.
- Em vez de enviar o ambiente virtual para o repositório, você deve adicionar o arquivo ``requirements.txt`` ao seu repositório. Este arquivo contém uma lista das dependências necessárias para o projeto e pode ser usado pelos desenvolvedores para configurar seus próprios ambientes virtuais.


## Alterando a Política de Execução de Scripts no Windows


- **Passo 1**: abrir o **_Windows PowerShell_** no modo **_Administrador_**
- **Passo 2**: digitar o comando `​Set-ExecutionPolicy Unrestricted -Force​`


## Uso Básico


#### Criação de um Ambiente Virtual
```bash
python -m venv nome_do_ambiente
```

#### Ativação do Ambiente Virtual
```bash
nome_do_ambiente\Scripts\activate
```

#### Instalação de Pacotes
```bash
pip install nome_do_pacote
```

#### Gerando o requirements.txt
```bash
pip freeze > requirements.txt
```

#### Desativação do Ambiente Virtual
```bash
deactivate
```

#### Instalando Dependências de um Projeto que contém requirements.txt
```bash
pip install -r requirements.txt
```