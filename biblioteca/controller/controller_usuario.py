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
                print('Erro ao verficiar login, Usuário não existe')
                db.close()
                return False
            
            id_usuario, nome, cpf, senha, email = usuario

            if(uSenha != senha):
                print('Erro ao verficiar login, Senha incorreta')
                db.close()
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
                db.close()
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
                db.close()
                return True
            except ValueError as e:
                print('Usuário não é administrador')
                db.close()
                return False
            
        except Exception as e:
            print(e)
            return False
    
    @staticmethod
    def verificarSeUsuarioExiste(cpf: str) -> bool:
        try:
            db = DB()

            db.exec(Usuario.getIdQuery(), (cpf,))

            try:
                usuario = unpackValue(db.f_one())
                db.close()
                return True
            except ValueError as e:
                print('Usuário não existe')
                db.close()
                return False
        except Exception as e:
            print(e)
            return False