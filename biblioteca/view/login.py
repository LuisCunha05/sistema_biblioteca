import sys
from PyQt6.QtCore import Qt
from PyQt6.uic.load_ui import loadUi
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QLabel, QMainWindow
from ..util import basePath


class Login(QWidget):
    def __init__(self) -> None:
        super().__init__()

        loadUi(basePath('biblioteca\\view\\layouts\\login.ui'), self)
        self.b_entrar:QPushButton





if __name__ == "__main__":

    app = QApplication(sys.argv)

    tela = Login()
    tela.show()

    #Finaliza e sinaliza o fechamento do app para o windows
    sys.exit(app.exec())
