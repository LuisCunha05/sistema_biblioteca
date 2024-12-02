from .usuario import Usuario, UsuarioBuilder

class Administrador(Usuario):
    def __init__(self) -> None:
        super().__init__()
        self.__isAdmin = True

    def isAdmin(self) -> bool:
        return self.__isAdmin
    
    @staticmethod
    def deleteQuery() -> str:
        """Remove o usuário. Input: id_usuario: int"""
        return 'delete from usuario where id_usuario=%s'
    
    @staticmethod
    def updateQuery(nome: bool | None = False, senha: bool | None = False, email: bool | None = False) -> str:
        """
        Gera o query para alterar os dados selecionados pelos argumentos verdadeiros no método.
        Example:
            update usuario set nome=%s,senha=%s,email=%s where id_usuario=%s
        """

        query = 'update usuario set '
        columns = []

        if(nome):
            columns.append('nome=%s')
        if(senha):
            columns.append('senha=%s')
        if(email):
            columns.append('email=%s')

        query += ','.join(columns) + ' where id_usuario=%s'

        return query
    
    @staticmethod
    def createAdministradorQuery() -> str:
        """Query para transformar um usuário em administrador"""

        return 'insert into administrador(id_usuario) values (%s)'


class AdministradorBuilder(UsuarioBuilder):
    def __init__(self) -> None:
        super().__init__()
        self._usuario = Administrador()

    def build(self) -> Administrador:
        return super().build()