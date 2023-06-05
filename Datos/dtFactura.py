from Datos.conexion import Conexion
from entidades.factura import Factura
from decimal import Decimal

class DT_factura:


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
            _INSERT = f"""INSERT INTO sermiccsa.factura (`fecha_pago`, `referencia`, `subtotal`, `cantidad_ir`, `iva`) values ('{factura.fecha}', '{factura.referencia}',{factura.subtotal},{factura.ir}, {factura.iva});"""
            cursor.execute(_INSERT)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception {e}')

    def obtener_factura(self, id_factura):
        facturas = self.listarFactura()

        for factura in facturas:
            if factura.idFactura == id_factura:
                if (factura.iva):
                    gasto = Decimal(factura.subtotal) + Decimal(factura.ir) + (Decimal(factura.subtotal) * Decimal('0.15'))
                else:
                    gasto = factura.subtotal + factura.ir

        return gasto

if __name__ == '__main__':
    facturas = DT_factura.listarFactura()
    for x in facturas:
        print(x)