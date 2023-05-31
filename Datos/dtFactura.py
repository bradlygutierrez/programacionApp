from Datos.conexion import Conexion
from entidades.factura import Factura


class DT_factura:
    _INSERT = "INSERT INTO sermiccsa.factura (id_factura, fecha_pago, referencia, subtotal, cantidad_ir, iva ) values (%d, %s, %s, %d, %d, %d)"

    @classmethod
    def listarFactura(cls):
        conexion = Conexion.getConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM sermiccsa.factura;")
        resultado = cursor.fetchall()
        facturas = []
        try:
            for x in resultado:
                factura = Factura(
                    x['id_factura'],
                    x['fecha_pago'],
                    x['referencia'],
                    x['subtotal'],
                    x['cantidad_ir'],
                    x['iva']
                )
                facturas.append(factura)
            return facturas
        except Exception as e:
            print(f'Excepción: {e}')

    @classmethod
    def guardarFactura(cls, factura):
        conexion = Conexion.getConnection()
        cursor = conexion.cursor()
        try:
            print(f'Factura a insertar: {factura}')
            valores = (factura.idFactura, factura.fecha, factura.referencia, factura.subtotal, factura.ir, factura.iva)
            cursor.execute(cls._INSERT, valores)
            print(f'Factura insertada: {factura}')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception {e}')


if __name__ == '__main__':
    facturas = DT_factura.listarFactura()
    for x in facturas:
        print(x)