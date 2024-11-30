from ..model.database import DB
from ..model.livro import Livro
from ..model.usuario import Usuario
from ..model.emprestimo import Emprestimo
from ..util import unpackValue

class ControllerEmprestimo:
    __MAX_EMPRESTIMOS: int = 3

    @staticmethod
    def getMaxEmprestimos():
        return ControllerEmprestimo.__MAX_EMPRESTIMOS

    @staticmethod
    def fazerEmprestimo(livro: Livro, usuario: Usuario) -> bool:
        """Adiciona um novo emprestimo ao banco, valida tanto livro e usuário e retorna false caso não seja possivel"""
        try:
            db = DB()
            db.exec(Emprestimo.isLivroEmprestado(), (livro.getId(),))

            try:
                result = unpackValue(db.f_one())
                print('Livro já está emprestado')
                db.close()
                return False
            except ValueError:
                pass

            db.exec(Emprestimo.usuarioHasLivroEmprestado(), (livro.getId(), usuario.getId()))
            try:
                result = unpackValue(db.f_one())
                print('Usuário já possui o livro emprestado')
                db.close()
                return False
            except ValueError:
                pass

            db.exec(Emprestimo.usuarioHasAnyLivroEmprestado(), (usuario.getId(),))
            emprestimos = db.f_all()
            if(len(emprestimos) == ControllerEmprestimo.getMaxEmprestimos()):
                print('Usuário já possui o Máximo de livros emprestados')
                db.close()
                return False

            db.exec(Emprestimo.adicionarEmprestimo(), (livro.getId(), usuario.getId()))
            db.commit()
            db.close()
            return True
        except Exception as e:
            print(f'Erro ao fazer Emprestimo no banco de dados: {e}')
            return False

    @staticmethod
    def fazerDevolucao(livro: Livro) -> bool:
        """Altera o estado de devolvido na tabela emprestimo e sinaliza que livro pode ser alterado, retorna False caso contrário"""
        try:
            db = DB()

            db.exec(Emprestimo.isLivroEmprestado(), (livro.getId(),))

            try:
                id_emprestimo = unpackValue(db.f_one())
            except ValueError as e:
                print('Erro ao fazer Devolução, livro não emprestado')
                db.close()
                return False
            
            db.exec(Emprestimo.setEmprestimoDevolvido(), (id_emprestimo,))
            db.commit()
            db.close()
            return True
        except Exception as e:
            print(f'Erro ao fazer Devolução no banco de dados: {e}')
            return False
        
    @staticmethod
    def listarEmprestimo(uNome_usuario: str = None, uTitulo_livro: str = None) -> list[Emprestimo]:
        """Retorna uma lista contendo os emprestimos com base nos filtros. """
        lista: list[Emprestimo] = []

        try:
            db = DB()

            arg = []
            if(uNome_usuario):
                arg.append(f'%{uNome_usuario}%')
            if(uTitulo_livro):
                arg.append(f'%{uTitulo_livro}%')

            arg = tuple(arg)

            db.exec(Emprestimo.listarEmprestimo(nome_usuario=uNome_usuario, nome_livro=uTitulo_livro), arg)
            result = db.f_all()

            if(result is not None and len(result) == 0):
                print('Nenhum emprestimo encontrado')
                db.close()
                return lista
            
            for dado in result:
                id_emprestimo,id_usuario,nome_usuario,id_livro,titulo_livro = dado 
                lista.append(Emprestimo(id_emprestimo, id_usuario, nome_usuario, id_livro, titulo_livro))
            
            db.close()
            return lista
        except Exception as e:
            print(f'Erro ao listar emprestimos do banco de dados:\n{e}')
            return lista
    
    @staticmethod
    def listarTodosEmprestimos() -> list[Emprestimo]:
        """Retorna uma lista contendo todos os emprestimos."""
        lista: list[Emprestimo] = []

        try:
            db = DB()

            db.exec(Emprestimo.listarTodosEmprestimos())
            result = db.f_all()

            if(result is not None and len(result) == 0):
                print('Nenhum emprestimo encontrado')
                db.close()
                return lista
            
            for dado in result:
                id_emprestimo,id_usuario,nome_usuario,id_livro,titulo_livro = dado 
                lista.append(Emprestimo(id_emprestimo, id_usuario, nome_usuario, id_livro, titulo_livro))
            
            db.close()
            return lista
        except Exception as e:
            print(f'Erro ao listar emprestimos do banco de dados:\n{e}')
            return lista