# Dicas para XPATH


**Extraindo o Valor do Texto:**
```
//span[@class='text']/text()
```


**Extraindo o Valor do Atributo:**
```
//li/a/@href
```


**Testando o XPATH no Console do Navegador:**
```javascript
$x('//li/a/@href')
```