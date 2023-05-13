import PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic.properties import QtWidgets

from IniciarSesion import Ui_iniciarSesion
from recuperarContraseña import Ui_recuperarContrasena
from crearCuenta import Ui_crearUsuario
from Proyectos import Ui_proyectos
from NuevoProyecto import Ui_NuevoProyecto


class MainWindow(QMainWindow):
    """Main application window, handles the workflow of secondary windows"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_iniciarSesion()
        self.ui.setupUi(self)
        self.verificador = 0
        self.contador = 1
        self.controlador_proyectos = 0
        self.ui.commandLinkButton_2.clicked.connect(self.show_crear_usuario)
        self.ui.commandLinkButton.clicked.connect(self.show_recuperar_contrasena)
        self.ui.pushButton.clicked.connect(self.show_proyectos)

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
        self.uiRecuperarContrasena.pushButton.clicked.connect(self.show_proyectos)
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

    def show_proyectos(self):
        if self.contador == 1:
            self.close()
        elif:
            self.uiPrincipal.close()

        if self.controlador_proyectos == 1:
            self.show_proyectos.close()
        else:


        self.uiproyectos = Ui_proyectos()
        self.uiproyectos.setupUi(self.uiproyectos)
        self.uiproyectos.pushButton_4.clicked.connect(self.show_Nuevo_Proyecto)
        self.uiproyectos.show()

    def show_Nuevo_Proyecto(self):

        self.controlador_proyectos = 1
        self.uiproyectos.close()
        self.uinuevoproyecto = Ui_NuevoProyecto()
        self.uinuevoproyecto.setupUi(self.uinuevoproyecto)
        self.uinuevoproyecto.pushButton.clicked.connect(self.show_Nuevo_Proyecto)
        self.uinuevoproyecto.show()

    def regresar_proyectos




if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
