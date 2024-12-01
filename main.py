import sys
from typing import List
from biblioteca.model.livro import Livro, LivroBuilder
from biblioteca.model import usuario
from biblioteca.controller.controller_usuario import ControllerUsuario
from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QStackedWidget
from biblioteca.view.login import Login
from biblioteca.view.cadastrar_livro import CadastroLivro

class App(QApplication):
    def __init__(self, argv: List[str]) -> None:
        super().__init__(argv)
        self.tela_login = Login()
        self.tela_login.b_entrar.clicked.connect(self.clica)
        self.tela_login.show()

    def clica(self):
        if(not hasattr(self, 'tela_cl')):
            self.tela_cl = CadastroLivro()
            self.tela_cl.b_inicio.clicked.connect(self.clica2)
        
        self.tela_cl.show()
        self.tela_login.hide()
        return
    
    def clica2(self):
        print('kcta')
        self.tela_cl.hide()
        self.tela_login.show()

if __name__ == '__main__':
    app = App(sys.argv)

    sys.exit(app.exec())
