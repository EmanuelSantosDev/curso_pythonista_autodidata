# Exportando para Banco de Dados


### Introdução ao SQLite
- SQLite é um banco de dados leve, embutido e autossuficiente.
- Não requer configuração de servidor ou instalação separada.
- Projetado para ser simples de usar e eficiente em termos de recursos.
- Ideal para aplicativos de desktop, dispositivos móveis e pequenos projetos web.


### Configurando o Arquivo ``pipelines.py``
```python
import sqlite3


class SQLitePipeline(object):
    def open_spider(self, spider):
        self.connection = sqlite3.connect('proxies.db')
        self.cursor = self.connection.cursor()
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
        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.cursor.execute('''
            INSERT OR IGNORE INTO proxies(
               ip_address,
               port,
               code,
               country,
               anonimity,
               google,
               https,
               last_checked
            ) VALUES(?,?,?,?,?,?,?,?)''', (
            item.get('ip_address'),
            item.get('port'),
            item.get('code'),
            item.get('country'),
            item.get('anonimity'),
            item.get('google'),
            item.get('https'),
            item.get('last_checked'),
        ))
        self.connection.commit()
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