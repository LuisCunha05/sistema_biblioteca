import sys
from typing import List
from biblioteca.model.livro import Livro, LivroBuilder
from biblioteca.model import usuario
from biblioteca.controller.controller_usuario import ControllerUsuario
from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QStackedWidget
from biblioteca.view.login import Login
from biblioteca.view.inicio import Inicio
from biblioteca.view.gerenciar_livro import GerenciarLivro
from biblioteca.view.cadastrar_livro import CadastroLivro
from biblioteca.view.cadastrar_usuario import CadastrarUsuario


class MainWindown(QStackedWidget):
    def __init__(self) -> None:
        super().__init__()
        self.showLogin()
    
    def showLogin(self):
        if(not hasattr(self, 'tela_login')):
            self.tela_login = Login()
            self.tela_login.b_entrar.clicked.connect(self.showGerenciarLivro)
            self.tela_login.b_cadastrar.clicked.connect(lambda x: self.showCadastrarUsuario(False))
            self.addWidget(self.tela_login)
        
        self.setCurrentWidget(self.tela_login)
    
    def showInicio(self):
        if(not hasattr(self, 'tela_inicio')):
            self.tela_inicio = Inicio()
            self.tela_inicio.b_sair.clicked.connect(self.showLogin)
            self.addWidget(self.tela_inicio)
        
        self.setCurrentWidget(self.tela_inicio)
    
    def showGerenciarLivro(self):
        if(not hasattr(self, 'tela_gerenciar_livro')):
            self.tela_gerenciar_livro = GerenciarLivro()
            self.tela_gerenciar_livro.b_inicio.clicked.connect(self.showInicio)
            self.tela_gerenciar_livro.b_cadastrar.clicked.connect(self.showCadastrarLivro)
            self.addWidget(self.tela_gerenciar_livro)
        
        self.setCurrentWidget(self.tela_gerenciar_livro)
    
    def showCadastrarLivro(self):
        if(not hasattr(self, 'tela_cadastrar_livro')):
            self.tela_cadastrar_livro = CadastroLivro()
            self.tela_cadastrar_livro.b_inicio.clicked.connect(self.showInicio)
            self.addWidget(self.tela_cadastrar_livro)
        
        self.setCurrentWidget(self.tela_cadastrar_livro)

    def showCadastrarUsuario(self, isAdmin: bool):
        if(not hasattr(self, 'tela_cadastrar_usuario')):
            self.tela_cadastrar_usuario = CadastrarUsuario()
            self.tela_cadastrar_usuario.b_inicio.clicked.connect(self.showInicio)
            self.addWidget(self.tela_cadastrar_usuario)
        
        self.setCurrentWidget(self.tela_cadastrar_usuario)

        if(isAdmin):
            self.tela_cadastrar_usuario.showAdminOption()
        else:
            self.tela_cadastrar_usuario.hideAdminOption()
        self.tela_cadastrar_usuario.hideInicioOption()

class App(QApplication):
    def __init__(self, argv: List[str]) -> None:
        super().__init__(argv)
        self.tela_mainwindown = MainWindown()
        self.tela_mainwindown.show()


if __name__ == '__main__':
    app = App(sys.argv)

    sys.exit(app.exec())
