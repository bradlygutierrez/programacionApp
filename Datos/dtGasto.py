from Datos.conexion import Conexion
from entidades.gasto import Gasto
from Datos.dtFactura import DT_factura

class DT_gasto:

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
            _INSERT = f"""INSERT INTO sermiccsa.gasto (`nombre`, `descripcion`, `id_etapa`, `id_rubro`, `id_beneficiario`, `id_factura`) values ('{gasto.nombre}', '{gasto.descripcion}',{gasto.idEtapa},{gasto.idRubro}, {gasto.idBeneficiario},{gasto.idFactura});"""
            cursor.execute(_INSERT)
            print(f'Gasto insertado: {gasto}')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception {e}')

    def calcular_total_gastos(self, lista_id_etapas):
        gastitos = self.listarGastos()
        total_gastos = 0

        for id_etapa in lista_id_etapas:
            for gasto in gastitos:
                if gasto.idEtapa == id_etapa:
                    total = DT_factura.obtener_factura(DT_factura, gasto.idFactura)
                    total_gastos = total_gastos + total

        return total_gastos





if __name__ == '__main__':
    gastos = DT_gasto.listarGastos()
    for x in gastos:
        print(x)
