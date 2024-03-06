# Pausas com SLEEP


É útil em situações que:
- não necessariamente estamos aguardando o elemento carregar na página.
- precisamos ser lentos (não ser detectado como bot).
- queremos visualizar melhor a execução dos passos.


```python
from time import sleep
sleep(10)
```