__all__ = ['DB']

try:
    import mysql.connector as myc
    from ..model.config import DB_CONFIG
    from mysql.connector.aio.cursor import MySQLCursor
except ImportError as e:
    print(f'Você não possui os arquivos necessários!\nErro:{e}')

class DB:
    def __init__(self) -> None:
        self.database = myc.connect(**DB_CONFIG)
        self.cursor: MySQLCursor = self.database.cursor()

    def close(self):
        """Fecha a conexão com o banco. Importante para não impedir novas conexões"""
        self.cursor.close()
        self.database.close()

    def f_one(self):
        """Retorna apenas uma linha por vez"""
        return self.cursor.fetchone()
    
    def f_all(self):
        """Retorna todas as linhas"""
        return self.cursor.fetchall()
    
    def f_many(self, quantidade = None):
        """Retorna a quantidade selecionada de linhas por vez"""
        return self.cursor.fetchmany(quantidade)
    
    def exec(self, query:str, args = None):
        """Executa a query"""
        self.cursor.execute(query, params=args)
    def commit(self):
        """Aplica mudanças ao Banco de dados, como insert, update, etc"""
        self.database.commit()

if __name__ == '__main__':
    t = DB()