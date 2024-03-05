# Movendo o Mouse e Clicando


```python
import pyautogui  

# Move o cursor do mouse para as coordenadas indicadas 
# em um período de 2 segundos
pyautogui.moveTo(1250, 26, duration=2)

# Move o cursor do mouse em relação à sua posição atual, 
# durante um período de 2 segundos
pyautogui.move(50, -15, duration=2)
```