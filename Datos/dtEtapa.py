from Datos.conexion import Conexion
from entidades.etapas import Etapa


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
                _INSERT = f"INSERT INTO `sermiccsa`.`etapa` (`nombre`, `numero_etapa`, `descripcion`, `presupuesto`) VALUES ('{etapa.nombreEtapa}', '{etapa.NumEtapa}', '{etapa.descripcion}', '{etapa.presupuestoEtapa}');"
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
            return cursor.rowcount
        except Exception as e:
                print(f'''Excepción: {e}''')

    def encontrar_gastos_totales(self, id_proyecto):
        etapitas = self.listarEtapa()
        etapas = []

        for etapa in etapitas:
            if etapa.idProyecto == id_proyecto:
                etapas.append(etapa.idEtapa)

        return etapas


if __name__ == '__main__':
    #LISTAR Etapas
    etapas = DT_etapa.listarEtapa()
    for x in etapas:
        print(x)