from Datos.conexion import Conexion
from entidades.etapas import Etapa


class DT_etapa:
    _INSERT = "INSERT INTO sermiccsa.etapa (descripcion, id_etapa, id_proyecto, nombre, numero_etapa, presupuesto) values (%s, %d, %d, %s, %d, %f)"

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
                    x['presupuesto'],x['numero_etapa'])
                etapas.append(etapa)
            return etapas
        except Exception as e:
            print(f'Excepción: {e}')

    @classmethod
    def guardarEtapa(cls, etapa):
        with Conexion.getConnection() as conexion:
            with conexion.cursor() as cursor:
                try:
                    print(f'Etapa a insertar: {etapa}')
                    valores = (etapa.idEtapa, etapa.idProyecto, etapa.nombreEtapa,etapa.descripcion, etapa.presupuestoEtapa, etapa.NumEtapa)
                    cursor.execute(cls._INSERT, valores)
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

    def Eliminar_Etapa(self):
        if Conexion.getConnection():
            print("Conexión exitosa")
        with Conexion.getConnection() as conexion:
            with conexion.cursor() as cursor:
                try:
                    cursor.execute("DELETE FROM sermiccsa.etapa WHERE id_etapa = 1")
                    cursor.commit()
                    print("Registro eliminado con éxito")
                except Exception as e:
                    print("Error durante la conexión", e)


if __name__ == '__main__':
    #LISTAR Etapas
    etapas = DT_etapa.listarEtapa()
    for x in etapas:
        print(x)