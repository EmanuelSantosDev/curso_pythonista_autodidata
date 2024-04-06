# Encontrando Elementos


#### find_element() 

- É usado para encontrar o primeiro elemento correspondente ao seletor fornecido no DOM.
- Se nenhum elemento corresponder ao seletor fornecido, o método lançará uma exceção ``NoSuchElementException``.

```python
# Sintaxe Básica
find_element(seletor)
```

#### find_elements()

- Retorna uma lista de todos os elementos correspondentes encontrados no DOM.
- Se nenhum elemento corresponder ao seletor fornecido, ele retorna uma **lista vazia**. 

```python
# Sintaxe Básica
find_elements(seletor)
```


## Identificadores de Localização (classe By)


Importando a classe ``By``:
```python
from selenium.webdriver.common.by import By
```


#### Identificador de ID
```python
elemento = browser.find_element(By.ID, 'buttonalerta')
```


#### Identificador de NAME
```python
campo_nome = browser.find_element(By.NAME, 'seu-nome')
```


#### Identificador de CLASS NAME
```python
elemento = browser.find_element(By.CLASS_NAME, 'navbar-brand')
```


#### Identificador de TEXTO em LINK
```python
# encontrando pelo texto completo
link_home = browser.find_element(By.LINK_TEXT, 'Home')

# encontrando por uma parte do texto
link_desafio = browser.find_element(By.PARTIAL_LINK_TEXT, 'Des')
```


#### Identificador de TAG
```python
titulo = browser.find_element(By.TAG_NAME, 'h1')
```


#### Identificador de XPATH
```python
titulo = browser.find_element(By.XPATH, '//*[text()="ZONA DE TESTES"]')
```


#### Identificador de SELETOR CSS
```python
elemento_h2 = browser.find_element(By.CSS_SELECTOR,'h2')
elementos_form_chec = browser.find_element(By.CSS_SELECTOR,'input[class="form-check-input"]')
```


## Elementos Escondidos e Elementos Dinâmicos


- Alguns elementos podem precisar de alguma interação prévia antes que os mesmos fiquem disponíveis na Tela ou no DOM.
- Elementos com um estilo CSS `style="display: none;"` ficam visíveis no DOM, mas estão **"escondidos"** na tela até que alguma interação seja realizada.
- Em contrapartida há outros elementos que são **criados dinamicamente** no DOM, conforme interações do usuário. 