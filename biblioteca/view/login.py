import sys
from PyQt6.QtCore import Qt
from PyQt6.uic.load_ui import loadUi
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QLabel, QMainWindow
from ..util import basePath


class Login(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.b_entrar:QPushButton

        loadUi(basePath('biblioteca\\view\\layouts\\login.ui') ,self)




if __name__ == "__main__":

    app = QApplication(sys.argv)


    tela = Login()
    tela.show()

    #Finaliza e sinaliza o fechamento do app para o windows
    sys.exit(app.exec())
