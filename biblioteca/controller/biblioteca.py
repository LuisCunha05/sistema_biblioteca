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
    def fazerLogin(email: str, senha: str) -> Usuario | bool:
        usuario = ControllerUsuario.verificarLogin(uEmail=email, uSenha=senha)
        if(not usuario):
            return False
        
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
        
        return ControllerAdministrador.adicionarUsuario(novo_usuario, senha)

    @staticmethod
    def fazerEmprestimo(usuario: Usuario, livro: Livro) -> bool:

        if(not ControllerUsuario.verificarSeUsuarioExiste(usuario.getCpf())):
            return False

        if(not ControllerLivro.verificarLivroExiste(livro.getIsbn(),)):
            return False
        
        return ControllerEmprestimo.fazerEmprestimo(livro=livro, usuario=usuario)

    @staticmethod
    def fazerDevolucao(usuario: Usuario, livro: Livro) -> bool:

        if(not ControllerUsuario.verificarSeUsuarioExiste(usuario.getCpf())):
            return False

        if(not ControllerLivro.verificarLivroExiste(livro.getIsbn(),)):
            return False
        
        ControllerEmprestimo.fazerDevolucao(livro)
    

if __name__ == "__main__":
    teste = (LivroBuilder()
                .addId(7)
                .addTitulo('test1')
                .addAutor('test2')
                .addGenero('test3')
                .addIsbn('007')
                .addStatus()
                .build()
            )

    print(teste)