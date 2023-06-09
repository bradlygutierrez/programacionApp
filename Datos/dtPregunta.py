from Datos.conexion import Conexion
from entidades.pregunta import Pregunta


class DT_pregunta:
    _INSERT = "INSERT INTO sermiccsa.pregunta (pregunta) values (%d, %s)"

    @classmethod
    def listarPreguntas(cls):
        conexion = Conexion.getConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM sermiccsa.pregunta;")
        resultado = cursor.fetchall()
        preguntas = []
        try:
            for x in resultado:
                u = Pregunta(x['id_pregunta'], x['pregunta'])
                preguntas.append(u)
            print('preguntas', preguntas)
            return preguntas
        except Exception as e:
            print(f'Excepción {e}')

    @classmethod
    def guardarPregunta(cls, pregunta):
        with Conexion.getConnection() as conexion:
            with conexion.cursor() as cursor:
                try:
                    print(f'Pregunta a insertar: {pregunta}')
                    valores = (pregunta.idPregunta, pregunta.contenidoPregunta)
                    cursor.execute(cls._INSERT, valores)
                    print(f'Pregunta insertado: {pregunta}')
                    conexion.commit()
                    return cursor.rowcount
                except Exception as e:
                    print(f'Exception {e}')

    def buscar_pregunta(self, id_pregunta):
        preguntas = self.listarPreguntas()

        for pregunta in preguntas:
            if pregunta.idPregunta == id_pregunta:
                return pregunta.contenidoPregunta


if __name__ == '__main__':
    #INSERTAR REGISTRO
    # usuario1 = Usuario(nombre='miguel', apellido='cervantes', nombreusuario='elQuijote', clave='123', fecha_creacion='2023-03-10')
    # insertar = DT_Usuario.guardarUsuario(usuario1)
    # print(f'Usuario insertado : {insertar}')

    #LISTAR USUARIOS
    pregunta = DT_pregunta.listarPreguntas()
    for x in pregunta:
        print(x)