# Pausas com WAIT IMPLÍCITO


- As **esperas implícitas** são técnicas para instruir o WebDriver a esperar um determinado período de tempo antes de lançar uma exceção indicando que um elemento não foi encontrado na página.
- O método ``implicitly_wait(x)`` define um tempo de espera implícito.
- Ajuda a tornar os scripts mais resilientes a atrasos na renderização da página ou problemas de conectividade de rede.


```python
driver = iniciar_driver()

# configuramos logo depois da inicialização do driver
driver.implicitly_wait(10)
```