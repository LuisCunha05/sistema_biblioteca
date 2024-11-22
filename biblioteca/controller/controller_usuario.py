__all__ = ['ControllerUsuario']
from ..model.database import DB
from ..model.usuario import Usuario, UsuarioBuilder
from ..model.config import SALT

class ControllerUsuario:

    @staticmethod
    def instanceFromDB(id_usuario: int = None, nome: str = None, cpf: str = None, email: str = None) -> list[Usuario]:
        """Retorna um instancia de Usuario apartir do banco de dados, caso exista e None caso contrário"""
        try:
            db = DB()

            args = []
            if(id_usuario):
                args.append(id_usuario)
            

            db.exec(Usuario.selectQuery(cpf=True), (cpf,))

            result = db.f_all()
            print(result)
            if(result is None):
                print(f'Usuário com cpf: {cpf}, não existe')
                return False
            id_usuario, nome, cpf_, email = result

            return  (
                UsuarioBuilder()
                    .addId(id_usuario)
                    .addNome(nome)
                    .addCpf(cpf_)
                    .addEmail(email)
                    .build()
            )

        except Exception as e:
            print(f'Erro ao criar instância de usuário através do banco de dados:\nErro:{e}')
    
    @staticmethod
    def adicionarUsuario(nome: str, cpf: str, senha: str, email: str) -> bool:
        pass
    #cadastro: livro,usuario,emprestimo