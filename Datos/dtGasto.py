from Datos.conexion import Conexion
from entidades.gasto import Gasto


class DT_gasto:
    _INSERT = "INSERT INTO sermiccsa.gasto (id_etapa, nombre, descripcion, id_rubro, id_beneficiario, id_factura ) values (%d, %s, %s, %d, %d, %d)"

    @classmethod
    def listarGastos(cls):
        conexion = Conexion.getConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM sermiccsa.gasto;")
        resultado = cursor.fetchall()
        gastos = []
        try:
            for x in resultado:
                gasto = Gasto(
                    x['id_gasto'],
                    x['id_etapa'],
                    x['id_rubro'],
                    x['id_factura'],
                    x['id_beneficiario'],
                    x['nombre'],
                    x['descripcion']
                )
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
            valores = ( gasto.idEtapa, gasto.nombre, gasto.descripcion, gasto.idRubro, gasto.idBeneficiario, gasto.idFactura)
            cursor.execute(cls._INSERT, valores)
            print(f'Gasto insertado: {gasto}')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception {e}')


if __name__ == '__main__':
    gastos = DT_gasto.listarGastos()
    for x in gastos:
        print(x)
