# Digitando Textos


### Textos sem Caracteres Especiais
```python
# Digitando textos sem caracteres especiais
pyautogui.typewrite('emanuel@automacao.com.br')
```


### Função de Segurança Integrada
Se o PyAutoGUI está aguardando a movimentação do mouse para terminar de digitar, pode ser devido à sua função de segurança integrada para evitar que scripts automatizados causem danos acidentais. Você pode tentar ajustar o tempo de atraso entre cada caractere digitado usando o parâmetro ``interval`` da função ``pyautogui.typewrite()``: 
```python
pyautogui.typewrite('seu texto aqui', interval=0.1)
```


### Textos com Caracteres Especiais
Para digitação de textos com caracteres especiais vamos utilizar a biblioteca ``pyperclip``:
```python
import pyautogui
import pyperclip


def escrever_frase(frase):
    # Copiando a frase para a área de transferência
    pyperclip.copy(frase)
    # Colando o conteúdo
    pyautogui.hotkey('ctrl', 'v')


# Chamando a função que irá tratar a frase, pois ela contém caracteres especiais
escrever_frase('Olá, seja bem-vindo João!')
```