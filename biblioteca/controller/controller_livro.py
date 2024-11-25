__all__ = ['ControllerLivro']
from ..model.database import DB
from ..model.livro import Livro, LivroBuilder
from ..model.usuario import Usuario, UsuarioBuilder
from ..util import unpackValue

class ControllerLivro:
    @staticmethod
    def selecionarLivro(id_livro: int = None, titulo: str = None, autor: str = None, genero: str = None, isbn: str = None, status: int = None) -> list[Livro]:
        try:
            lista = []
            db = DB()
            arg = []

            if(id_livro):
                arg.append(id_livro)
            if(titulo):
                arg.append(f'%{titulo}%')
            if(autor):
                arg.append(f'%{autor}%')
            if(genero):
                arg.append(f'%{genero}%')
            if(isbn):
                arg.append(isbn)
            if(status):
                arg.append(status)

            arg = tuple(arg)

            db.exec(Livro.selectQuery(id_livro=id_livro,titulo=titulo,autor=autor,genero=genero,isbn=isbn,status_livro=status), arg)
            
            result = db.f_all()
            if(not len(result)):
                print(f'Nenhum livro encontrado')
                return lista

            for dado in result:
                try:
                    lId_livro, lTitulo, lAutor, lGenero, lStatus, lIsbn = dado
                    lista.append((
                        LivroBuilder()
                            .addId(lId_livro)
                            .addTitulo(lTitulo)
                            .addAutor(lAutor)
                            .addGenero(lGenero)
                            .addStatus(lStatus)
                            .addIsbn(lIsbn)
                            .build()
                        )
                    )
                except (ValueError, TypeError) as e:
                    print(e)
            
            return lista
        except Exception as e:
            print(f'Erro ao criar instância de livro através do banco de dados:\nErro:{e}')
            return lista

    @staticmethod
    def adicionarLivro(livro: Livro) -> bool:
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
            try:
                if(titulo):
                    livro.setTitulo(titulo)
                    arg.append(titulo)
                if(autor):
                    livro.setAutor(autor)
                    arg.append(autor)
                if(genero):
                    livro.setGenero(genero)
                    arg.append(genero)
                if(status):
                    livro.setStatus(status)
                    arg.append(status)
            except (ValueError, TypeError) as e:
                print(f'Erro ao alterar livro, parametro inválido')

            arg.append(livro.getId())
            arg = tuple(arg)

            db.exec(query=livro.updateQuery(titulo=titulo, autor=autor, genero=genero, status=status), args=arg)
            db.commit()
            db.close()
            return True
        except Exception as e:
            print(f'Erro ao connectar ao banco de dados: {e}')
            return False
        
    def removerLivro(livro: Livro) -> bool:
        try:
            db = DB()

            db.exec(livro.selectQuery(id_livro=True), (livro.getId(),))

            try:
                result = unpackValue(db.f_one())
            except ValueError as e:
                print('Livro não encontrado no banco de dados')
                return False
            
            db.exec(livro.deleteQuery(), (livro.getId(),))
            db.commit()
            db.close()
            del livro
            return True
        except Exception as e:
            print(f'Erro ao remover o livro do banco de dados:\nErro:{e}')
            return False
    
    # @staticmethod
    # def adicionarLivro(titulo: str, autor: str, genero: str, isbn: str, status: int = 1) -> bool:
    #     """Adiciona um novo livro ao banco de dados. Verifica primeiro se Isbn já existe no banco e aborta caso sim. Retorna um Bool com status de sucesso da operação de adição"""
    #     try:
    #         novo: Livro = (LivroBuilder()
    #                         .addTitulo(titulo)
    #                         .addAutor(autor)
    #                         .addGenero(genero)
    #                         .addStatus(status)
    #                         .addIsbn(isbn)
    #                         .build()
    #                     )
    #     except (ValueError, TypeError) as e:
    #         print(f'Erro ao criar instância de Livro:\n{e}')
    #         return False

    #     try:
    #         db = DB()
    #         db.exec(novo.getIdQuery(), (novo.getIsbn(),))
    #         try:
    #             id_livro = unpackValue(db.f_one())
    #             print(f'Livro com Isbn: {novo.getIsbn()}, já foi adicionado!')
    #             return False
    #         except ValueError:
    #             pass

    #         db.exec(query=novo.createQuery(), args=novo.getAsDB())
    #         db.commit()
    #         db.close()
    #         return True
    #     except Exception as e:
    #         print(f'Erro ao connectar ao banco de dados: {e}')
    #         return False
    