from ..model.database import DB
from ..util import toHash
from ..model.livro import Livro, LivroBuilder
from ..model.usuario import Usuario, UsuarioBuilder
from .controller_usuario import ControllerUsuario
from .controller_livro import ControllerLivro
from .controller_emprestimo import ControllerEmprestimo


__all__ = ['Biblioteca']

class Biblioteca:

    @staticmethod
    def fazerLogin(email: str, senha: str) -> Usuario | bool:
        if(not ControllerUsuario.verificarLogin(uEmail=email, uSenha=senha)):
            return False
        
        usuario, = ControllerUsuario.selecionarUsuario(email=email)
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
        if(len(usuario.livros) == usuario.getMaxEmprestimo()):
            print('O usuário já atingiu o maximo de emprestimos')
            return False
        
        if(livro.status != 'Disponivel'):
            print('O livro não pode ser emprestado!')
            return False
        
        usuario.adicionarLivro(livro.titulo)
        livro.emprestarLivro(usuario)
    @staticmethod
    def fazerDevolucao(usuario: Usuario, livro: Livro) -> bool:
        if(len(usuario.livros) == 0):
            print('O usuário não possui livros para devolver')
            return False
        
        if(livro.status != 'Emprestado'):
            print('O livro não está emprestado!')
            return False
        
        usuario.adicionarLivro(livro)
        livro.devolverLivro()

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