# Download de Imagens

- <mark>**ATENÇÃO!!! o elemento precisa estar inteiramente visível antes de ser 'printado'!!!**</mark>
- O argumento ``'wb'`` abre o arquivo no modo de escrita binária, pronto para receber dados de imagem:
   - útil para tipos de dados binários como imagens, áudio, etc...
   - não realiza codificação de caracteres.
   - garante que os dados sejam gravados exatamente como são, sem modificações.

```python
# baixando uma imagen única
simbolo_do_gremio = driver.find_element(By.XPATH, "//img[@alt='gremio']")
with open('simbolo.jpg', 'wb') as arquivo:
    arquivo.write(simbolo_do_gremio.screenshot_as_png)


# baixando múltiplas imagens
imagens = driver.find_elements(By.TAG_NAME, 'img')
contador = 1
for imagem in imagens:
    with open(f'imagem{contador}.jpg', 'wb') as arquivo:
        arquivo.write(imagem.screenshot_as_png)
    contador += 1
```