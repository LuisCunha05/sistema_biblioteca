import sys
from PyQt6.QtCore import Qt
from PyQt6.uic.load_ui import loadUi
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QMessageBox, QTableWidget
from ..util import basePath


class GerenciarLivro(QWidget):
    def __init__(self) -> None:
        super().__init__()

        loadUi(basePath('biblioteca\\view\\layouts\\gerenciar_livro.ui'), self)
        self.b_inicio:QPushButton
        self.table_livro: QTableWidget
        
        self.table_livro.setColumnWidth(0, 180)
        self.table_livro.setColumnWidth(1, 180)
        self.table_livro.setColumnWidth(2, 180)
        self.table_livro.setColumnWidth(3, 100)
        self.table_livro.setColumnWidth(4, 100)