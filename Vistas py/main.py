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
        self.ui = Ui_iniciarSesion()
        self.ui.setupUi(self)
        self.verificador = 0
        self.contador = 1
        self.ui.commandLinkButton_2.clicked.connect(self.show_crear_usuario)
        self.ui.commandLinkButton.clicked.connect(self.show_recuperar_contrasena)

    def show_crear_usuario(self):
        if self.contador == 1:
            self.close()
        else:
            self.uiPrincipal.close()

        self.verificador = 1

        # Hide main window
        self.uiCrearUsuario = Ui_crearUsuario()
        self.uiCrearUsuario.setupUi(self.uiCrearUsuario)
        self.uiCrearUsuario.pushButton.clicked.connect(self.show_main_window)
        self.uiCrearUsuario.show()


    def show_recuperar_contrasena(self):

        if self.contador == 1:
            self.close()
        else:
            self.uiPrincipal.close()

        # Hide main window
        # Show third window
        self.verificador = 0

        self.uiRecuperarContrasena = Ui_recuperarContrasena()
        self.uiRecuperarContrasena.setupUi(self.uiRecuperarContrasena)
        self.uiRecuperarContrasena.pushButton.clicked.connect(self.show_main_window)
        self.uiRecuperarContrasena.show()

    def show_main_window(self):
        if self.verificador == 1:
            self.uiCrearUsuario.close()
        else:
            self.uiRecuperarContrasena.close()

        self.contador = 2

        self.uiPrincipal = Ui_iniciarSesion()
        self.uiPrincipal.setupUi(self.uiPrincipal)

        # Connect button to show second window
        self.uiPrincipal.commandLinkButton_2.clicked.connect(self.show_crear_usuario)
        self.uiPrincipal.commandLinkButton.clicked.connect(self.show_recuperar_contrasena)
        self.uiPrincipal.pushButton.clicked.connect(self.show_main_window)
        self.uiPrincipal.show()


if __name__ == '__main__':
    import sys
    print("Hola Andre")
    print("Hola Bradly")
    print("Hola Jorge")
    print("Ultimo push")
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
