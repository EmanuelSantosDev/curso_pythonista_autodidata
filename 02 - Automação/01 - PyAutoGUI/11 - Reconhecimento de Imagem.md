# Reconhecimento de Imagem


- o PyAutoGUI realiza o reconhecimento de imagens simples
- ao tirar print, tenha em mente que as imagens não podem ser complexas
- salve as imagens na extensão **PNG**


### Capturando as Coordenadas do Box da Imagem
```python
coordenadas = pyautogui.locateOnScreen('numero_8.png')
print(coordenadas)  # Box(left=1024, top=409, width=71, height=48)
```
 
### Capturando as Coordenadas do Centro da Imagem
```python
coordenadas = pyautogui.locateCenterOnScreen('numero_8.png')
print(coordenadas)  # Point(x=1059, y=433)

# Movendo o Mouse para as Coordenadas Correspondentes
pyautogui.click(coordenadas[0], coordenadas[1], duration=2)
```