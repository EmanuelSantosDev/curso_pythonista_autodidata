# VPS Selenium


## Configurações do Selenium


```python
arguments = ['--lang=en-US', '--window-size=1920,1080',
            '--incognito', '--disable-gpu', '--no-sandbox', '--headless', '--disable-dev-shm-usage']
```


## Atualizando os Pacotes do Sistema Operacional


Atualizando a LISTA DE PACOTES do Sistema Operacional:
```
sudo apt-get update -y
```

Atualizando os PACOTES do Sistema Operacional:
```
sudo apt-get upgrade -y
```


## Instalando o GIT 


```
sudo apt-get install git
```


## Instalando o Google Chrome


```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```


#### Corrigindo Dependências Quebradas:


```
sudo apt-get install -f
```


#### Excluindo o Pacote de Instalação do Google Chrome:
```
rm -rf google-chrome-stable_current_amd64.deb
```


## Transferindo o Projeto para a VPS


```
git clone <endereço-https-repositório>
``` 
Poderá solicitar:
- **User Name Github:** _EmanuelSantosDev_
- **Password Github:** _Github > Perfil > Settings > Developer settings > Personal access tokens > Tokens (classic) > Generate new token > Generate new token (classic) > Dar um Nome ao Token > No expiration > Marcar Todos os Acessos > Generate token > Salvar o Token em um Local Seguro_


## Criando o Ambiente Virtual


```
python3 -m venv <nome-do-ambiente>
```

- O terminal poderá irá sugerir uma linha de comando para baixar a biblioteca necessária para a criação de um ambiente virtual.
- Utilizar o comando `sudo` antes desta linha indicada.
- Após isso repita o comando para criação do ambiente virtual.


```
python3 -m venv <nome-do-ambiente>
```


## Ativando o Ambiente Virtual


```
source <nome-do-ambiente>/bin/activate
```


## Instalando as Bibliotecas do Projeto


```
pip3 install selenium webdriver-manager
```


## Rodando a Aplicação


```
python3 app.py
```


## Encerrando a Aplicação


```
ctrl + c
```


## Executando Múltiplos Programas (Terminal Desbloqueado)


- ``nohup``: permite que o processo continue em execução mesmo que você feche o terminal ou deslogue.
- ``&``: coloca o comando anterior (no caso, python3 app.py) em segundo plano, permitindo que você continue usando o terminal enquanto o processo está em execução.
- retornará um número de ``id`` que é essencial para identificar o processo (bot) rodando no sistema. 
- cria um arquivo chamado ``nohup.out`` que armazena qualquer saída que normalmente seria exibida no terminal e é útil para verificar mensagens de erro ou outras informações de diagnóstico.

```
nohup python3 app.py &
```


## Verificando o arquivo ``nohup.out``


```
cat nohup.out
```


## Encerrando o Processo Através do Gerenciador de Tarefas


```
htop
```

- Localizar o processo em execução
- ``F9`` (kill) + ``Enter``



## Desativando o Ambiente Virtual


```
deactivate
```


## Deslogando do Servidor Remoto


```
exit
```