__all__ = ['Livro', 'LivroBuilder']

class Livro:
    def __init__(self) -> None:
        self._id_livro = None
        self._titulo: str = ''
        self._autor: str = ''
        self._genero: str = ''
        self._isbn: str = ''
        self._status: int = None #1:disponivel,2-emprestado,3-extraviado,4-danificado

    def setId(self, id: int):
        if(type(id) != int):
            raise TypeError('Tipo esperado: int')
        if(id <= 0):
            raise ValueError('ID não pode ser menor ou igual a Zero')
        
        self._id_livro = id

    def setTitulo(self, titulo: str):
        if(type(titulo) != str):
            raise TypeError('Tipo esperado: str')
        if(titulo == ''):
            raise ValueError('Valor não pode ser vazio')

        self._titulo = titulo

    def setAutor(self, autor: str):
        if(type(autor) != str):
            raise TypeError('Tipo esperado: str')
        if(autor == ''):
            raise ValueError('Valor não pode ser vazio')

        self._autor = autor

    def setGenero(self, genero: str):
        if(type(genero) != str):
            raise TypeError('Tipo esperado: str')
        if(genero == ''):
            raise ValueError('Valor não pode ser vazio')

        self._genero = genero

    def setIsbn(self, isbn: str):
        if(type(isbn) != str):
            raise TypeError('Tipo esperado: str')
        if(isbn == ''):
            raise ValueError('Valor não pode ser vazio')

        self._isbn = isbn

    def setStatus(self, status: int = 1):
        """Status do livro são: 1:disponivel, 2:emprestado, 3:extraviado, 4:danificado"""
        if(type(status) != int):
            raise TypeError('Tipo esperado: int')
        if(status < 1 or status > 4):
            raise ValueError('Valor precisa ser [1,4]')

        self._status = status

    def getId(self) -> int:
        return self._id_livro

    def getTitulo(self) -> str:
        return self._titulo

    def getAutor(self) -> str:
        return self._autor

    def getGenero(self) -> str:
        return self._genero

    def getIsbn(self) -> str:
        return self._isbn

    def getStatus(self) -> int:
        return self._status

    def getAsDB(self) -> tuple:
        return (self._titulo, self._autor, self._genero, self._isbn, self._status)

    @staticmethod
    def createQuery() -> str:
        """Adiciona um novo livro ao banco de dados"""
        return """
                insert into livro
                    (titulo, autor, genero, isbn, status_livro)
                    values (%s,%s,%s,%s,%s)
                """
    
    @staticmethod
    def selectQuery(id_livro:bool|None = False, titulo:bool|None = False, autor:bool|None = False, genero:bool|None = False, isbn:bool|None = False, status_livro:bool|None = False) -> str:
        """
        Gera o query para ler os livros, aplicando os filtros dados pelos argumentos verdadeiros no método.
        Example:
            select * from livro where titulo=%s and autor=%s and genero=%s and isbn=%s
        """

        query = 'select * from livro'
        columns:list[str] = []

        if(id_livro):
            columns.append('id_livro=%s')
        if(titulo):
            columns.append('titulo=%s')
        if(autor):
            columns.append('autor=%s')
        if(genero):
            columns.append('genero=%s')
        if(isbn):
            columns.append('isbn=%s')
        if(status_livro):
            columns.append('status_livro=%s')

        if(len(columns) != 0):
            query += ' where ' + ' and '.join(columns)

        return query

    @staticmethod
    def deleteQuery() -> str:
        """Remove livro do banco. Input: id_livro: int"""
        return 'delete from livro where id_livro=%s'
    
    @staticmethod
    def updateQuery(titulo:bool|None = False, autor:bool|None = False, genero:bool|None = False, status:bool|None = False) -> str:
        """
        Gera o query para alterar os dados selecionados pelos argumentos verdadeiros no método.
        Example:
            update livro set titulo=%s,autor=%s,genero=%s,status_livro=%s where id_livro=%s
        """

        query = 'update livro set '
        columns = []

        if(titulo):
            columns.append('titulo=%s')
        if(autor):
            columns.append('autor=%s')
        if(genero):
            columns.append('genero=%s')
        if(status):
            columns.append('status_livro=%s')
        
        query += ','.join(columns) + ' where id_livro=%s'

        return query
    
    @staticmethod
    def getIdQuery() -> str:
        """Retorna ID do livro apartir do ISBN"""
        return 'select id_livro from livro where isbn=%s'
    
    @staticmethod
    def setEmprestadoQuery() -> str:
        """Altera status_livro para emprestado. Input: id_livro: int"""
        return 'update livro set status_livro=2 where id_livro=%s'

    def __str__(self) -> str:
        return f'ID: {self.getId()}, Título: {self.getTitulo()}, Autor: {self.getAutor()}, Gênero: {self.getGenero()}, ISBN: {self.getIsbn()}, Status: {self.getStatus()}'

    def __iter__(self):
        return iter((self._titulo, self._autor, self._genero, self._isbn, self._status))

class LivroBuilder:
    def __init__(self) -> None:
        self._livro = Livro()

    def addId(self, id: int):
        self._livro.setId(id)
        return self

    def addTitulo(self, titulo: str):
        self._livro.setTitulo(titulo)
        return self

    def addAutor(self, autor: str):
        self._livro.setAutor(autor)
        return self

    def addGenero(self, genero: str):
        self._livro.setGenero(genero)
        return self

    def addIsbn(self, isbn: str):
        self._livro.setIsbn(isbn)
        return self

    def addStatus(self, status: int = 1):
        self._livro.setStatus(status)
        return self

    def build(self):
        if(self._livro.getTitulo() == ''):
            raise ValueError('O atributo Titulo não pode ser vazio')
        if(self._livro.getAutor() == ''):
            raise ValueError('O atributo Autor não pode ser vazio')
        if(self._livro.getGenero() == ''):
            raise ValueError('O atributo Genero não pode ser vazio')
        if(self._livro.getIsbn() == ''):
            raise ValueError('O atributo Isbn não pode ser vazio')
        if(self._livro.getStatus() is None):
            raise ValueError('O atributo Status precisa ser um int')
        return self._livro

Livro.__name__ = 'Livro'
LivroBuilder.__name__ = 'LivroBuilder'

if __name__ == "__main__":
    teste = (LivroBuilder()
                .addId(7)
                .addTitulo('test1')
                .addAutor('test2')
                .addGenero('test3')
                .addIsbn('007')
                .addStatus()
                .build()
            )

    print(teste)
    #print(ControllerLivro.adicionarLivroFromInstance(teste))
    #print(teste.selectQuery(titulo=True, isbn=True, autor=True, genero=True))