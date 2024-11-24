__all__ = ['Emprestimo']

class Emprestimo:

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
        """Retorna todos os emprestimos com base no Nome do usuário ou Nome do livro"""

        query = """select u.nome,l.titulo
                    from emprestimo as e
                        inner join usuario as u
                            on e.id_usuario=u.id_usuario
                        inner join livro as l
                            on e.id_livro=l.id_livro
                                where"""

        condition = []
        if(nome_usuario is not None):
            condition.append(' u.nome like %s ')
        if(nome_livro is not None):
            condition.append(' l.titulo like %s ')

        query += ' and '.join(condition)

        return query