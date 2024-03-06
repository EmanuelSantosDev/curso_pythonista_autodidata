# Click


```python
# Clique na Posição Atual (com botão esquerdo)
pyautogui.click()


# Clique na Posição Atual (personalizando o botão)
pyautogui.click(button='right')
pyautogui.click(button='left')
pyautogui.click(button='middle')


# Forma Mais Usada (acumula os métodos moveTo + click)
pyautogui.click(x=1498, y=442, duration=2)


# Clique Totalmente Personalizado
pyautogui.click(
    x=1498,
    y=442,
    clicks=100,
    interval=0.1,
    button='left',
    duration=2
)


# Clique com Outras Personalizações Pontuais
pyautogui.click(clicks=10)


# Funções Prontas para Cliques
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()
pyautogui.leftClick()
pyautogui.tripleClick()
```