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
    
    # def __init__(self) -> None:
    #     self._id_emprestimo: int = None
    #     self._id_livro: int = None
    #     self._id_usuario: int = None
    #     self._devolvido: bool = None
    
    # def setId(self, id: int):
    #     if(type(id) != int):
    #         raise TypeError('Tipo esperado: int')
    #     if(id <= 0):
    #         raise ValueError('ID precisa não pode ser menor ou igual Zero')
        
    #     self._id_emprestimo = id

    # def setIdLivro(self, id: int):
    #     if(type(id) != int):
    #         raise TypeError('Tipo esperado: int')
    #     if(id <= 0):
    #         raise ValueError('ID precisa não pode ser menor ou igual Zero')
        
    #     self._id_livro = id

    # def setIdUsuario(self, id: int):
    #     if(type(id) != int):
    #         raise TypeError('Tipo esperado: int')
    #     if(id <= 0):
    #         raise ValueError('ID precisa não pode ser menor ou igual Zero')
        
    #     self._id_usuario = id
    
    # def setDevolvido(self, devolvido: bool):
    #     if(type(devolvido) != bool):
    #         raise TypeError('Tipo esperado: int')
        
    #     self._devolvido = devolvido

    # def getId(self) -> int:
    #     return self._id_emprestimo
    
    # def getIdLivro(self) -> int:
    #     return self._id_livro
    
    # def getIdUsuario(self) -> int:
    #     return self._id_usuario

    # def getDevolvido(self) -> bool:
    #     return self._devolvido

    # def __str__(self) -> str:
    #     return f'ID: {self.getId()}, ID Livro: {self.getIdLivro()}, ID Usuario: {self.getIdUsuario()}, Devolvido: {self.getDevolvido()}'
    
    # def __repr__(self) -> str:
    #     return f'Emprestimo({self.getId()},{self.getIdLivro()},{self.getIdUsuario()},{self.getDevolvido()})'

if __name__ == '__main__':
    pass