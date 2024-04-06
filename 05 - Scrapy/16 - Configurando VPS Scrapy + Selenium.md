# Configurando VPS Scrapy + Selenium


Os passos são muito semelhantes à configuração padrão para o Scrapy, porém, com a adição da instalação do **Google Chrome**. 


## Verificando Instalação do Python


```
python3 --version
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
pip3 install scrapy selenium
```


## Rodando a Aplicação 


```
scrapy crawl nome_do_bot -O dados.csv
```


## Visualizando o Arquivo no Terminal


```
cat dados.csv
```


## Exportando o Arquivo Gerado para o Computador


**Na VPS:**
```
git status
git add .
git commit -m "mensagem"
git push
```


**No computador local:**
```
git pull
```