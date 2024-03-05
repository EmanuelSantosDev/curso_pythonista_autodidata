# Git


## Configuração Inicial


```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```


Visualizando as configurações:
```bash
git config --global --list
```


## Inicialização e Clonagem


Inicializa um novo repositório Git:
```bash
git init
```


Clona um repositório existente:
```bash
git clone <url_do_repositorio>
```


## Básicos do Dia a Dia


Adiciona alterações dos arquivos à área de staging:
```bash
git add <arquivo>
git add .
```


Confirma as mudanças no repositório local:
```bash
git commit -m "Mensagem do commit"
```


Exibe o status das mudanças como untracked, modified, etc:
```bash
git status
```


## Desfazendo Coisas


Descarta as alterações não confirmadas em um arquivo específico e restaura o estado para o que foi registrado no último commit:
```bash
git checkout <nome_arquivo>
```


Retira o arquivo do Staging:
```bash
git restore --staged <nome_arquivo>
```


Elimina o commit retornando o arquivo para o Staging:
```bash
git reset --soft <hash_do_commit_anterior>
```


Elimina o commit e retorna o arquivo para antes do Staging (modified):
```bash
git reset --mixed <hash_do_commit_anterior>
```


Elimina o commit e tudo o que foi feito nele, inclusive as alterações nos arquivos:
```bash
git reset --hard <hash_do_commit_anterior>
```


## Atualização e Publicação


Envia mudanças locais para o repositório remoto:
```bash
git push
```


Atualiza o repositório local com as mudanças do repositório remoto:
```bash
git pull
```


## Logs e Histórico


Exibe o histórico de commits:
```bash
git log
git log --oneline
```


Exibe as diferenças entre commits, branches, etc:
```bash
git diff
```