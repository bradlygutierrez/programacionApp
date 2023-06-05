import PyQt5
import sys
from PyQt5 import QtCore
from decimal import Decimal
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from Datos.dtGasto import DT_gasto
from IniciarSesion import Ui_iniciarSesion
from entidades.gasto import Gasto
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
from Datos.dtUsuario import DT_Usuario
from entidades.usuario import Usuario
from Datos.dtPregunta import DT_pregunta
from PreguntarUsuario import Ui_UsuarioRecuperar
from OlvidasteContra import Ui_PreguntaContra
from CambiarContra import Ui_NuevaContra
class MainWindow(QMainWindow):
    """Main application window, handles the workflow of secondary windows"""

    def __init__(self):
        super().__init__()
        self.nombre_proyecto = ""
        self.ui = Ui_iniciarSesion()
        self.ui.setupUi(self)
        self.nombre_editar = ""
        self.verificador = 1
        self.id_usuario = 0
        self.ui.commandLinkButton_2.clicked.connect(self.show_crear_usuario)
        self.ui.commandLinkButton.clicked.connect(self.show_recuperar_contrasena)
        self.ui.commandLinkButton_3.clicked.connect(sys.exit)
        self.ui.pushButton.clicked.connect(self.mostrar_proyectos_especificos)

    def creacion_usuario(self):
        correo = self.uiCrearUsuario.lineEdit.text()
        nombre_usuario = self.uiCrearUsuario.lineEdit_4.text()
        clave = self.uiCrearUsuario.lineEdit_3.text()
        confirmar_clave = self.uiCrearUsuario.lineEdit_5.text()
        respuesta = self.uiCrearUsuario.lineEdit_6.text()
        pregunta = self.uiCrearUsuario.comboBox.currentData()

        if confirmar_clave != clave:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Sermiccsa")
            mensaje.setText("Las claves no coinciden, intenta de nuevo")
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.exec_()
        else:
            if(DT_Usuario.existe_solo_usuario(DT_Usuario, nombre_usuario)):
                mensaje = QMessageBox()
                mensaje.setWindowTitle("Sermiccsa")
                mensaje.setText("Usuario ya existe. Intente de nuevo")
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.exec_()
            else:
                usuario_a_guardar = Usuario(1, nombre_usuario, correo, pregunta, clave, respuesta)
                DT_Usuario.guardarUsuario(usuario_a_guardar)
                self.show_main_window()



    def show_crear_usuario(self):

        if self.verificador == 1:
            self.close()
        elif self.verificador == 2:
            self.uiPrincipal.close()
        elif self.verificador == 3:
            self.uiCrearUsuario.close()
        else:
            pass

        self.verificador = 3

        # Hide main window
        self.uiCrearUsuario = Ui_crearUsuario()
        self.uiCrearUsuario.setupUi(self.uiCrearUsuario)
        self.uiCrearUsuario.pushButton.clicked.connect(self.show_main_window)
        self.uiCrearUsuario.pushButton_5.clicked.connect(self.creacion_usuario)
        self.uiCrearUsuario.cargar_preguntas()
        self.uiCrearUsuario.show()

    def solucionar_recuperacion(self):
        nuevaClave = self.uiNuevaContra.lineEdit.text()
        nuevaClave1 = self.uiNuevaContra.lineEdit_2.text()
        if(nuevaClave == nuevaClave1):
            DT_Usuario.actualizar_clave(DT_Usuario, self.nombre_editar, nuevaClave)
            self.show_main_window()
        else:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Sermiccsa")
            mensaje.setText("Las claves no coinciden. Intente de nuevo")
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.exec_()
            self.manejar_pregunta_respuesta()


    def manejar_pregunta_respuesta(self):
        respuesta = self.uiPreguntaRespuesta.lineEdit.text()
        if(DT_Usuario.verificar_respuesta(DT_Usuario, self.nombre_editar, respuesta)):
            self.uiPreguntaRespuesta.close()
            self.verificador = 15
            self.uiNuevaContra = Ui_NuevaContra()
            self.uiNuevaContra.setupUi(self.uiNuevaContra)
            self.uiNuevaContra.pushButton.clicked.connect(self.recuperando_clave)
            self.uiNuevaContra.pushButton_2.clicked.connect(self.solucionar_recuperacion)
            self.uiNuevaContra.show()
        else:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Sermiccsa")
            mensaje.setText("Respuesta invalida. Intente de nuevo")
            mensaje.setIcon(QMessageBox.Critical)
            mensaje.exec_()
            self.recuperando_clave()


    def recuperando_clave(self):
        self.nombre_editar = self.uiUsuarioRecuperar.lineEdit.text()
        self.id_pregunta = DT_Usuario.buscar_pregunta(DT_Usuario, self.nombre_editar)
        self.pregunta = DT_pregunta.buscar_pregunta(DT_pregunta, self.id_pregunta)

        if(DT_Usuario.existe_solo_usuario(DT_Usuario, self.nombre_editar)):
            if self.verificador == 4:
                self.uiUsuarioRecuperar.close()
            elif self.verificador == 15:
                self.uiNuevaContra.close()

            self.verificador = 14
            self.uiPreguntaRespuesta = Ui_PreguntaContra()
            self.uiPreguntaRespuesta.setupUi(self.uiPreguntaRespuesta)
            self.uiPreguntaRespuesta.lineEdit_2.setText(self.pregunta)
            self.uiPreguntaRespuesta.pushButton.clicked.connect(self.show_recuperar_contrasena)
            self.uiPreguntaRespuesta.pushButton_2.clicked.connect(self.manejar_pregunta_respuesta)
            self.uiPreguntaRespuesta.show()
        else:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Sermiccsa")
            mensaje.setText("Usuario no encontrado. Intente de nuevo")
            mensaje.setIcon(QMessageBox.Information)
            mensaje.exec_()
            self.show_recuperar_contrasena()


    def show_recuperar_contrasena(self):
        if self.verificador == 1:
            self.close()
        elif self.verificador == 2:
            self.uiPrincipal.close()
        elif self.verificador == 4:
            self.uiUsuarioRecuperar.close()
        elif self.verificador == 14:
            self.uiPreguntaRespuesta.close()
        else:
            pass

        # Hide main window
        # Show third window
        self.verificador = 4

        self.uiUsuarioRecuperar = Ui_UsuarioRecuperar()
        self.uiUsuarioRecuperar.setupUi(self.uiUsuarioRecuperar)
        self.uiUsuarioRecuperar.pushButton.clicked.connect(self.show_main_window)
        self.uiUsuarioRecuperar.pushButton_2.clicked.connect(self.recuperando_clave)
        self.uiUsuarioRecuperar.show()

    def mostrar_proyectos_especificos(self):
        if self.verificador == 1:
            nombre = self.ui.lineEdit.text()
            clave = self.ui.lineEdit_2.text()
            self.verificadorInterno = 1
        elif self.verificador == 2:
            nombre = self.uiPrincipal.lineEdit.text()
            clave = self.uiPrincipal.lineEdit_2.text()
            self.verificadorInterno = 2
        else:
            pass

        if(DT_Usuario.existe_usuario(DT_Usuario, nombre, clave)):
            self.id_usuario = DT_Usuario.conseguir_id_usuario(DT_Usuario, nombre, clave)
            self.show_proyectos()
        else:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("SERMICCSA")
            mensaje.setText("No encontramos tus credenciales ¡Intenta de nuevo!")
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.exec_()
            if self.verificador == 1:
                self.ui.lineEdit.setText("")
                self.ui.lineEdit_2.setText("")

            elif self.verificador == 2:
                self.uiPrincipal.lineEdit.setText("")
                self.uiPrincipal.lineEdit_2.setText("")
            else:
                pass


    def show_main_window(self):

        if self.verificador == 3:
            self.uiCrearUsuario.close()
        elif self.verificador == 4:
            self.uiUsuarioRecuperar.close()

        elif self.verificador == 1:
            self.close()
        elif self.verificador == 15:
            self.uiNuevaContra.close()
        elif self.verificador == 7:
            self.uiConfiguracion.close()
        else:
            pass

        self.verificador = 2

        self.uiPrincipal = Ui_iniciarSesion()
        self.uiPrincipal.setupUi(self.uiPrincipal)

        # Connect button to show second window
        self.uiPrincipal.commandLinkButton_2.clicked.connect(self.show_crear_usuario)
        self.uiPrincipal.commandLinkButton.clicked.connect(self.show_recuperar_contrasena)
        self.uiPrincipal.commandLinkButton_3.clicked.connect(sys.exit)
        self.uiPrincipal.pushButton.clicked.connect(self.mostrar_proyectos_especificos)
        self.uiPrincipal.show()

    def show_proyectos(self):

        if self.verificador == 1:
            self.close()
        elif self.verificador == 2:
            self.uiPrincipal.close()
        elif self.verificador == 6:
            self.uiNuevoproyecto.close()
        elif self.verificador == 8:
            self.uiVerificar.close()
        elif self.verificador == 7:
            self.uiConfiguracion.close()
        elif self.verificador == 10:
            self.uiproyectoX.close()
        else:
            pass

        self.verificador = 5

        self.uiProyectos = Ui_proyectos()
        self.uiProyectos.setupUi(self.uiProyectos)
        self.uiProyectos.pushButton_4.clicked.connect(self.show_nuevo_proyecto)
        self.uiProyectos.pushButton_2.clicked.connect(self.show_configuracion)
        self.uiProyectos.tableWidget.cellDoubleClicked.connect(self.show_proyectoX_DAO)
        self.uiProyectos.pushButton_3.clicked.connect(self.verificar_eliminacion)
        self.uiProyectos.cargar_proyectos(self.id_usuario)
        self.uiProyectos.show()

    def eliminar_proyectos(self):
        try:
            row = self.uiProyectos.tableWidget.currentRow()
            self.nombre_proyecto = self.uiProyectos.tableWidget.item(row, 0).text()
            DT_proyect().eliminarProyecto(self.nombre_proyecto)
            self.show_proyectos()
        except Exception as e:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("SERMICCSA")
            mensaje.setText("No hay ninguna fila seleccionada")
            mensaje.setIcon(QMessageBox.Critical)
            mensaje.exec_()

    def verificar_eliminacion(self):
        if self.verificador == 5:
            self.uiProyectos.close()
        else:
            pass

        self.verificador = 8

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

        if self.verificador == 5:
            self.uiProyectos.close()
        else:
            pass

        self.verificador = 6

        self.uiNuevoproyecto = Ui_nuevoProyecto()
        self.uiNuevoproyecto.setupUi(self.uiNuevoproyecto)
        self.uiNuevoproyecto.pushButton.clicked.connect(self.show_proyectos)
        self.uiNuevoproyecto.pushButton_2.clicked.connect(self.save_nuevo_proyecto)
        self.uiNuevoproyecto.show()
    def cambiar_clave(self):
        nombre_usuario = DT_Usuario.conseguir_nombre(DT_Usuario, self.id_usuario)
        clave_actual = self.uiConfiguracion.lineEdit.text()
        nueva_clavecita = self.uiConfiguracion.lineEdit_2.text()
        nueva_clavecita2 = self.uiConfiguracion.lineEdit_3.text()

        if(DT_Usuario.existe_usuario(DT_Usuario, nombre_usuario, clave_actual)):
            if nueva_clavecita == nueva_clavecita2:
                DT_Usuario.actualizar_clave(DT_Usuario,nombre_usuario,nueva_clavecita)
                self.show_main_window()
            else:
                mensaje = QMessageBox()
                mensaje.setWindowTitle("SERMICCSA")
                mensaje.setText("Las claves ingresadas no coinciden")
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.exec_()
        else:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("SERMICCSA")
            mensaje.setText("Su clave actual no coincide. Intente de nuevo!")
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.exec_()

    def cambiar_nombre(self):
        nuevo_nombre = self.uiConfiguracion.lineEdit_4.text()

        if(DT_Usuario.existe_solo_usuario(DT_Usuario, nuevo_nombre)):
            mensaje = QMessageBox()
            mensaje.setWindowTitle("SERMICCSA")
            mensaje.setText("Elija otro nombre de usuario, el que desea, esta ocupado")
            mensaje.setIcon(QMessageBox.Critical)
            mensaje.exec_()
        else:
            DT_Usuario.actualizar_nombre(DT_Usuario, self.id_usuario, nuevo_nombre)
            self.show_main_window()


    def show_configuracion(self):

        self.verificador = 7
        self.uiProyectos.close()
        self.uiConfiguracion = Ui_configuracion()
        self.uiConfiguracion.setupUi(self.uiConfiguracion)
        self.uiConfiguracion.pushButton_3.clicked.connect(self.show_proyectos)
        self.uiConfiguracion.pushButton_4.clicked.connect(self.cambiar_clave)
        self.uiConfiguracion.pushButton_5.clicked.connect(self.cambiar_nombre)
        self.uiConfiguracion.show()

    def show_proyectoX_DAO(self):
        row = self.uiProyectos.tableWidget.currentRow()
        self.nombre_proyecto = self.uiProyectos.tableWidget.item(row, 0).text()
        self.proyecto_actual = DT_proyect().encontrarProyecto(self.nombre_proyecto)
        etapas = DT_etapa.encontrar_gastos_totales(DT_etapa, self.proyecto_actual.id_proyecto)
        self.total_gastos = DT_gasto.calcular_total_gastos(DT_gasto, etapas)
        print(self.total_gastos)
        self.show_proyectoX()

    def show_proyectoX(self):
        if self.verificador == 5:
            self.uiProyectos.close()
        elif self.verificador == 11:
            self.uiagregargasto.close()
        elif self.verificador == 12:
            self.uiverEtapas.close()
        elif self.verificador == 9:
            self.uietapas.close()
        else:
            pass

        self.verificador = 10

        self.uiproyectoX = Ui_proyectoX()
        self.uiproyectoX.setupUi(self.uiproyectoX)
        self.uiproyectoX.pushButton_4.clicked.connect(self.show_proyectos)
        self.uiproyectoX.pushButton_2.clicked.connect(self.show_agregar_gasto)
        self.uiproyectoX.pushButton.clicked.connect(self.show_ver_etapa)
        etapas = DT_etapa.encontrar_gastos_totales(DT_etapa, self.proyecto_actual.id_proyecto)
        self.uiproyectoX.cargar_proyectoX(self.proyecto_actual, Decimal(self.proyecto_actual.presupuesto_inicial) - self.total_gastos, etapas)
        self.uiproyectoX.show()

    def show_agregar_gasto(self):
        self.verificador= 11
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

    def save_agregarGasto(self):
        nombre = self.uiagregargasto.lineEdit.text()
        descripcion = self.uiagregargasto.lineEdit_2.text()
        referencia = self.uiagregargasto.lineEdit_3.text()
        subtotal = self.uiagregargasto.lineEdit_4.text()
        ir = self.uiagregargasto.lineEdit_5.text()
        IVA = self.uiagregargasto.lineEdit_6.text()
        GastoGuardar = Gasto(self._idGasto,nombre,descripcion,referencia,subtotal,ir,IVA)
        DT_gasto.guardarGasto(GastoGuardar)


    def limpiar_campos_guardar_beneficiario(self):
        self.uiagregargasto.lineEdit_8.setText("")
        self.uiagregargasto.lineEdit_7.setText("")

    def show_etapas(self):
        if self.verificador == 10:
            self.uiproyectoX.close()
        elif self.verificador == 13:
            self.uiespecificaciones.close()
        else:
            pass

        self.verificador = 12
        self.uietapas = Ui_Etapas()
        self.uietapas.setupUi(self.uietapas)
        self.uietapas.pushButton.clicked.connect(self.show_agregar_etapa)
        self.uietapas.pushButton_5.clicked.connect(self.show_nuevo_proyecto)
        self.uietapas.pushButton_4.clicked.connect(self.show_proyectoX)
        self.uietapas.cargar_etapas()
        self.uietapas.show()

    def show_agregar_etapa(self):
        self.verificador = 13

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


    #def generar_reporte(data): para los reportes


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
