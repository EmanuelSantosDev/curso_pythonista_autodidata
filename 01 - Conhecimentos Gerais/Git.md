# Git


## Configuração Inicial


Configuração do Git, como nome de usuário, e-mail, etc.
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```


Visualizando as configurações.
```bash
git config --global --list
```


## Inicialização e Clonagem


Inicializa um novo repositório Git.
```bash
git init
```


Clona um repositório existente.
```bash
git clone <url_do_repositorio>
```


## Básicos do Dia a Dia


Adiciona mudanças ao índice (staging area).
```bash
git add <arquivo>
git add .
```


Registra as mudanças no repositório.
```bash
git commit -m "Mensagem do commit"
```


Exibe o status das mudanças como untracked, modified, etc.
```bash
git status
```


## Atualização e Publicação


Atualiza o repositório local com as mudanças do repositório remoto.
```bash
git pull
```


Envia mudanças locais para o repositório remoto.
```bash
git push
```


## Logs e Histórico


Exibe o histórico de commits.
```bash
git log
```


Exibe as diferenças entre commits, branches, etc.
```bash
git diff
```