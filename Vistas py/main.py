import PyQt5
import sys
from PyQt5 import QtCore
import xlsxwriter
from Datos.dtFactura import DT_factura
from entidades.factura import Factura
import datetime
from Referencias import Ui_referencia
from decimal import Decimal
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from Datos.dtGasto import DT_gasto
from IniciarSesion import Ui_iniciarSesion
from entidades.gasto import Gasto
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
from ContraNueva import Ui_NuevaContra

class MainWindow(QMainWindow):
    """Main application window, handles the workflow of secondary windows"""

    def __init__(self):
        super().__init__()
        self.total_gastos = 0
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
        elif self.verificador == 9:
            self.uietapas.close()
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
        try:
            nombre = self.uiNuevoproyecto.lineEdit.text()
            presupuesto_inicial = self.uiNuevoproyecto.lineEdit_2.text()
            beneficiario = self.uiNuevoproyecto.lineEdit_3.text()
            fecha_inicio = self.uiNuevoproyecto.lineEdit_4.text()
            descripcion = self.uiNuevoproyecto.lineEdit_5.text()

            self.proyectoGuardar = Proyecto(5, self.id_usuario, fecha_inicio, nombre, descripcion, presupuesto_inicial, beneficiario)

            DT_proyect.guardarProyecto(self.proyectoGuardar)

            self.limpiar_campos_guardar_proyecto

            self.proyectoGuardado = DT_proyect.encontrarProyecto(DT_proyect, self.proyectoGuardar.nombre)

            self.show_etapas()
        except:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("SERMICCSA")
            mensaje.setText("Error al guardar proyecto, intente de nuevo")
            mensaje.setIcon(QMessageBox.Critical)
            mensaje.exec_()
            self.show_nuevo_proyecto()


    def show_nuevo_proyecto(self):

        if self.verificador == 5:
            self.uiProyectos.close()
        elif self.verificador == 9:
            self.uietapas.close()
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
        self.uiproyectoX.pushButton_2.clicked.connect(self.generar_reporte) #Imprimir
        self.uiproyectoX.pushButton.clicked.connect(self.show_ver_etapa) #Ver gasto por etapa
        self.uiproyectoX.pushButton_3.clicked.connect(self.show_agregar_gasto) #Agregar Gasto
        self.uiproyectoX.pushButton_4.clicked.connect(self.show_proyectos) #Salir
        etapas = DT_etapa.encontrar_gastos_totales(DT_etapa, self.proyecto_actual.id_proyecto)
        self.uiproyectoX.cargar_proyectoX(self.proyecto_actual, Decimal(self.proyecto_actual.presupuesto_inicial) - self.total_gastos)
        self.uiproyectoX.show()

    def show_agregar_gasto(self):
        if self.verificador == 10:
            self.uiproyectoX.close()
        elif self.verificador == 17:
            self.uiReferencia.close()
        else:
            pass

        self.verificador = 11
        self.uiagregargasto = Ui_agregarGasto()
        self.uiagregargasto.setupUi(self.uiagregargasto)
        self.uiagregargasto.pushButton_4.clicked.connect(self.show_proyectoX)
        self.uiagregargasto.pushButton_3.clicked.connect(self.save_beneficiario)
        self.uiagregargasto.cargar_combo_box(self.proyecto_actual.id_proyecto)
        self.uiagregargasto.show()

    def actual_beneficiario(self):
        DT_beneficiario.editar_beneficiario(DT_beneficiario, self.beneficiarioGuardado.id_Beneficiario, self.beneficiarioGuardar.nombre)
        bene = DT_beneficiario.buscar_beneficiario_por_referencia(DT_beneficiario, self.beneficiarioGuardar.identificacion)
        self.G_id_beneficiaro = bene.id_Beneficiario
        self.uiReferencia.close()
        self.controlador_beneficiario = True
        self.es_nuevo_beneficiario = False
        self.save_factura()

    def viejo_beneficiario(self):
        self.G_id_beneficiaro = self.beneficiarioGuardado.id_Beneficiario
        self.uiReferencia.close()
        self.controlador_beneficiario: False
        self.es_nuevo_beneficiario = False
        self.save_factura()

    def nuevo_beneficiario(self):
        bene = DT_beneficiario.buscar_beneficiario_por_referencia(DT_beneficiario, self.beneficiarioGuardar.identificacion)
        self.G_id_beneficiaro = bene.id_Beneficiario
        self.controlador_beneficiario: False
        self.es_nuevo_beneficiario = True
        self.save_factura()



    def save_factura(self):
        try:
            fecha = datetime.date.today()
            referencia = self.uiagregargasto.lineEdit_3.text()
            subtotal = float(self.uiagregargasto.lineEdit_4.text())
            ir = float(self.uiagregargasto.lineEdit_5.text())
            if self.uiagregargasto.checkBox.isChecked():
                iva = True
            else:
                iva = False
            self.factura_nueva = Factura(1, fecha, referencia, subtotal, ir, iva)
            DT_factura.guardarFactura(self.factura_nueva)
            factu = DT_factura.buscar_usuario_por_referencia(DT_factura, self.factura_nueva.referencia)
            self.G_id_factura = factu.idFactura
            self.save_agregarGasto()
        except:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("SERMICCSA")
            mensaje.setText("No se logro guardar tu factura")
            mensaje.setIcon(QMessageBox.Critical)
            mensaje.exec_()
            if self.es_nuevo_beneficiario:
                DT_beneficiario.eliminar_beneficiario(DT_beneficiario, self.G_id_beneficiaro)
            else:
                if self.controlador_beneficiario:
                    DT_beneficiario.editar_beneficiario(DT_beneficiario, self.beneficiarioGuardado.id_Beneficiario, self.beneficiarioGuardado.nombre)
            self.show_proyectoX()


    def save_beneficiario(self):
        nombre = self.uiagregargasto.lineEdit_6.text()
        identificacion = self.uiagregargasto.lineEdit_7.text()
        self.beneficiarioGuardar = Beneficiario(3, nombre, identificacion)

        if(DT_beneficiario.buscar_referencia(DT_beneficiario, identificacion)):
            self.beneficiarioGuardado = DT_beneficiario.buscar_beneficiario_por_referencia(DT_beneficiario, identificacion)
            self.verificador = 17
            self.uiReferencia = Ui_referencia()
            self.uiReferencia .setupUi(self.uiReferencia)
            self.uiReferencia.label_10.setText(str(self.beneficiarioGuardado.nombre))
            self.uiReferencia.label_11.setText(str(self.beneficiarioGuardado.identificacion))
            self.uiReferencia.label_13.setText(str(nombre))
            self.uiReferencia.label_12.setText(str(identificacion))
            self.uiReferencia.pushButton.clicked.connect(self.show_agregar_gasto)
            self.uiReferencia.pushButton_2.clicked.connect(self.viejo_beneficiario)
            self.uiReferencia.pushButton_3.clicked.connect(self.actual_beneficiario)
            self.uiagregargasto.close()
            self.uiReferencia.show()
        else:
            DT_beneficiario.guardarBeneficiario(self.beneficiarioGuardar)
            self.nuevo_beneficiario()

    def save_agregarGasto(self):
        try:
            nombre = self.uiagregargasto.lineEdit.text()
            descripcion = self.uiagregargasto.lineEdit_2.text()
            id_rubro = self.uiagregargasto.comboBox_2.currentData()
            id_etapa = self.uiagregargasto.comboBox_3.currentData()
            print(id_rubro)
            print(id_etapa)
            GastoGuardar = Gasto(3, id_etapa, id_rubro, self.G_id_factura, self.G_id_beneficiaro, nombre, descripcion)
            DT_gasto.guardarGasto(GastoGuardar)
            mensaje = QMessageBox()
            mensaje.setWindowTitle("SERMICCSA")
            mensaje.setText("Gasto guardado con exito")
            mensaje.setIcon(QMessageBox.Information)
            mensaje.exec_()
            self.show_proyectoX()
        except Exception as e:
            print(f'Excepción: {e}')
            mensaje = QMessageBox()
            mensaje.setWindowTitle("SERMICCSA")
            mensaje.setText("No se logro guardar tu gasto")
            mensaje.setIcon(QMessageBox.Critical)
            mensaje.exec_()
            DT_factura.eliminar_factura(DT_factura, self.G_id_factura)
            self.show_proyectoX()

    def mostrar_error(self):
        mensaje = QMessageBox()
        mensaje.setWindowTitle("SERMICCSA")
        mensaje.setText("Agrega tus etapas antes de salir")
        mensaje.setIcon(QMessageBox.Critical)
        mensaje.exec_()

    def verificar_proyecto(self):
        self.proyecto_actual = self.proyectoGuardado
        self.show_proyectoX()

    def cancelar_creacion(self):
        self.proyecto_actual = self.proyectoGuardado
        DT_proyect().eliminarProyecto(self.proyecto_actual.nombre)
        self.show_proyectos()

    def show_etapas(self):
        if self.verificador == 10:
            self.uiproyectoX.close()
        elif self.verificador == 13:
            self.uiespecificaciones.close()
        elif self.verificador == 6:
            self.uiNuevoproyecto.close()
        elif self.verificador == 16:
            self.uiNuevaEtapa.close()
        elif self.verificador == 9:
            self.uiNuevaEtapa.close()
        else:
            pass

        self.verificador = 9

        self.uietapas = Ui_Etapas()
        self.uietapas.setupUi(self.uietapas)
        self.uietapas.pushButton.clicked.connect(self.show_agregar_etapa)
        self.uietapas.pushButton_3.clicked.connect(self.cancelar_creacion)
        self.uietapas.pushButton_5.clicked.connect(self.mostrar_error)
        self.uietapas.pushButton_4.clicked.connect(self.verificar_proyecto)
        self.uietapas.cargar_etapas(self.proyectoGuardado.id_proyecto)
        self.uietapas.show()

    def show_agregar_etapa(self):

        if self.verificador == 9:
            self.uietapas.close()
        else:
            pass

        self.verificador = 16
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
        etapaGuardar = Etapa(1, self.proyectoGuardado.id_proyecto, nombre, descripcion, presupuesto, numero_etapa)
        DT_etapa.guardarEtapa(etapaGuardar)
        self.limpiar_campos_guardar_nueva_etapa()
        self.show_etapas()

    def eliminar_etapa(self):
        try:
            row = self.uiverEtapas.tableWidget.currentRow()

            self.nombre_etapa = self.uiverEtapas.tableWidget.item(row, 0).text()
            DT_etapa().eliminarEtapa(self.nombre_etapa)
            self.show_ver_etapa()
        except:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("SERMICCSA")
            mensaje.setText("No hay ninguna celda seleccionada")
            mensaje.setIcon(QMessageBox.Critical)
            mensaje.exec_()

    def limpiar_campos_guardar_nueva_etapa(self):
        self.uiNuevaEtapa.lineEdit.setText("")
        self.uiNuevaEtapa.lineEdit_2.setText("")
        self.uiNuevaEtapa.lineEdit_3.setText("")
        self.uiNuevaEtapa.lineEdit_4.setText("")

    def etapa_especifica(self):
        row = self.uiverEtapas.tableWidget.currentRow()
        self.nombre_etapa = self.uiverEtapas.tableWidget.item(row, 2).text()
        descripcion = self.uiverEtapas.tableWidget.item(row, 3).text()
        self.etapa_actual = DT_etapa.buscar_etapa_por_nomdes(DT_etapa, self.nombre_etapa, descripcion)
        self.show_especificaciones_etapas()

    def show_ver_etapa(self):
        if self.verificador == 10:
            self.uiproyectoX.close()
        elif self.verificador == 13:
            self.uiespecificaciones.close()
        else:
            pass

        self.verificador = 12

        self.uiproyectoX.close()
        self.uiverEtapas = Ui_VerEtapas()
        self.uiverEtapas.setupUi(self.uiverEtapas)
        self.uiverEtapas.pushButton.clicked.connect(self.show_proyectoX)
        self.uiverEtapas.pushButton_2.clicked.connect(self.eliminar_etapa)
        self.uiverEtapas.cargar_etapa(self.proyecto_actual.id_proyecto)
        self.uiverEtapas.tableWidget.cellDoubleClicked.connect(self.etapa_especifica)
        self.uiverEtapas.show()

    def show_especificaciones_etapas(self):
        if self.verificador == 12:
            self.uiverEtapas.close()
        else:
            pass

        self.verificador = 13

        self.uiverEtapas.close()
        self.uiespecificaciones = Ui_Especificaciones_Etapas()
        self.uiespecificaciones.setupUi(self.uiespecificaciones)
        self.uiespecificaciones.pushButton.clicked.connect(self.show_ver_etapa)
        self.uiespecificaciones.cargar_gastos(self.etapa_actual)
        self.uiespecificaciones.show()


    def generar_reporte(self):
        try:
            workbook = xlsxwriter.Workbook("Gastos.xlsx")
            worksheet = workbook.add_worksheet("Gastito")

            worksheet.write(0, 0, "Nombre del Gasto")
            worksheet.write(0, 1, "Descripcion del Gasto")
            worksheet.write(0, 2, "Etapa")
            worksheet.write(0, 3, "Subtotal de la Factura")
            worksheet.write(0, 4, "Beneficiario")

            resultados = self.uiproyectoX.gasto_tabla(self.proyecto_actual.id_proyecto)

            for index, resultado in enumerate(resultados):
                worksheet.write(index + 1, 0, str(resultado['Nombre del gasto']))
                worksheet.write(index + 1, 1, str(resultado['Descripción del gasto']))
                worksheet.write(index + 1, 2, str(resultado['Nombre de la etapa']))
                worksheet.write(index + 1, 3, str(resultado['Total de la factura']))
                worksheet.write(index + 1, 4, str(resultado['Nombre del beneficiario']))

            workbook.close()
            mensaje = QMessageBox()
            mensaje.setWindowTitle("SERMICCSA")
            mensaje.setText("El reporte se ha generado de manera exitosa")
            mensaje.setIcon(QMessageBox.Information)
            mensaje.exec_()
        except:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("SERMICCSA")
            mensaje.setText("Fallo al generar el reporte")
            mensaje.setIcon(QMessageBox.Critical)
            mensaje.exec_()







if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
