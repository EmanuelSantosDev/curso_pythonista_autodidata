# Iniciando e Encerrando um Bot Selenium


### driver.get()
- Navega para uma URL específica.
- Utilizado para iniciar a automação navegando para a página inicial de um site ou para qualquer outra página específica que deseje testar.
```python
driver.get('https://www.exemplo.com')
```


### driver.quit()
- Encerra a sessão do WebDriver e fechar todas as janelas abertas.
- Útil quando você terminou de interagir com todas as janelas e deseja encerrar completamente a sessão do WebDriver.
```python
driver.quit()
```


### driver.close()
- Fechar a janela atualmente ativa no navegador.
- Útil quando você deseja fechar uma única janela, mas manter outras janelas abertas na mesma sessão do WebDriver.
```python
driver.close()
```