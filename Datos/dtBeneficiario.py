from Datos.conexion import Conexion
from entidades.beneficiario import Beneficiario


class DT_beneficiario:

    @classmethod
    def listarBeneficiario(cls):
        conexion = Conexion.getConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM sermiccsa.beneficiario")
        resultado = cursor.fetchall()
        beneficiarios = []
        try:
            for x in resultado:
                beneficiario = Beneficiario(
                    x['id_beneficiario'],
                    x['nombre'],
                    x['identificacion'],
                )
                beneficiarios.append(beneficiario)
            return beneficiarios
        except Exception as e:
            print(f'Excepción: {e}')

    @classmethod
    def guardarBeneficiario(cls, beneficiario):
            conexion = Conexion.getConnection()
            cursor = conexion.cursor()
            try:
                _INSERT = f"INSERT INTO `sermiccsa`.`beneficiario`(`nombre`, `identificacion`)VALUES ('{beneficiario.nombre}', '{beneficiario.identificacion}');"
                print(f'Beneficiario a insertar: {beneficiario}')
                cursor.execute(_INSERT)
                print(f'beneficiario insertado: {beneficiario}')
                conexion.commit()
                return cursor.rowcount
            except Exception as e:
                print(f'Exception {e}')

    def editar_beneficiario(self, id, nombre):
        conexion = Conexion.getConnection()
        cursor = conexion.cursor()
        try:
            cursor.execute(f"""UPDATE sermiccsa.beneficiario SET nombre = '{nombre}' WHERE id_beneficiario = '{id}'""")
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
                print("Error durante la conexión en editar", e)

    def buscar_referencia(self, referencia):
        beneficiarios= self.listarBeneficiario()

        for beneficiario in beneficiarios:
            if beneficiario.identificacion == referencia:
                return True

    def buscar_usuario_por_referencia(self, referencia):
        beneficiarios = self.listarBeneficiario()

        for beneficiario in beneficiarios:
            if beneficiario.identificacion == referencia:
                return beneficiario

    def eliminar_beneficiario(cls, id):
        conexion = Conexion.getConnection()
        cursor = conexion.cursor()
        try:
            _DELETE = f"DELETE FROM `sermiccsa`.`beneficiario` WHERE (`id_beneficiario` = '{id}');"
            print("Eliminando beneficiario")
            cursor.execute(_DELETE)
            print("Beneficiario eliminado")
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'''Excepción: {e}''')


if __name__ == '__main__':
    #LISTAR Etapas
    Beneficiario = DT_beneficiario.listarBeneficiario()
    for x in Beneficiario:
        print(x)