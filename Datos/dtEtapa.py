from conexion import Conexion
from entidades.etapas import Etapa


class DT_etapa:
    _INSERT = "INSERT INTO sermiccsa.etapa (descripcion, id_etapa, id_proyecto, nombre, numero_etapa, presupuesto) values (%s, %d, %d, %s, %d, %f)"

    @classmethod
    def listarProyectos(cls):
        with Conexion.getConnection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM sermiccsa.etapa")
                resultado = cursor.fetchall()
                etapas = []
                try:
                    for x in resultado:
                        u = Etapa(x['descripcion'], x['id_etapa'], x['id_proyecto'], x['nombre'],
                                    x['numero_etapa'],x['presupuesto'])
                        etapas.append(u)
                    print('Etapas', etapas)
                    return etapas
                except Exception as e:
                    print(f'Excepción {e}')

    @classmethod
    def guardarProyectos(cls, etapa):
        with Conexion.getConnection() as conexion:
            with conexion.cursor() as cursor:
                try:
                    print(f'Etapa a insertar: {etapa}')
                    valores = (etapa.descripcion, etapa.idEtapa, etapa.idProyecto ,etapa.nombreEtapa, etapa.NumEtapa, etapa.presupuestoEtapa)
                    cursor.execute(cls._INSERT, valores)
                    print(f'Etapa insertado: {etapa}')
                    conexion.commit()
                    return cursor.rowcount
                except Exception as e:
                    print(f'Exception {e}')


if __name__ == '__main__':
    #INSERTAR REGISTRO
    # usuario1 = Usuario(nombre='miguel', apellido='cervantes', nombreusuario='elQuijote', clave='123', fecha_creacion='2023-03-10')
    # insertar = DT_Usuario.guardarUsuario(usuario1)
    # print(f'Usuario insertado : {insertar}')

    #LISTAR Etapas
    etapas = DT_etapa.listarProyectos()
    for x in etapas:
        print(x)