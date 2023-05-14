from Datos.conexion import Conexion
from entidades.proyecto import Proyecto


class DT_proyect:
    _INSERT = "INSERT INTO sermiccsa.proyecto (beneficiario, fecha_inicio, id_proyecto, id_usuario, presupuesto_inicial) VALUES (%s, NOW(), %s, %s, %s)"

    @classmethod
    def listarProyectos2(cls):
        with Conexion.getConnection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM sermiccsa.proyecto")
                resultado = cursor.fetchall()
                proyectos = []
                try:
                    for x in resultado:
                        proyecto = Proyecto(
                            x['id_proyecto'],
                            x['id_usuario'],
                            x['fecha_inicio'],
                            x['presupuesto_inicial'],
                            x['beneficiario']
                        )
                        proyectos.append(proyecto)
                    return proyectos
                except Exception as e:
                    print(f'Excepción: {e}')
    @classmethod
    def listarProyectos(cls):
        conexion = Conexion.getConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM sermiccsa.proyecto")
        resultado = cursor.fetchall()
        proyectos = []
        try:
            for x in resultado:
                proyecto = Proyecto(
                x['id_proyecto'],
                x['id_usuario'],
                x['fecha_inicio'],
                x['presupuesto_inicial'],
                x['beneficiario']
                )
                proyectos.append(proyecto)
            return proyectos
        except Exception as e:
            print(f'Excepción: {e}')
    @classmethod
    def guardarProyecto(cls, proyecto):
        with Conexion.getConnection() as conexion:
            with conexion.cursor() as cursor:
                try:
                    valores = (
                        proyecto.beneficiario,
                        proyecto.fecha_inicio,
                        proyecto.id_proyecto,
                        proyecto.id_usuario,
                        proyecto.presupuesto_inicial
                    )
                    cursor.execute(cls._INSERT, valores)
                    conexion.commit()
                    return cursor.rowcount
                except Exception as e:
                    print(f'''Excepción: {e}''')


if __name__ == '__main__':
    proyectos = DT_proyect.listarProyectos()
    for proyecto in proyectos:
        print(proyecto)
