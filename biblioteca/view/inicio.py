import sys
from PyQt6.uic.load_ui import loadUi
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QMessageBox, QLabel, QStackedWidget
from ..util import basePath


class Inicio(QWidget):
    def __init__(self) -> None:
        super().__init__()
        loadUi(basePath('biblioteca\\view\\layouts\\inicio.ui') ,self)
        self.b_sair:QPushButton
