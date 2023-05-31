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

    def Editar_beneficiario(self):
        if Conexion.getConnection():
            print("Conexión exitosa editar")
        with Conexion.getConnection() as conexion:
            with conexion.cursor() as cursor:
                try:
                    cursor.execute("UPDATE FROM sermiccsa.beneficiario SET nombre = 'PRUEBA 1'")
                    cursor.commit()
                    print("Registro editado con éxito")
                except Exception as e:
                    print("Error durante la conexión", e)

    def Eliminar_beneficiario(self):
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
    Beneficiario = DT_beneficiario.listarBeneficiario()
    for x in Beneficiario:
        print(x)