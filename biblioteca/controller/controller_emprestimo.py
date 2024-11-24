from ..model.database import DB
from ..model.livro import Livro
from ..model.usuario import Usuario
from ..model.emprestimo import Emprestimo
from ..util import unpackValue

class ControllerEmprestimo:
    @staticmethod
    def fazerEmprestimo(livro: Livro, usuario: Usuario) -> bool:
        """Adiciona um novo emprestimo ao banco, valida tanto livro e usuário e retorna false caso não seja possivel"""
        try:
            db = DB()
            db.exec(Emprestimo.isLivroEmprestado(), (livro.getId(),))

            try:
                result = unpackValue(db.f_one())
                print('Livro já está emprestado')
                return False
            except ValueError:
                pass

            db.exec(Emprestimo.usuarioHasLivroEmprestado(), (livro.getId(), usuario.getId()))
            try:
                result = unpackValue(db.f_one())
                print('Usuário já possui o livro emprestado')
                return False
            except ValueError:
                pass

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
                return False
            
            db.exec(Emprestimo.setEmprestimoDevolvido(), (id_emprestimo,))
            db.commit()
            db.close()
            return True
        except Exception as e:
            print(f'Erro ao fazer Devolução no banco de dados: {e}')
            return False