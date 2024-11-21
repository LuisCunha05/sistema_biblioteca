__all__ = ['ControllerUsuario']
from ..model.database import DB
from ..model.usuario import Usuario, UsuarioBuilder

class ControllerUsuario:

    @staticmethod
    def instanceFromDB(cpf: str) -> Usuario:
        try:
            db = DB()
            db.exec(Usuario.selectQuery(cpf=True), (cpf,))

            result = db.f_one()
            if(result is None):
                print(f'Usuário com cpf: {cpf}, não existe')
                return False
            id_usuario, nome,email,cpf = result


        except Exception as e:
            print(f'Erro ao criar instância de usuário através do banco de dados:\nErro:{e}')