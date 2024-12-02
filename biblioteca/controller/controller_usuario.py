__all__ = ['ControllerUsuario']
from ..model.database import DB
from ..model.usuario import Usuario, UsuarioBuilder
from ..util import unpackValue

class ControllerUsuario:

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
                db.close()
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
            return False
    
    @staticmethod
    def adicionarUsuario(usuario: Usuario, senha: str) -> bool:
        if(senha is None or len(senha) == 0):
            print('Erro ao adicionar usuário, senha inválida')
            return False
        
        try:
            db = DB()

            db.exec(Usuario.selectQuery(cpf=True, email=True), (usuario.getCpf(), usuario.getEmail()))
            teste = db.f_all()

            if(len(teste)):
                print('Usuario com CPF ou Email já existente')
                db.close()
                return False

            arg = (usuario.getNome(), usuario.getCpf(), senha, usuario.getEmail())

            db.exec(Usuario.createQuery(), arg)
            db.commit()
            db.close()
            return True
        except Exception as e:
            print(f'Erro ao adicionar usuário ao banco de dados:\nErro:{e}')
            return False

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