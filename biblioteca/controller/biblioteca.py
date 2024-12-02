from ..model.database import DB
from ..model.livro import Livro, LivroBuilder
from ..model.usuario import Usuario, UsuarioBuilder
from ..model.administrador import Administrador, AdministradorBuilder
from .controller_usuario import ControllerUsuario
from .controller_livro import ControllerLivro
from .controller_emprestimo import ControllerEmprestimo
from .controller_administrador import ControllerAdministrador
from .controller_emprestimo import ControllerEmprestimo, Emprestimo


__all__ = ['Biblioteca']

class Biblioteca:

    @staticmethod
    def fazerLogin(email: str, senha: str) -> Usuario | Administrador | bool:
        """Tenta realiazar o login e retorna um instância de Usuário ou Administrador"""
        usuario = ControllerUsuario.verificarLogin(uEmail=email, uSenha=senha)
        if(not usuario):
            return False
        
        if(ControllerUsuario.verificarAdministrador(usuario.getId())):
            usuario = (
                AdministradorBuilder()
                .addId(usuario.getId())
                .addNome(usuario.getNome())
                .addCpf(usuario.getCpf())
                .addEmail(usuario.getEmail())
                .build()
            )
            print('Logado como Administrador!')
        
        return usuario
    
    @staticmethod
    def fazerCadastro(nome: str, cpf:str, senha:str, email: str) -> bool:
        try:
            novo_usuario =  (
                UsuarioBuilder()
                    .addNome(nome)
                    .addCpf(cpf)
                    .addEmail(email)
                    .build()
            )
        except (ValueError, TypeError) as e:
            print(f'Erro ao realizar cadastro: {e}')
            return False
        
        return ControllerUsuario.adicionarUsuario(novo_usuario, senha)

    @staticmethod
    def fazerEmprestimo(usuario: Usuario, livro: Livro) -> bool:

        if(not ControllerUsuario.verificarSeUsuarioExiste(usuario.getCpf())):
            return False

        if(not ControllerLivro.verificarLivroExiste(livro.getIsbn(),)):
            return False
        
        if(not ControllerEmprestimo.fazerEmprestimo(livro=livro, usuario=usuario)):
            return False
        
        return ControllerLivro.alterarLivro(status=2)

    @staticmethod
    def fazerDevolucao(usuario: Usuario, livro: Livro) -> bool:

        if(not ControllerUsuario.verificarSeUsuarioExiste(usuario.getCpf())):
            return False

        if(not ControllerLivro.verificarLivroExiste(livro.getIsbn(),)):
            return False
        
        if(not ControllerLivro.alterarLivro(status=1)):
            return False

        return ControllerEmprestimo.fazerDevolucao(livro)
    
    @staticmethod
    def listarEmprestimo(uNome_usuario: str = None, uTitulo_livro: str = None) -> list[Emprestimo]:
        lista: list[Emprestimo] = None

        if(uNome_usuario or uTitulo_livro):
            lista = ControllerEmprestimo.listarEmprestimo(uNome_usuario, uTitulo_livro)
        else:
            lista = ControllerEmprestimo.listarTodosEmprestimos()

        return lista


if __name__ == "__main__":
    pass