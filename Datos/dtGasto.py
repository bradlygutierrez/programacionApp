from conexion import Conexion
from entidades.gasto import Gasto

class DT_gasto:
    _INSERT = "INSERT INTO sermiccsa.gasto (id_gasto, nombre, descripcion, id_etapa) values (%d, %s, %s, %d)"
    @classmethod
    def listarGastos(cls):
        conexion = Conexion.getConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM sermiccsa.gasto;")
        resultado = cursor.fetchall()
        gastos = []
        try:
            for x in resultado:
                gasto = Gasto(x['id_gasto'], x['nombre'], x['descripcion'], x['id_etapa'])
                gastos.append(gasto)
            return gastos
        except Exception as e:
            print(f'Excepción: {e}')

    @classmethod
    def guardarGasto(cls, gasto):
        conexion = Conexion.getConnection()
        cursor = conexion.cursor()
        try:
            print(f'Gasto a insertar: {gasto}')
            valores = (gasto.idGasto, gasto.nombre, gasto.descripcion, gasto.idEtapa)
            cursor.execute(cls._INSERT, valores)
            print(f'Gasto insertado: {gasto}')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception {e}')

if __name__ == '__main__':
    gasto = DT_gasto.listarGastos()
    for x in gasto:
        print(x)