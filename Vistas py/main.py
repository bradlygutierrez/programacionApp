import PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic.properties import QtWidgets

from IniciarSesion import Ui_iniciarSesion
from recuperarContraseña import Ui_recuperarContrasena
from crearCuenta import Ui_crearUsuario


class MainWindow(QMainWindow):
    """Main application window, handles the workflow of secondary windows"""

    def __init__(self):
        super().__init__()

        # Set up main window
        self.ui = Ui_iniciarSesion()
        self.ui.setupUi(self)

        # Connect button to show second window
        self.ui.commandLinkButton_2.clicked.connect(self.show_second_window)
        self.ui.commandLinkButton.clicked.connect(self.show_third_window)

    def show_second_window(self):
        # Hide main window
        self.hide()

        # Show second window
        self.second_window = QMainWindow()
        self.ui2 = Ui_crearUsuario()
        self.ui2.setupUi(self.second_window)
        self.ui2.pushButton.clicked.connect(self.close)
        self.second_window.show()
        self.ui2.pushButton.clicked.connect(self.show_main_window)

    def show_third_window(self):
        # Hide main window
        self.hide()

        # Show third window
        self.third_window = QMainWindow()
        self.ui3 = Ui_recuperarContrasena()
        self.ui3.setupUi(self.third_window)
        self.ui3.pushButton.clicked.connect(self.close)
        self.third_window.show()

    def show_main_window(self):
        self.hide()

        # Show main window
        self.main_window = QMainWindow()
        self.ui4 = self
        self.ui4.pushButton.clicked.connect(self.close)
        self.main_window.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
