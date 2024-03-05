# Verificando a Cor do Pixel


- A função ``pixelMatchesColor()`` é uma função da biblioteca PyAutoGUI que permite verificar se a cor de um pixel em uma determinada posição na tela corresponde a uma cor específica.
- Se a cor do pixel nessas coordenadas corresponder à cor especificada dentro da tolerância fornecida, a função retorna ``True``, indicando que a cor corresponde. Caso contrário, retorna ``False``.


```python
# Sintaxe 
pyautogui.pixelMatchesColor(x, y, (r, g, b), tolerance=0)
```

- ``x``: a coordenada **x** do pixel na tela.
- ``y``: a coordenada **y** do pixel na tela.
- ``(r, g, b)``: uma tupla contendo os valores de vermelho, verde e azul da cor a ser verificada.
- ``tolerance``: uma tolerância opcional para permitir pequenas diferenças nas cores. O valor padrão é **0**, o que significa que as cores devem corresponder exatamente.


## Exemplos:


```python
# sem tolerância
x = pyautogui.pixelMatchesColor(1114, -266, (0, 152, 0))

# com tolerância
y = pyautogui.pixelMatchesColor(300, 300, (0, 255, 0), tolerance=50)
```