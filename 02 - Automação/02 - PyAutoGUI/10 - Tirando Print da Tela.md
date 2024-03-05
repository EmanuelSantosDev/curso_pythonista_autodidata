# Tirando Prints da Tela


### Tirando Print da Tela Inteira
```python
pyautogui.screenshot('print_de_tela.jpg')
```

### Tirando Print de Partes Especificas


Sintaxe do Parâmetro ``region()``:
```python
region(eixo x, eixo y, 'x' pixels para a direita, 'x' pixels para baixo)
```

**DICA**: usar a ferramenta de Print Screen para calcular o tamanho dos pixels.

```python
pyautogui.screenshot('calculadora.jpg', region=(992, 63, 321, 530))
```