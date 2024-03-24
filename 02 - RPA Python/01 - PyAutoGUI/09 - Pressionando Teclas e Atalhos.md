# Pressionando Teclas e Atalhos


### Pressionando Teclas Avulsas
```python
pyautogui.press('tab')
pyautogui.press('space')
pyautogui.press('backspace')

```

### Como Descobrir as Teclas Disponíveis
```python
print(pyautogui.KEYBOARD_KEYS)
```


### Combinando Teclas (hotkey)
```python
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'v')
```


### Combinando Teclas (Forma Antiga)
```python
pyautogui.keyDown('ctrl')
pyautogui.keyDown('a')
pyautogui.keyUp('ctrl')
pyautogui.keyUp('a')
```