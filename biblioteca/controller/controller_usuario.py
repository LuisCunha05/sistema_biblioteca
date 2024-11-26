__all__ = ['ControllerUsuario']
from ..model.database import DB
from ..model.usuario import Usuario
from ..util import unpackValue

class ControllerUsuario:

    @staticmethod
    def verificarLogin(uEmail: str, uSenha:str) -> bool:
        try:
            db = DB()

            db.exec(Usuario.getUsuarioByEmailQuery(), (uEmail,))

            usuario = db.f_one()
            if(usuario is None):
                return False
            
            id_usuario = usuario[0]

            db.exec(Usuario.getSenhaQuery(), (id_usuario,))
            senha = unpackValue(db.f_one())

            if(uSenha != senha):
                print('Erro ao verficiar login, Senha incorreta')
            
            return True
        except Exception as e:
            print(e)
            return False
    
    @staticmethod
    def verificarAdministrador(id_usuario: int) -> bool:
        try:
            db = DB()

            db.exec(Usuario.isAdministradorQuery(), (id_usuario,))

            try:
                usuario = unpackValue(db.f_one())
                return True
            except ValueError as e:
                print('Usuário não é administrador')
                return False
            
        except Exception as e:
            print(e)
            return False