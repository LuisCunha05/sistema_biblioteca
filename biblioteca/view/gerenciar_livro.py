from PyQt6.QtCore import Qt
from PyQt6.uic.load_ui import loadUi
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem
from ..util import basePath


class GerenciarLivro(QWidget):
    def __init__(self) -> None:
        super().__init__()

        loadUi(basePath('biblioteca\\view\\layouts\\gerenciar_livro.ui'), self)
        #------------------------------------Type Annotation------------------------------------#
        self.b_inicio:QPushButton
        self.b_alterar:QPushButton
        self.table_livro: QTableWidget
        

        #------------------------------------ Configuration ------------------------------------#
        self.table_livro.setColumnWidth(0, 180)
        self.table_livro.setColumnWidth(1, 180)
        self.table_livro.setColumnWidth(2, 180)
        self.table_livro.setColumnWidth(3, 100)
        self.table_livro.setColumnWidth(4, 100)
        self.b_alterar.clicked.connect(lambda x: self.adicionarLinha((1,'a','b','c',3, 'd')))

    def adicionarLinha(self, data: tuple[int,str,str,str,int,str]):
        """
            Adiciona uma nova linha a tabela

            Arguments
            ---------
            data: tuple[int,str,str,str,int,str] = id_livro, titulo, autor, genero, status, isbn
        """
        self.table_livro.insertRow(self.table_livro.rowCount())

        id_livro, titulo, autor, genero, status, isbn = data

        row = self.table_livro.rowCount() - 1
        self.table_livro.setItem(row, 0, QTableWidgetItem(titulo))
        self.table_livro.setItem(row, 1, QTableWidgetItem(autor))
        self.table_livro.setItem(row, 2, QTableWidgetItem(genero))
        self.table_livro.setItem(row, 3, QTableWidgetItem(isbn))
        self.table_livro.setItem(row, 4, QTableWidgetItem(str(status)))