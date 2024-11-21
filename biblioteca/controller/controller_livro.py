__all__ = ['ControllerLivro']
from ..model.database import DB
from ..model.livro import Livro, LivroBuilder
from ..model.usuario import Usuario, UsuarioBuilder

class ControllerLivro:
    @staticmethod
    def instanceFromDB(isbn: str) -> Livro:
        try:
            db = DB()

            db.exec(Livro.selectQuery(isbn=True), (isbn,))
            id_livro,titulo,autor,genero,status,isbn_ = db.f_one()

            return (LivroBuilder()
                            .addTitulo(titulo)
                            .addAutor(autor)
                            .addGenero(genero)
                            .addStatus(status)
                            .addIsbn(isbn_)
                            .build()
                        )
        except Exception as e:
            print(f'Erro ao criar instância de livro através do banco de dados:\nErro:{e}')

    
    @staticmethod
    def adicionarLivro(titulo: str, autor: str, genero: str, isbn: str, status: int = 1) -> bool:
        """Adiciona um novo livro ao banco de dados. Verifica primeiro se Isbn já existe no banco e aborta caso sim. Retorna um Bool com status de sucesso da operação de adição"""
        try:
            novo: Livro =(LivroBuilder()
                            .addTitulo(titulo)
                            .addAutor(autor)
                            .addGenero(genero)
                            .addStatus(status)
                            .addIsbn(isbn)
                            .build()
                        )
        except (ValueError, TypeError) as e:
            print(f'Erro ao criar instância de Livro:\n{e}')
            return False

        try:
            db = DB()
            id_livro = ControllerLivro.getIdLivro(db, isbn)

            if(not id_livro):
                print(f'Livro com Isbn: {isbn}, já foi adicionado!')
                return False

            db.exec(query=novo.createQuery(), args=novo.getAsDB())
            db.commit()
            db.close()
            return True
        except Exception as e:
            print(f'Erro ao connectar ao banco de dados: {e}')
            return False
    
    @staticmethod
    def adicionarLivroFromInstance(livro: Livro) -> bool:
        """Adiciona um novo livro ao banco de dados. Verifica primeiro se Isbn ja existe no banco e aborta caso sim. Retorna um Bool com status de sucesso da operação de adição"""

        try:
            db = DB()
            id_livro = ControllerLivro.getIdLivro(db, livro)

            if(id_livro):
                print(f'Livro com Isbn: {livro.getIsbn()}, já foi adicionado!')
                return False

            db.exec(query=livro.createQuery(), args=livro.getAsDB())
            db.commit()
            db.close()
            return True
        except Exception as e:
            print(f'Erro ao connectar ao banco de dados: {e}')
            return False
    
    @staticmethod
    def alterarLivro(livro: Livro, titulo: str = None, autor: str = None, genero: str = None, status: int = None) -> bool:
        try:
            db = DB()
            id_livro = ControllerLivro.getIdLivro(db, livro)

            if(not id_livro):
                print(f'Livro com Isbn: {livro.getIsbn()}, não foi encontrado!')
                return False

            #Gerando tuple para query
            arg = []
            if(titulo):
                arg.append(titulo)
            if(autor):
                arg.append(autor)
            if(genero):
                arg.append(genero)
            if(status):
                arg.append(status)
            arg.append(livro.getIsbn())
            arg = tuple(arg)

            db.exec(query=livro.updateQuery(titulo=titulo, autor=autor, genero=genero, status=status), args=arg)
            db.commit()
            db.close()
            return True
        except Exception as e:
            print(f'Erro ao connectar ao banco de dados: {e}')
            return False
    
    @staticmethod
    def getIdLivro(database:DB, livro: Livro | str) -> int:
        """Retorna o id do livro caso exista, Raises ValueError se livro não exister no banco de dados"""

        if(isinstance(livro, Livro)):
            database.exec(livro.getIdQuery(), (livro.getIsbn(),))
        elif(type(livro) == str):
            database.exec('select id_livro from livro where isbn=%s', (livro,))
        else:
            raise TypeError('Livro não corresponde a um tipo válido')

        id_livro = database.f_one()

        if(not id_livro):
            raise ValueError('Livro inexistente')

        id_livro = id_livro[0]
        return id_livro