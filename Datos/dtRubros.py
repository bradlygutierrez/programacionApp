from Datos.conexion import Conexion
from entidades.rubro import Rubro


class DT_rubro:
    _INSERT = "INSERT INTO sermiccsa.rubro (id_rubro, nombre) values (%d, %s)"

    @classmethod
    def listarrubros(cls):
        conexion = Conexion.getConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM sermiccsa.rubro")
        resultado = cursor.fetchall()
        rubros = []
        try:
            for x in resultado:
                rubro = Rubro(
                    x['id_rubro'],
                    x['nombre'])
                rubros.append(rubro)
            return rubros
        except Exception as e:
            print(f'Excepción: {e}')


if __name__ == '__main__':
    # LISTAR Etapas
    etapas = DT_rubro.listarrubros()
    for x in etapas:
        print(x)
