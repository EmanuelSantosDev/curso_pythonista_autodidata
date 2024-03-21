# Exportando para Banco de Dados


### Introdução ao SQLite
- SQLite é um banco de dados leve, embutido e autossuficiente.
- Não requer configuração de servidor ou instalação separada.
- Projetado para ser simples de usar e eficiente em termos de recursos.
- Ideal para aplicativos de desktop, dispositivos móveis e pequenos projetos web.


### Configurando o Arquivo ``pipelines.py``
```python
import sqlite3


# classe que será usada como um pipeline para lidar com a 
# persistência de dados em um banco de dados SQLite
class SQLitePipeline(object):
    # Método chamado quando o spider é aberto
    def open_spider(self, spider):
        # Estabelecendo conexão com o banco de dados SQLite
        self.connection = sqlite3.connect('proxies.db')
        # Criando um cursor para executar comandos SQL
        self.cursor = self.connection.cursor()
        # Criando a tabela 'proxies' se ela ainda não existir
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS proxies(
                ip_address TEXT NOT NULL PRIMARY KEY,
                port NUMBER,
                code TEXT,
                country TEXT,
                anonimity TEXT,
                google TEXT,
                https TEXT,
                last_checked TEXT
            )
        ''')
        # Comitando as alterações no banco de dados
        self.connection.commit()

    # Método chamado quando o spider é fechado
    def close_spider(self, spider):
        # Fechando a conexão com o banco de dados
        self.connection.close()

    # Método chamado para processar cada item extraído pelo spider
    def process_item(self, item, spider):
        # Inserindo o item no banco de dados, ignorando se já existe um 
        # registro com a mesma chave primária
        # VALUES(?,?,?,?,?,?,?,?) são marcadores posicionais que correspondem
        # ao número de valores que serão inseridos na tabela a fim de evitar 
        # uma injeção de SQL
        self.cursor.execute('''
            INSERT OR IGNORE INTO proxies(ip_address,port,code,country,anonimity,google,https,last_checked) VALUES(?,?,?,?,?,?,?,?)
        ''', (
            item.get('ip_address'),
            item.get('port'),
            item.get('code'),
            item.get('country'),
            item.get('anonimity'),
            item.get('google'),
            item.get('https'),
            item.get('last_checked'),
        ))
        # Comitando as alterações no banco de dados
        self.connection.commit()
        # Retornando o item processado para que ele possa continuar 
        # sendo processado pelos outros pipelines, se houver
        return item
```

### Configurando o Arquivo ``settings.py``
```python
ITEM_PIPELINES = {
    "varredor_de_sites.pipelines.SQLitePipeline": 300,
}
```


### Exportando para o Banco de Dados
```
scrapy crawl nome_da_spider
```