from ..model.database import DB
from ..model.usuario import Usuario, UsuarioBuilder
from ..controller.controller_usuario import ControllerUsuario
from ..model.administrador import Administrador, AdministradorBuilder
from ..util import unpackValue

class ControllerAdministrador(ControllerUsuario):
    @staticmethod
    def adicionarAdministrador(id_usuario: str) -> bool:
        try:
            db = DB()

            db.exec(Administrador.isAdministradorQuery(), (id_usuario,))

            try:
                result = unpackValue(db.f_one())
            except ValueError as e:
                print('Usuário já é um administrador')
                db.close()
                return False

            db.exec(Administrador.createAdministradorQuery(), (id_usuario,))
            db.commit()
            db.close()
            return True
        except Exception as e:
            print(f'Erro ao adicionar novo administrador no banco de dados:\nErro:{e}')
            return False

    @staticmethod
    def removerUsuario(usuario: Usuario) -> bool:
        try:
            db = DB()

            db.exec(Administrador.selectQuery(id_usuario=True), (usuario.getId(),))

            try:
                result = unpackValue(db.f_one())
            except ValueError as e:
                print('Usuário não encontrado no banco de dados')
                db.close()
                return False
            
            db.exec(Administrador.deleteQuery(), (usuario.getId(),))
            db.commit()
            db.close()
            del usuario
            return True
        except Exception as e:
            print(f'Erro ao remover o usuário do banco de dados:\nErro:{e}')
            return False
    
    @staticmethod
    def alterarUsuario(usuario: Usuario, nome: str = None, senha: str = None, email:str = None) -> bool:
        try:
            db = DB()

            db.exec(Administrador.selectQuery(id_usuario=True), (usuario.getId(),))

            try:
                result = unpackValue(db.f_one())
            except ValueError as e:
                print('Usuário não encontrado no banco de dados')
                db.close()
                return False
            
            if(senha and len(senha) == 0):
                print('Senha inválida')
                db.close()
                return False
            
            arg = []

            if(nome):
                usuario.setNome(nome)
                arg.append(nome)
            
            if(senha):
                arg.append(senha)

            if(email):
                db.exec(Administrador.selectQuery(email=True), (email,))
                try:
                    teste = unpackValue(db.f_one())
                    print(f'Erro ao alterar usuário, Email já registrado')
                    db.close()
                    return False
                except ValueError as e:
                    pass
                usuario.setEmail(email)
                arg.append(email)
            
            arg.append(usuario.getId())
            arg = tuple(arg)

            db.exec(Administrador.updateQuery(nome=nome, senha=senha, email=email), arg)
            db.commit()
            db.close()
            return True
        except Exception as e:
            print(f'Erro ao alterar o usuário do banco de dados:\nErro:{e}')
            return False