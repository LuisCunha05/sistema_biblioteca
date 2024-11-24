from biblioteca.model.livro import Livro, LivroBuilder
from biblioteca.model import usuario
from biblioteca.controller.controller_usuario import ControllerUsuario

if __name__ == '__main__':
    teste = ControllerUsuario.instanceFromDB(id_usuario=5)
    print(teste)

    ControllerUsuario.alterarUsuario(teste[0], nome='kdsad')

    novo = ControllerUsuario.instanceFromDB(id_usuario=5)
    print(teste)