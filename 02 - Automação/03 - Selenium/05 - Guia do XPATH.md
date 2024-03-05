# Guia do XPATH

- **XPATH** é uma linguagem de consulta usada para selecionar elementos em um documento XML ou HTML.
- ``//`` indica que a busca começa a partir do nó raiz do documento HTML.
- ``/`` indica que o próximo elemento deve ser um filho direto do elemento anterior.

#### Forma mais Comum para se Montar um XPATH (tag + atributo + valor)
```
//tag[@atributo="valor"]
//button[@id="dropdownMenuButton"]  
//section[@class="jumbotron"]       
```

#### Encontrando o Filho Direto
```
//div/fieldset
//div/fieldset/h4
//div[@id="select-class-example"]/fieldset/h4
```

#### Encontrando o Filho Direto pelo Índice
```
//thead/tr/th[2]
```

#### Ultra Genérico (engloba todas os elementos da página)
```
//* 
```

#### Ultra genérico + Tag (seleciona todos os elementos que contém esta tag)
```
//*[tag]
```

#### Tag
```
//tag
```

#### Buscando por um Texto Espefícico
```
//*[text()="Exemplo Checkbox"]      # Genérico, porém especificando o texto
//h4[text()="Exemplo Checkbox"]     # Com tag e especificando o texto
```

#### Contém uma Parte do Texto
```
//*[contains(text(),"Exemplo")] 
//*[contains(text(),"Exemplo") or contains(text(), "Dropdown")]
//*[contains(text(),"Dropdown") and contains(text(), "Bootstrap")]
```

#### Inicia com um Texto Específico
```
//*[starts-with(text(), "Exemplo")]
//*[starts-with(@class, "btn")]
```