from .usuario import Usuario, UsuarioBuilder

class Administrador(Usuario):
    def __init__(self) -> None:
        super().__init__()
        self.__isAdmin = True

    def isAdmin(self) -> bool:
        return self.__isAdmin
    
    @staticmethod
    def createQuery() -> str:
        """Adiciona um novo usuário. Input: nome:str; cpf:str; senha:str; email:str"""
        return 'insert into usuario(nome,cpf,senha,email) values (%s,%s,%s,%s)'
    
    @staticmethod
    def deleteQuery() -> str:
        """Remove o usuário. Input: id_usuario: int"""
        return 'delete from usuario where id_usuario=%s'
    
    @staticmethod
    def selectQuery(id_usuario:bool|None = False, nome:bool|None = False, email:bool|None = False,  cpf:bool|None = False) -> str:
        """
        Gera o query para ler o usuario, aplicando os filtros dados pelos argumentos verdadeiros no método.
        Example:
            select id_usuario,nome,cpf,email from usuario where id_usuario=%s and nome=%s and email=%s and cpf=%s
        """

        query = 'select id_usuario,nome,cpf,email from usuario'
        columns:list[str] = []

        if(id_usuario):
            columns.append('id_usuario=%s')
        if(nome):
            columns.append('nome like %s')
        if(email):
            columns.append('email=%s')
        if(cpf):
            columns.append('cpf=%s')
        

        if(len(columns) != 0):
            query += ' where ' + ' and '.join(columns)

        return query

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


class AdministradorBuilder(UsuarioBuilder):
    def __init__(self) -> None:
        super().__init__()
        self._usuario = Administrador()