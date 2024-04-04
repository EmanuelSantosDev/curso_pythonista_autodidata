# API


APIs são serviços disponibilizados online para acessar recursos ou funcionalidades de uma aplicação web.  

## As APIs possuem 4 partes:

- URL Base
- Endpoint
- Recurso 
- Verbos HTTP

### URL Base
É o prefixo comum de todas as URLs em uma API.
```
http://dummy.restapiexample.com/api/v1
```

### Endpoint
É o sufixo específico que identifica recursos ou operações individuais na API.
```
http://dummy.restapiexample.com/api/v1/employees
http://dummy.restapiexample.com/api/v1/create
http://dummy.restapiexample.com/api/v1/delete/2
```

### Recurso  
Tudo que é retornado ou enviado a uma API é considerado um recurso.


### Verbos HTTP
São métodos de requisição que indicam a ação que deseja ser executada em um recurso web. 
- ``GET`` - obter dados
- ``POST`` - enviar dados
- ``PUT`` - atualizar dados
- ``DELETE`` - excluir dados


#### Códigos de Status HTTP (Status Codes)

São códigos numéricos retornados por um servidor HTTP em resposta a uma requisição, indicando o resultado da operação realizada. É possível visualizá-los na aba **_Network_** do navegador.

- **1xx** - Informativo
  - 100: Continue
  - 101: Mudando Protocolos

- **2xx** - Sucesso
  - 200: OK
  - 201: Criado
  - 204: Sem Conteúdo

- **3xx** - Redirecionamento
  - 301: Movido Permanentemente
  - 302: Encontrado
  - 304: Não Modificado

- **4xx** - Erro do Cliente
  - 400: Solicitação Inválida
  - 401: Não Autorizado
  - 403: Proibido
  - 404: Não Encontrado

- **5xx** - Erro do Servidor
  - 500: Erro Interno do Servidor
  - 502: Gateway Ruim
  - 503: Serviço Indisponível
