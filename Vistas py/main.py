import PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from IniciarSesion import Ui_iniciarSesion
from recuperarContraseña import Ui_recuperarContrasena
from crearCuenta import Ui_crearUsuario
from Proyectos import Ui_proyectos
from NuevoProyecto import Ui_nuevoProyecto
from Configuracion import Ui_configuracion
from Etapas import Ui_Etapas
from AgregarEtapa import Ui_AgregarEtapa
from ProyectoX import Ui_proyectoX
from Proyectos import Ui_proyectos
from Datos.dtProyecto import DT_proyect
from entidades.proyecto import Proyecto
from verificacionEliminacionProyecto import Ui_verificarEliminacion
from AgregarGasto import Ui_agregarGasto
from VerEtapas import Ui_VerEtapas
from EspecificacionesEtapas import Ui_Especificaciones_Etapas
from Datos.dtBeneficiario import DT_beneficiario
from entidades.beneficiario import Beneficiario
from entidades.etapas import Etapa
from Datos.dtEtapa import DT_etapa

class MainWindow(QMainWindow):
    """Main application window, handles the workflow of secondary windows"""

    def __init__(self):
        super().__init__()
        self.nombre_proyecto = ""
        self.ui = Ui_iniciarSesion()
        self.ui.setupUi(self)
        self.verificador = 0
        self.contador = 1
        self.controlador_proyectos = 7
        self.id_usuario = 1
        self.controlador_etapas = 10
        self.controlador_proyectoX = 12
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
        self.uiPrincipal.pushButton.clicked.connect(self.show_proyectos)
        self.uiPrincipal.show()

    def show_proyectos(self):
        if self.contador == 1:
            self.close()
        else:
            self.uiPrincipal.close()
        if self.controlador_proyectos == 1:
            self.uiNuevoproyecto.close()
        elif self.controlador_proyectos == 2:
            self.uiConfiguracion.close()
        elif self.controlador_proyectos == 3:
            self.uiEtapas.close()
        elif self.controlador_proyectos == 4:
            self.uiVerificar.close()
        elif self.controlador_proyectos == 5:
            self.uiproyectoX.close()
        else:
            print("Pasamos")

        self.uiProyectos = Ui_proyectos()
        self.uiProyectos.setupUi(self.uiProyectos)
        self.uiProyectos.pushButton_4.clicked.connect(self.show_nuevo_proyecto)
        self.uiProyectos.pushButton_2.clicked.connect(self.show_configuracion)
        self.uiProyectos.tableWidget.cellDoubleClicked.connect(self.show_proyectoX)
        self.uiProyectos.pushButton_3.clicked.connect(self.verificar_eliminacion)
        self.uiProyectos.cargar_proyectos()
        self.uiProyectos.show()

    def eliminar_proyectos(self):
        row = self.uiProyectos.tableWidget.currentRow()
        self.nombre_proyecto = self.uiProyectos.tableWidget.item(row, 0).text()
        DT_proyect().eliminarProyecto(self.nombre_proyecto)
        self.show_proyectos()

    def verificar_eliminacion(self):
        self.controlador_proyectos = 4
        self.uiVerificar = Ui_verificarEliminacion()
        self.uiVerificar.setupUi(self.uiVerificar)
        self.uiVerificar.pushButton_2.clicked.connect(self.eliminar_proyectos)
        self.uiVerificar.pushButton.clicked.connect(self.show_proyectos)
        self.uiVerificar.show()

    def limpiar_campos_guardar_proyecto(self):
        self.uiNuevoproyecto.lineEdit.setText("")
        self.uiNuevoproyecto.lineEdit.setText("")
        self.uiNuevoproyecto.lineEdit.setText("")
        self.uiNuevoproyecto.lineEdit.setText("")
        self.uiNuevoproyecto.lineEdit.setText("")

    def save_nuevo_proyecto(self):
        nombre = self.uiNuevoproyecto.lineEdit.text()
        presupuesto_inicial = self.uiNuevoproyecto.lineEdit_2.text()
        beneficiario = self.uiNuevoproyecto.lineEdit_3.text()
        fecha_inicio = self.uiNuevoproyecto.lineEdit_4.text()
        descripcion = self.uiNuevoproyecto.lineEdit_5.text()

        proyectoGuardar = Proyecto(5, self.id_usuario, fecha_inicio, nombre, descripcion, presupuesto_inicial, beneficiario)

        DT_proyect.guardarProyecto(proyectoGuardar)

        self.limpiar_campos_guardar_proyecto
        self.show_etapas()

    def show_nuevo_proyecto(self):
        if self.controlador_proyectoX == 2:
            self.uietapas.close()
        self.controlador_proyectos = 1
        self.uiProyectos.close()
        self.uiNuevoproyecto = Ui_nuevoProyecto()
        self.uiNuevoproyecto.setupUi(self.uiNuevoproyecto)
        self.uiNuevoproyecto.pushButton.clicked.connect(self.show_proyectos)
        self.uiNuevoproyecto.pushButton_2.clicked.connect(self.save_nuevo_proyecto)
        self.uiNuevoproyecto.show()

    def show_configuracion(self):
        self.controlador_proyectos = 2
        self.uiProyectos.close()
        self.uiConfiguracion = Ui_configuracion()
        self.uiConfiguracion.setupUi(self.uiConfiguracion)
        self.uiConfiguracion.pushButton.clicked.connect(self.show_proyectos)
        self.uiConfiguracion.show()

    def show_proyectoX(self):
        self.controlador_proyectos = 5
        if self.controlador_proyectos == 1:
            self.close()
        else:
            self.uiProyectos.close()

        if self.controlador_proyectoX == 1:
            self.uiagregargasto.close()
        elif self.controlador_proyectoX == 2:
            self.uietapas.close()
        elif self.controlador_proyectoX == 3:
            self.uiverEtapas.close()
        else:
            self.close()

        self.uiproyectoX = Ui_proyectoX()
        self.uiproyectoX.setupUi(self.uiproyectoX)
        self.uiproyectoX.pushButton_4.clicked.connect(self.show_proyectos)
        self.uiproyectoX.pushButton_2.clicked.connect(self.show_agregar_gasto)
        self.uiproyectoX.pushButton.clicked.connect(self.show_ver_etapa)
        self.uiproyectoX.cargar_proyectoX()
        self.uiproyectoX.show()

    def show_agregar_gasto(self):
        self.controlador_proyectoX = 1
        self.uiproyectoX.close()
        self.uiagregargasto = Ui_agregarGasto()
        self.uiagregargasto.setupUi(self.uiagregargasto)
        self.uiagregargasto.pushButton_4.clicked.connect(self.save_beneficiario)
        self.uiagregargasto.pushButton.clicked.connect(self.show_proyectoX)
        self.uiagregargasto.cargar_beneficiario()
        self.uiagregargasto.show()

    def save_beneficiario(self):
        nombre = self.uiagregargasto.lineEdit_7.text()
        identificacion = self.uiagregargasto.lineEdit_8.text()
        beneficiarioGuardar = Beneficiario(nombre, identificacion)
        DT_beneficiario.guardarBeneficiario(beneficiarioGuardar)
        self.limpiar_campos_guardar_beneficiario()
        self.show_agregar_gasto()

    def limpiar_campos_guardar_beneficiario(self):
        self.uiagregargasto.lineEdit_8.setText("")
        self.uiagregargasto.lineEdit_7.setText("")

    def show_etapas(self):
        if self.controlador_proyectos == 1:
            self.uiNuevoproyecto.close()
        self.controlador_proyectoX = 2

        if self.controlador_proyectoX == 5:
            self.close()
        else:
            self.uiProyectos.close()

        if self.controlador_etapas == 1:
            self.uiNuevaEtapa.close()
        elif self.controlador_etapas == 2:
            self.uiverEtapas.close()
        elif self.controlador_etapas == 3:
            self.uiEliminarEtapa.close()
        else:
            self.close()

        self.uietapas = Ui_Etapas()
        self.uietapas.setupUi(self.uietapas)
        self.uietapas.pushButton.clicked.connect(self.show_agregar_etapa)
        self.uietapas.pushButton_5.clicked.connect(self.show_nuevo_proyecto)
        self.uietapas.pushButton_4.clicked.connect(self.show_proyectoX)
        self.uietapas.cargar_etapas()
        self.uietapas.show()

    def show_agregar_etapa(self):
        self.controlador_etapas = 1

        self.uietapas.close()
        self.uiNuevaEtapa = Ui_AgregarEtapa()
        self.uiNuevaEtapa.setupUi(self.uiNuevaEtapa)
        self.uiNuevaEtapa.pushButton.clicked.connect(self.save_etapa)
        self.uiNuevaEtapa.pushButton_2.clicked.connect(self.show_etapas)
        self.uiNuevaEtapa.show()

    def save_etapa(self):
        numero_etapa = self.uiNuevaEtapa.lineEdit.text()
        nombre = self.uiNuevaEtapa.lineEdit_2.text()
        descripcion = self.uiNuevaEtapa.lineEdit_4.text()
        presupuesto = self.uiNuevaEtapa.lineEdit_3.text()
        etapaGuardar = Etapa(1, 5, nombre, descripcion, presupuesto, numero_etapa)
        DT_etapa.guardarEtapa(etapaGuardar)
        self.limpiar_campos_guardar_nueva_etapa()
        self.show_etapas()

    def eliminar_etapa(self):
        row = self.uiverEtapas.tableWidget.currentRow()
        self.nombre_etapa = self.uiverEtapas.tableWidget.item(row, 0).text()
        DT_etapa().eliminarEtapa(self.nombre_etapa)
        self.show_ver_etapa()

    def limpiar_campos_guardar_nueva_etapa(self):
        self.uiNuevaEtapa.lineEdit.setText("")
        self.uiNuevaEtapa.lineEdit_2.setText("")
        self.uiNuevaEtapa.lineEdit_3.setText("")
        self.uiNuevaEtapa.lineEdit_4.setText("")

    def show_ver_etapa(self):
        if self.controlador_etapas == 4:
            self.uiespecificaciones.close()
        self.controlador_proyectoX = 3

        self.uiproyectoX.close()
        self.uiverEtapas = Ui_VerEtapas()
        self.uiverEtapas.setupUi(self.uiverEtapas)
        self.uiverEtapas.pushButton.clicked.connect(self.show_proyectoX)
        self.uiverEtapas.pushButton_2.clicked.connect(self.eliminar_etapa)
        self.uiverEtapas.cargar_etapa()
        self.uiverEtapas.tableWidget.cellDoubleClicked.connect(self.show_especificaciones_etapas)
        self.uiverEtapas.show()

    def show_especificaciones_etapas(self):
        self.controlador_etapas = 4

        self.uiverEtapas.close()
        self.uiespecificaciones = Ui_Especificaciones_Etapas()
        self.uiespecificaciones.setupUi(self.uiespecificaciones)
        self.uiespecificaciones.pushButton.clicked.connect(self.show_ver_etapa)
        self.uiespecificaciones.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
