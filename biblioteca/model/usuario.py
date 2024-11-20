__all__ = ['Usuario', 'UsuarioBuilder']

class Usuario:
    def __init__(self) -> None:
        self._id_usuario: int = None
        self._nome: str = ''
        self._cpf: str = ''
        self._email: str = ''
        self._livros: list[str] = []

    def setId(self, id: int):
        if(type(id) != int):
            raise TypeError("Tipo esperado: int")
        if(id <= 0):
            raise ValueError('Id não pode ser menor ou igual a 0')

        self._id_usuario = id

    def setNome(self, nome: str):
        if(type(nome) != str):
            raise TypeError("Tipo esperado: str")
        if(nome == ''):
            raise ValueError('Nome não pode ser vazio!')

        self._nome = nome


    def setCpf(self, cpf: str):
        if(type(cpf) != str):
            raise TypeError("Tipo esperado: str")
        if(cpf == ''):
            raise ValueError('Cpf não pode ser vazio!')

        cpf = cpf.replace('.', '').replace('-', '').replace(' ', '')

        if(len(cpf) != 11):
            raise ValueError("Cpf não possui comprimento correto.")
        if(not cpf.isdigit()):
            raise TypeError("Cpf deve conter apenas [0-9], '.' ou '-'" )

        self._cpf = cpf


    def setEmail(self, email: str):
        if(type(email) != str):
            raise TypeError("Tipo esperado: str")
        if(email == '' or email.find('@') < 0):
            raise ValueError('Email Inválido!')

        self._email = email

    def getId(self) -> int:
        return self._id_usuario

    def getNome(self) -> str:
        return self._nome

    def getCpf(self) -> str:
        return self._cpf

    def getEmail(self) -> str:
        return self._email

    @staticmethod
    def createQuery() -> str:
        return 'insert into usuario(nome,cpf,senha,email) values (%s,%s,%s,%s)'
    
    @staticmethod
    def selectQuery(nome:bool|None = False, email:bool|None = False, id_usuario:bool|None = False) -> str:
        """
        Gera o query para ler os usuarios, aplicando os filtros dados pelos argumentos verdadeiros no método.
        Example:
            select * from usuario where nome=%s and email=%s and id_usuario=%s
        """

        query = 'select * from usuario'
        columns:list[str] = []

        if(nome):
            columns.append('nome=%s')
        if(email):
            columns.append('email=%s')
        if(id_usuario):
            columns.append('id_usuario=%s')

        if(len(columns) != 0):
            query += ' where ' + ' and '.join(columns)

        return query
    
    @staticmethod
    def deleteQuery() -> str:
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
    def getIdQuery(self) -> str:
        return 'select id_usuario from usuario where cpf=%s'
    
    def __str__(self) -> str:
        return f'ID: {self.getId()}, Nome: {self.getNome()}, Cpf: {self.getCpf()}, Email: {self.getEmail()}'

class UsuarioBuilder():
    def __init__(self) -> None:
        self._usuario = Usuario()

    def addId(self, id_usuario: int):
        self._usuario.setId(id=id_usuario)
        return self

    def addNome(self, nome: str):
        self._usuario.setNome(nome=nome)
        return self
    
    def addCpf(self, cpf: str):
        self._usuario.setCpf(cpf=cpf)
        return self
    
    def addEmail(self, email: str):
        self._usuario.setEmail(email=email)
        return self
    
    def build(self):
        if(self._usuario.getId() is None):
            raise ValueError('Id do usuario não pode ser Nulo')
        if(self._usuario.getNome() == ''):
            raise ValueError('Nome não pode ser vazio')
        if(self._usuario.getCpf() == ''):
            raise ValueError('Cpf não pode ser vazio')
        if(self._usuario.getEmail() == ''):
            raise ValueError('Email não pode ser vazio')
        
        return self._usuario

Usuario.__name__ = 'Usuario'
UsuarioBuilder.__name__ = 'UsuarioBuilder'

if __name__ == "__main__":
    aa = (UsuarioBuilder()
            .addId(3)
            .addNome('Jaum')
            .addCpf('12345678911')
            .addEmail('he@oi.com')
            .build()
        )
    
    print(aa)

