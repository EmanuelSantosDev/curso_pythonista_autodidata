#  Capturando a Posição do Mouse


Todas as operações abaixo são realizadas no Terminal.


### Iniciando o Interpretador Python
```bash
python
```


### Capturando a Coordenada Atual
```bash
import pyautogui
pyautogui.position()
```


### Capturando Coordenadas em Tempo Real
```bash
pyautogui.displayMousePosition()
```


### Forma Mais Útil para Registrar as Coordenadas
Utilizamos a biblioteca **mouseinfo**:
```bash
from mouseinfo import mouseInfo
mouseInfo()
```
- Desmarcar a opção **3 Sec. Button Delay**.
- Utilizar o atalho ``F6`` para ir registrando as coordenadas.