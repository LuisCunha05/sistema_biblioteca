__all__ = ['ControllerUsuario']
from ..model.database import DB
from ..model.usuario import Usuario, UsuarioBuilder
from ..model.config import SALT
from ..util import unpackValue

class ControllerUsuario:

    
    @staticmethod
    def adicionarUsuario(usuario: Usuario, senha: str) -> bool:
        if(len(senha) == 0):
            print('Erro ao adicionar usuário, senha inválida')
            return False
        
        try:
            db = DB()

            arg = (usuario.getNome(), usuario.getCpf(), senha, usuario.getEmail())

            db.exec(usuario.createQuery(), arg)
            db.commit()
            db.close()
            return True
        except Exception as e:
            print(f'Erro ao adicionar usuário ao banco de dados:\nErro:{e}')
    
    @staticmethod
    def selecionarUsuario(id_usuario: int = None, nome: str = None, cpf: str = None, email: str = None) -> list[Usuario]:
        """Retorna um instancia de Usuario apartir do banco de dados, caso exista e None caso contrário"""
        try:
            lista = []
            db = DB()

            args = []
            if(id_usuario):
                args.append(id_usuario)
            if(nome):
                args.append(f'%{nome}%')
            if(cpf):
                args.append(cpf)
            if(email):
                args.append(email)
            args = tuple(args)

            db.exec(Usuario.selectQuery(id_usuario=id_usuario, nome=nome,cpf=cpf,email=email), args)

            result = db.f_all()

            if(not len(result)):
                print(f'Usuário não existe')
                return lista
            
            for dado in result:
                try:
                    uId, uNome, uCpf, uEmail = dado
                    lista.append((
                        UsuarioBuilder()
                            .addId(uId)
                            .addNome(uNome)
                            .addCpf(uCpf)
                            .addEmail(uEmail)
                            .build()
                    ))
                except (ValueError, TypeError) as e:
                    print(e)
            
            return lista

        except Exception as e:
            print(f'Erro ao criar instância de usuário do banco de dados:\nErro:{e}')

    @staticmethod
    def removerUsuario(usuario: Usuario) -> bool:
        try:
            db = DB()

            db.exec(usuario.selectQuery(id_usuario=True), (usuario.getId(),))

            try:
                result = unpackValue(db.f_one())
            except ValueError as e:
                print('Usuário não encontrado no banco de dados')
                return False
            
            db.exec(usuario.deleteQuery(), (usuario.getId(),))
            db.commit()
            db.close()
            del usuario
            return True
        except Exception as e:
            print(f'Erro ao remover o usuário do banco de dados:\nErro:{e}')
    
    @staticmethod
    def alterarUsuario(usuario: Usuario, nome: str = None, senha: str = None, email:str = None) -> bool:
        try:
            db = DB()

            db.exec(usuario.selectQuery(id_usuario=True), (usuario.getId(),))

            try:
                result = unpackValue(db.f_one())
            except ValueError as e:
                print('Usuário não encontrado no banco de dados')
                return False
            
            if(senha and len(senha) == 0):
                print('Senha inválida')
                return False
            
            arg = []
            if(nome):
                usuario.setNome(nome)
                arg.append(nome)
            if(senha):
                arg.append(senha)
            if(email):
                usuario.setEmail(email)
                arg.append(email)
            
            arg.append(usuario.getId())
            arg = tuple(arg)

            db.exec(usuario.updateQuery(nome=nome, senha=senha, email=email), arg)
            db.commit()
            db.close()
            return True
        except Exception as e:
            print(f'Erro ao alterar o usuário do banco de dados:\nErro:{e}')

    # @staticmethod
    # def adicionarUsuario(nome: str, cpf: str, senha: str, email: str) -> bool:
    #     try:
    #         novo = (
    #             UsuarioBuilder()
    #                 .addNome(nome)
    #                 .addCpf(cpf)
    #                 .addEmail(email)
    #                 .build()
    #         )
    #     except (ValueError, TypeError) as e:
    #         print('Valores inválidos para criar um Usuário')
    #         return False
        
    #     if(len(senha) == 0):
    #         print('Senha inválida')
    #         return False
        
    #     try:
    #         db = DB()

    #         arg = (novo.getNome(), novo.getCpf(), senha, novo.getEmail())

    #         db.exec(novo.createQuery(), arg)
    #         db.commit()
    #         db.close()
    #         return True
    #     except Exception as e:
    #         print(f'Erro ao adicionar usuário ao banco de dados:\nErro:{e}')