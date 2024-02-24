# Declaração with


- A declaração ``with`` é usada para garantir a execução segura de código ao trabalhar com recursos que precisam ser liberados ou fechados após o uso, como arquivos, conexões de rede ou conexões de banco de dados. 
- O uso do ``with`` garante que o recurso seja fechado automaticamente quando o bloco with é concluído, mesmo se ocorrerem exceções durante a execução do bloco.


#### Sintaxe Geral:
```python
with expressao as variavel:
    # Código dentro do bloco 'with'
```