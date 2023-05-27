from Datos.conexion import Conexion
from entidades.proyecto import Proyecto



class DT_proyect:
    _INSERT = "INSERT INTO sermiccsa.proyecto (id_usuario, nombre, descripcion,fecha_inicio, beneficiario, presupuesto_inicial ) VALUES (%s, %s, %s, NOW(), %s, %f)"

    @classmethod
    def listarProyectos(cls):
        conexion = Conexion.getConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM sermiccsa.proyecto;")
        resultado = cursor.fetchall()
        proyectos = []
        try:
            for x in resultado:
                proyecto = Proyecto(
                x['id_proyecto'],
                x['id_usuario'],
                x['nombre'],
                x['descripcion'],
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
                        proyecto.id_usuario,
                        proyecto.nombre,
                        proyecto.descripcion,
                        proyecto.fecha_inicio,
                        proyecto.presupuesto_inicial,
                        proyecto.beneficiario_proyecto

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
