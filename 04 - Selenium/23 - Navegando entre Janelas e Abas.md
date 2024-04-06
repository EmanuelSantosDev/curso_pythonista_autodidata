# Navegando entre JANELAS e ABAS


O exemplo abaixo foi feito utilizando **JANELAS**, mas a lógica e o código são os mesmos se estivéssemos utilizando **ABAS**.


```python
# salvando a janela que estamos atualmente
janela_inicial = browser.current_window_handle

# verificando o endereço da janela inicial
print(janela_inicial)  # CBA4EE20E1FEA7CF190311A733285D13

# localizando o botão que abre uma nova janela
botao_abrir_janela = browser.find_element(By.ID, "abrir_janela")

# normalmente o click() padrão não funciona em botões de novas janelas
browser.execute_script('arguments[0].click()', botao_abrir_janela)

# obtendo as janelas que estão abertas atualmente
janelas = browser.window_handles
for janela in janelas:
    print(janela)
    # CBA4EE20E1FEA7CF190311A733285D13
    # 7C667DE732F2839EFF4DD9562E6F1B45

# navegando entre as janelas
for janela in janelas:
    if janela not in janela_inicial:
        # alterando para a nova janela
        browser.switch_to.window(janela)
        '''
        EXECUTAR SCRIPT NA NOVA JANELA
        ''' 
        # fechando a janela atual
        browser.close()

# voltando para a janela inicial
browser.switch_to.window(janela_inicial)
```

#### Exemplo utilizando Abas (mudamos apenas o nome das variáveis):
```python
abas = browser.window_handles

for aba in abas:
    if aba not in janela_inicial:
        browser.switch_to.window(aba)
        # EXECUTAR SCRIPT NA NOVA ABA
        browser.close()

browser.switch_to.window(janela_inicial)
```