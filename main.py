from biblioteca.model.livro import Livro, LivroBuilder
from biblioteca.model import usuario
from biblioteca.controller.controller_usuario import ControllerUsuario
from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton

if __name__ == '__main__':
    teste = ControllerUsuario.selecionarUsuario(id_usuario=5)
    print(teste)

    # ControllerUsuario.alterarUsuario(teste[0], nome='kdsad')

    # novo = ControllerUsuario.instanceFromDB(id_usuario=5)
    # print(teste)
    pass