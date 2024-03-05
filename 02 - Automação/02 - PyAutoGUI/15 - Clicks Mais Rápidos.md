# Clicks Mais Rápidos


- A função `click()` do PyAutoGUI é lenta para automações que exijam velocidade.
- Como alternativa temos a biblioteca `pywin32`.


## O que é PyWin32


É uma extensão Python que fornece acesso à API do Windows, permitindo que os desenvolvedores criem aplicativos que interajam com o sistema operacional Windows.


### Instalação


```bash
pip install pywin32
```


### Clicks mais Rápidos


Exemplo extraído do bot do game **Piano Titles**:
```python
import pyautogui
import keyboard
import win32api # Importa o módulo win32api para interagir com o sistema Windows
import win32con # Importa o módulo win32con para acessar constantes do Windows
from time import sleep


# aperta o botão 'START'
pyautogui.click(1405,-562, duration=2)


# usando a biblioteca 'pywin32' para efetuar o click rapidamente
def click_rapido(x, y):
   # Define a posição do cursor do mouse para as coordenadas (x, y)
   win32api.SetCursorPos((x, y))
   # Simula o pressionamento do botão esquerdo do mouse na posição atual
   win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
   sleep(0.05)
   # Simula a liberação do botão esquerdo do mouse na posição atual
   win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# pausa o game quando o usuário apertar a tecla '1'
while keyboard.is_pressed('1') == False:
   # mapeando cada uma das 4 teclas do game
   if pyautogui.pixelMatchesColor(1256, -505, (0, 0, 0)):
      click_rapido(1256, -505)
   if pyautogui.pixelMatchesColor(1360, -507, (0, 0, 0)):
      click_rapido(1360, -507)
   if pyautogui.pixelMatchesColor(1444, -507, (0, 0, 0)):
      click_rapido(1444, -507)
   if pyautogui.pixelMatchesColor(1536, -489, (0, 0, 0)):
      click_rapido(1536, -489)
```