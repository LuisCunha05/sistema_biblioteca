__all__ = ['ControllerUsuario']
from ..model.database import DB
from ..model.usuario import Usuario, UsuarioBuilder
from ..model.config import SALT

class ControllerUsuario:

    @staticmethod
    def instanceFromDB(cpf: str) -> Usuario:
        """Retorna um instancia de Usuario apartir do banco de dados, caso exista e None caso contrário"""
        try:
            db = DB()
            db.exec(Usuario.selectQuery(cpf=True), (cpf,))

            result = db.f_one()
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