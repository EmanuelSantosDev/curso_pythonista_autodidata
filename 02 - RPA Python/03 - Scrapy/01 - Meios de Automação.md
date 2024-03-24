# Meios de Automação


### PyAutoGUI

**Prós:**
- Fácil de aprender
- Se o ambiente for consistente, os resultados são consistentes
- Pouca manutenção
- Raramente é bloqueado
- Pode ser usado em sistemas web e desktop
- No caso de um executável, não depende da instalação de programas extras para rodar em outro computador

**Contras:**
- Depende da resolução da tela
- Trava o uso do computador
- Mais caro/complexo para hospedar
- Não é ideal para varrer dados de sistema, é usado principalmente para automatizar sistemas


### Selenium

**Prós:**
- Não atrapalha o uso do computador
- Pode ser executado em segundo plano 
- Pode ser hospedado mais facilmente na nuvem (mais barato e escalável)

**Contras:**
- Se o DOM do site mudar, a automação precisa ser atualizada
- Pode ser usado somente em sistemas web
- É um dos mais visados para bloqueio, sendo que é um dos mais utilizados para automações
- Pode ser usado para varrer dados, mas é idealmente usado para automatizar sistemas
- No caso de um executável, depende da instalação de um navegador


### Scrapy

**Prós:**
- Não precisa da instalação de um navegador para rodar
- É mais rápido e leve que o Selenium
- Criado principalmente para varrer dados
- No caso de um executável, ele pode rodar em qualquer computador e sistema operacional

**Contras:**
- Pode ser usando somente em sistemas web