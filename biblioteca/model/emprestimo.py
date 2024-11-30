__all__ = ['Emprestimo']

class Emprestimo:
    def __init__(self, id_emprestimo: int, id_usuario: int, nome_usuario: str, id_livro: int, titulo_livro: str) -> None:
        self._id_emprestimo: int = id_emprestimo
        self._id_usuario: int = id_usuario
        self._nome_usuario: str = nome_usuario
        self._id_livro: int = id_livro
        self._titulo_livro: str = titulo_livro
    
    def getID(self) -> int:
        return self._id_emprestimo
    
    def getIdUsuario(self) -> int:
        return self._id_usuario
    
    def getNomeUsuario(self) -> str:
        return self._nome_usuario
    
    def getIdLivro(self) -> int:
        return self._id_livro
    
    def getTituloLivro(self) -> str:
        return self._titulo_livro

    @staticmethod
    def adicionarEmprestimo() -> str:
        """Adiciona um novo emprestimo"""

        return 'insert into emprestimo(id_livro,id_usuario,devolvido) values (%s,%s,false)'

    @staticmethod
    def isLivroEmprestado() -> str:
        """
            Retorna o ID na tabela emprestimo, para livro com devolvido=False.
            Input: id_livro: int
        """
        return  """
                    select id_emprestimo
                        from emprestimo
                            where
                                id_livro=%s and
                                devolvido=false
                                    order by id_emprestado desc
                """
    
    @staticmethod
    def usuarioHasLivroEmprestado() -> str:
        """
            Retorna o ID na tabela emprestimo, baseado em um Usuario e Livro com devolvido=False.
            Input: id_livro: int;id_usuario: int
        """

        return  """
                    select id_emprestimo 
                        from emprestimo
                            where
                                id_livro=%s and
                                id_usuario=%s and
                                devolvido=false
                                    order by id_emprestimo desc
                """
    
    @staticmethod
    def usuarioHasAnyLivroEmprestado() -> str:
        """
            Retorna o ID na tabela emprestimo, baseado em um Usuario com devolvido=False.
            Input: id_usuario: int
        """
        return  """
                    select id_emprestimo 
                        from emprestimo
                            where
                                id_usuario=%s and
                                devolvido=false
                                    order by id_emprestimo desc
                """
    
    @staticmethod
    def setEmprestimoDevolvido() -> str:
        """ALtera colúna devolvido na tabela emprestimo para True. Input: id_emprestimo: int"""

        return  """
                    update emprestimo
                        set devolvido=true
                            where
                                id_emprestimo=%s
                """
    
    @staticmethod
    def listarEmprestimo(nome_usuario: bool | None = None, nome_livro: bool | None = None) -> str:
        """Retorna todos os emprestimos com base no Nome do usuário ou Nome do livro, seguindo o formato: ID: int, ID Usuário: int, Nome Usuário: str, ID Livro: int, Título Livro: str"""

        query = """select e.id_emprestimo,u.id_usuario,u.nome,l.id_livro,l.titulo
                    from emprestimo as e
                        inner join usuario as u
                            on e.id_usuario=u.id_usuario
                        inner join livro as l
                            on e.id_livro=l.id_livro
                                where
                """

        condition = []
        if(nome_usuario is not None):
            condition.append(' u.nome like %s')
        if(nome_livro is not None):
            condition.append(' l.titulo like %s')

        query += ' and '.join(condition)

        return query
    
    @staticmethod
    def listarTodosEmprestimos() -> str:
        """Retorna todos os valores em emprestimo, seguindo o formato: ID: int, ID Usuário: int, Nome Usuário: str, ID Livro: int, Título Livro: str"""
        return  """select e.id_emprestimo,u.id_usuario,u.nome,l.id_livro,l.titulo
                    from emprestimo as e
                        inner join usuario as u
                            on e.id_usuario=u.id_usuario
                        inner join livro as l
                            on e.id_livro=l.id_livro
                """