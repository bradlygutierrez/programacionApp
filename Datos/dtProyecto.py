from Datos.conexion import Conexion
from entidades.proyecto import Proyecto



class DT_proyect:

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
                x['fecha_inicio'],
                x['nombre'],
                x['descripcion'],
                x['presupuesto_inicial'],
                x['beneficiario']
                )
                proyectos.append(proyecto)
            return proyectos
        except Exception as e:
            print(f'Excepción: {e}')
        conexion.close()
    @classmethod
    def guardarProyecto(cls, proyecto):
        conexion = Conexion.getConnection()
        cursor = conexion.cursor()

        try:
            presupuesto_convertido = float(proyecto.presupuesto_inicial)

            _INSERT = f"""INSERT INTO sermiccsa.proyecto (`id_usuario`, `nombre`, `descripcion`, `fecha_inicio`, `beneficiario`, `presupuesto_inicial`) VALUES ('{proyecto.id_usuario}', '{proyecto.nombre}','{proyecto.descripcion}','{proyecto.fecha_inicio}', '{proyecto.beneficiario_proyecto}', '{presupuesto_convertido}');"""
            cursor.execute(_INSERT)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
                print(f'''Excepción: {e}''')


if __name__ == '__main__':
    proyectos = DT_proyect.listarProyectos()
    for proyecto in proyectos:
        print(proyecto)
