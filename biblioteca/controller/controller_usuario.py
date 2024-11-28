__all__ = ['ControllerUsuario']
from ..model.database import DB
from ..model.usuario import Usuario, UsuarioBuilder
from ..util import unpackValue

class ControllerUsuario:

    @staticmethod
    def verificarLogin(uEmail: str, uSenha:str) -> Usuario | bool:
        """Retorna uma instância do Usuário, caso login seja válido, false caso não"""
        try:
            db = DB()

            db.exec(Usuario.getUsuarioByEmailQuery(), (uEmail,))

            usuario = db.f_one()
            if(usuario is None):
                return False
            
            id_usuario, nome, cpf, senha, email = usuario

            if(uSenha != senha):
                print('Erro ao verficiar login, Senha incorreta')
                return False
            
            try:
                return (
                    UsuarioBuilder()
                        .addId(id_usuario)
                        .addNome(nome)
                        .addCpf(cpf)
                        .addEmail(email)
                        .build()
                )

            except (ValueError, TypeError) as e:
                print(e)
                return False
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