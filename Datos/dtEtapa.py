from Datos.conexion import Conexion
from entidades.etapas import Etapa
from PyQt5.QtWidgets import QApplication, QMessageBox

class DT_etapa:

    @classmethod
    def listarEtapa(cls):
        conexion = Conexion.getConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM sermiccsa.etapa")
        resultado = cursor.fetchall()
        etapas = []
        try:
            for x in resultado:
                etapa = Etapa(
                    x['id_etapa'],
                    x['id_proyecto'],
                    x['nombre'],
                    x['descripcion'],
                    x['presupuesto'],
                    x['numero_etapa'])
                etapas.append(etapa)
            return etapas
        except Exception as e:
            print(f'Excepción: {e}')

    @classmethod
    def guardarEtapa(cls, etapa):
            conexion = Conexion.getConnection()
            cursor = conexion.cursor()
            try:
                _INSERT = f"INSERT INTO `sermiccsa`.`etapa` (`nombre`, `id_proyecto`, `numero_etapa`, `descripcion`, `presupuesto`) VALUES ('{etapa.nombreEtapa}', '{etapa.idProyecto}' , '{etapa.NumEtapa}', '{etapa.descripcion}', '{etapa.presupuestoEtapa}');"
                print(f'Etapa a insertar: {etapa}')
                cursor.execute(_INSERT)
                print(f'Etapa insertado: {etapa}')
                conexion.commit()
                return cursor.rowcount
            except Exception as e:
                print(f'Exception {e}')


    def Editar_Etapa(self):
        if Conexion.getConnection():
            print("Conexión exitosa editar")
        with Conexion.getConnection() as conexion:
            with conexion.cursor() as cursor:
                try:
                    cursor.execute("UPDATE FROM sermiccsa.etapa SET nombre = 'PRUEBA 1'")
                    cursor.commit()
                    print("Registro editado con éxito")
                except Exception as e:
                    print("Error durante la conexión", e)

    @classmethod
    def eliminarEtapa(cls, etapa):
        conexion = Conexion.getConnection()
        cursor = conexion.cursor()
        try:
            print(etapa)
            _DELETE = f"DELETE FROM `sermiccsa`.`etapa` WHERE (`id_etapa` = '{etapa}');"
            print("Eliminando etapa")
            cursor.execute(_DELETE)
            print("Etapa eliminada")
            conexion.commit()
            mensaje = QMessageBox()
            mensaje.setWindowTitle("SERMICCSA")
            mensaje.setText("Etapa eliminada con ecito")
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.exec_()
            return cursor.rowcount
        except Exception as e:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("SERMICCSA")
            mensaje.setText("No hay ninguna celda seleccionada")
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.exec_()
            print(f'''Excepción: {e}''')

    def encontrar_gastos_totales(self, id_proyecto):
        etapitas = self.listarEtapa()
        etapas = []

        for etapa in etapitas:
            print(etapa.idEtapa)
            if etapa.idProyecto == id_proyecto:
                etapas.append(etapa.idEtapa)

        for xd in etapas:
            print(xd)

        return etapas

    def buscar_etapa_por_nombre(self, nombre):
        etapas = self.listarEtapa()

        for etapa in etapas:
            if etapa.nombreEtapa == nombre:
                return etapa

    def encontrar_etapas_de_proyecto(self, id_proyecto):
        etapitas = self.listarEtapa()
        etapas = []

        for etapa in etapitas:
            if etapa.idProyecto == id_proyecto:
                etapas.append(etapa)

        return etapas

    def buscar_etapa_por_nomdes(self, nombre, descripcion):
        etapas = self.listarEtapa()

        for etapa in etapas:
            if etapa.nombreEtapa == nombre:
                if etapa.descripcion == descripcion:
                    return etapa


if __name__ == '__main__':
    #LISTAR Etapas
    etapas = DT_etapa.listarEtapa()
    for x in etapas:
        print(x)