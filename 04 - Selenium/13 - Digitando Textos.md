# Digitando Textos


```python
# localizando o elemento
campo_nome = browser.find_element(By.ID, 'dadosusuario')

# digitando
campo_nome.send_keys('Emanuel Santos')
```


## Digitando Textos de Forma Humanizada


```python
import random


# guardando o texto em uma variável
texto = '''Lorem ipsum dolor sit amet . Os operadores gráficos e 
tipográficos sabem disso bem, na realidade, todas as profissões que 
lidam com o universo da comunicação têm um relacionamento estável 
com essas palavras, mas o que é? Lorem ipsum é um texto fofo sem 
qualquer sentido.'''


# sleep() com intervalos irregulares simulando uma digitação humanizada
def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1, 5)/30)


# encontrando o campo de texto
campo_de_texto = browser.find_element(
    By.XPATH, "//textarea[@placeholder='digite seu texto aqui']")

# chamando a função que irá digitar o texto de forma humanizada
digitar_naturalmente(texto, campo_de_texto)
```