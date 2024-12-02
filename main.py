import sys
from typing import List
from biblioteca.model.livro import Livro, LivroBuilder
from biblioteca.model import usuario
from biblioteca.controller.controller_usuario import ControllerUsuario
from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QStackedWidget
from biblioteca.view.login import Login
from biblioteca.view.cadastrar_livro import CadastroLivro

class MainWindown(QStackedWidget):
    def __init__(self) -> None:
        super().__init__()
        self.showLogin()
    
    def showLogin(self):
        if(not hasattr(self, 'tela_login')):
            self.tela_login = Login()
            self.tela_login.b_entrar.clicked.connect(self.showInicio)
            self.addWidget(self.tela_login)
        
        self.setCurrentWidget(self.tela_login)
    
    def showInicio(self):
        if(not hasattr(self, 'tela_inicio')):
            self.tela_inicio = CadastroLivro()
            self.tela_inicio.b_inicio.clicked.connect(self.showLogin)
            self.addWidget(self.tela_inicio)
        
        self.setCurrentWidget(self.tela_inicio)

class App(QApplication):
    def __init__(self, argv: List[str]) -> None:
        super().__init__(argv)
        self.tela_mainwindown = MainWindown()
        self.tela_mainwindown.show()


if __name__ == '__main__':
    app = App(sys.argv)

    sys.exit(app.exec())
