from conexion import Conexion
from entidades.proyecto import Proyecto


class DT_proyect:
    _INSERT = "INSERT INTO sermiccsa.proyecto (beneficiario, fecha_inicio, id_proyecto, id_usuario, presupuesto_inicial) values (%s, now(), %d, %d, %f)"

    @classmethod
    def listarProyectos(cls):
        with Conexion.getConnection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM sermiccsa.proyecto")
                resultado = cursor.fetchall()
                proyecto = []
                try:
                    for x in resultado:
                        u = Proyecto(x['id_proyecto'], x['id_usuario'],x['fecha_inicio'],x['presupuesto_inicial'],x['beneficiario']
                                    )
                        proyecto.append(u)
                    print('proyectos', proyecto)
                    return proyecto
                except Exception as e:
                    print(f'Excepción {e}')

    @classmethod
    def guardarProyectos(cls, proyecto):
        with Conexion.getConnection() as conexion:
            with conexion.cursor() as cursor:
                try:
                    print(f'Proyecto a insertar: {proyecto}')
                    valores = (proyecto.idBeneficiario, proyecto.fechaInicio, proyecto.idproyecto, proyecto.idUsuario, proyecto.presupuestoInicial)
                    cursor.execute(cls._INSERT, valores)
                    print(f'Proyecto insertado: {proyecto}')
                    conexion.commit()
                    return cursor.rowcount
                except Exception as e:
                    print(f'Exception {e}')


if __name__ == '__main__':
    #INSERTAR REGISTRO
    # usuario1 = Usuario(nombre='miguel', apellido='cervantes', nombreusuario='elQuijote', clave='123', fecha_creacion='2023-03-10')
    # insertar = DT_Usuario.guardarUsuario(usuario1)
    # print(f'Usuario insertado : {insertar}')

    #LISTAR USUARIOS
    proyectos = DT_proyect.listarProyectos()
    for x in proyectos:
        print(x)