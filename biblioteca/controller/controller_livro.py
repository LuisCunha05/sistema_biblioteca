__all__ = ['ControllerLivro']
from ..model.database import DB
from ..model.livro import Livro, LivroBuilder
from ..model.usuario import Usuario, UsuarioBuilder
from ..util import unpackValue

class ControllerLivro:
    @staticmethod
    def instanceFromDB(isbn: str) -> Livro:
        try:
            db = DB()

            db.exec(Livro.selectQuery(isbn=True), (isbn,))
            id_livro,titulo,autor,genero,status,isbn_ = db.f_one()

            return (LivroBuilder()
                            .addId(id_livro)
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
            db.exec(novo.getIdQuery(), (novo.getIsbn(),))
            try:
                id_livro = unpackValue(db.f_one())
                print(f'Livro com Isbn: {novo.getIsbn()}, já foi adicionado!')
                return False
            except ValueError:
                pass

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
            db.exec(livro.getIdQuery(), (livro.getIsbn(),))
            try:
                id_livro = unpackValue(db.f_one())
                print(f'Livro com Isbn: {livro.getIsbn()}, já foi adicionado!')
                return False
            except ValueError:
                pass
            
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
            db.exec(livro.getIdQuery(), (livro.getIsbn(),))
            try:
                id_livro = unpackValue(db.f_one())
            except ValueError:
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
            arg.append(livro.getId())
            arg = tuple(arg)

            db.exec(query=livro.updateQuery(titulo=titulo, autor=autor, genero=genero, status=status), args=arg)
            db.commit()
            db.close()
            return True
        except Exception as e:
            print(f'Erro ao connectar ao banco de dados: {e}')
            return False