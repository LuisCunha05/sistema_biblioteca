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
        
    @staticmethod
    def listarEmprestimo(nome_usuario: str = None, nome_livro: str = None) -> list[dict[str,str | int]]:
        """Retorna uma lista contendo os emprestimos dado os inputs. Formato: {id_emprestimo:int,nome_usuario:str,nome_livro:str}"""
        lista: list[dict[str,str | int]] = []

        try:
            db = DB()

            arg = []
            if(nome_usuario):
                arg.append(f'%{nome_usuario}%')
            if(nome_livro):
                arg.append(f'%{nome_livro}%')

            arg = tuple(arg)

            db.exec(Emprestimo.listarEmprestimo(nome_usuario=nome_usuario, nome_livro=nome_livro), arg)
            result = db.f_all()

            if(result is not None and len(result) == 0):
                print('Nenhum emprestimo encontrado')
                return lista
            
            for dado in result:
                lista.append({'id':dado[0],'nome_usuario':dado[1],'nome_livro':dado[2]})
            
            return lista
        except Exception as e:
            print(f'Erro ao listar emprestimos do banco de dados:\n{e}')
            return lista