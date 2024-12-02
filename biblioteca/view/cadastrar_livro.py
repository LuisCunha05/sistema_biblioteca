import sys
from PyQt6.QtCore import Qt
from PyQt6.uic.load_ui import loadUi
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QLabel, QMainWindow
from ..util import basePath


class CadastroLivro(QWidget):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent=parent)

        loadUi(basePath('biblioteca\\view\\layouts\\cadastro_livro.ui'), self)
        self.b_inicio:QPushButton
        self.b_inicio.setText('Opa')