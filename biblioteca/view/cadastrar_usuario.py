from PyQt6.QtCore import Qt
from PyQt6.uic.load_ui import loadUi
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QLabel, QMainWindow, QRadioButton
from ..util import basePath


class CadastrarUsuario(QWidget):
    def __init__(self) -> None:
        super().__init__()

        loadUi(basePath('biblioteca\\view\\layouts\\cadastrar_usuario.ui'), self)
        self.b_inicio:QPushButton
        self.r_admin: QRadioButton
        self.b_cadastrar:QPushButton
    
    def hideAdminOption(self):
        print(self.r_admin.isVisible())
        if(self.r_admin.isVisible()):
            self.r_admin.hide()
    
    def showAdminOption(self):
        print(self.r_admin.isVisible())
        if(not self.r_admin.isVisible()):
            self.r_admin.show()
    
    def showInicioOption(self):
        if(not self.b_inicio.isVisible()):
            self.b_inicio.show()
    
    def hideInicioOption(self):
        if(self.b_inicio.isVisible()):
            self.b_inicio.hide()