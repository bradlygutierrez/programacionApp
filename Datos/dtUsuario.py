from Datos.conexion import Conexion
from entidades.usuario import Usuario
from PyQt5.QtWidgets import QApplication, QMessageBox


class DT_Usuario:

    @classmethod
    def listarUsuario(cls):
        conexion = Conexion.getConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM sermiccsa.usuario;")
        resultado = cursor.fetchall()
        usuarios = []
        try:
            for x in resultado:
                u = Usuario(x['id_usuario'], x['nombre'], x['correo'], x['id_pregunta'],
                            x['clave'],x['respuesta'])
                usuarios.append(u)
            print('usuarios', usuarios)
            return usuarios
        except Exception as e:
            print(f'Excepción {e}')

    @classmethod
    def guardarUsuario(cls, usuario):
        conexion = Conexion.getConnection()
        cursor = conexion.cursor()
        try:
            print(f'Usuario a insertar: {usuario}')
            id_pregunta = int(usuario.pregunta)
            _INSERT = f"""INSERT INTO sermiccsa.usuario (`clave`, `correo`, `id_pregunta`, `nombre`, `respuesta`) values ('{usuario.contrasenia}', '{usuario.correo}','{id_pregunta}','{usuario.nombre}', '{usuario.respuesta}');"""
            cursor.execute(_INSERT)
            print(f'Usuario insertado: {usuario}')
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Sermiccsa")
            mensaje.setText("EL usuario se ha guardado con exito")
            mensaje.setIcon(QMessageBox.Information)
            mensaje.exec_()
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Sermiccsa")
            mensaje.setText("Error al intentar guardar usuario, intenta de nuevo")
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.exec_()
            print(f'Exception {e}')

    def existe_usuario(self, user, clave):
        usuarios = self.listarUsuario()

        for usuario in usuarios:
            if usuario.nombre == user:
                if usuario.contrasenia == clave:
                    return True
        return False

    def existe_solo_usuario(self, user):
        usuarios = self.listarUsuario()

        for usuario in usuarios:
            if usuario.nombre == user:
                    return True
        return False

    def conseguir_id_usuario(self, user, clave):
        usuarios = self.listarUsuario()

        for usuario in usuarios:
            if usuario.nombre == user:
                if usuario.contrasenia == clave:
                    return usuario.idUsuario

    def buscar_pregunta(self, name):
        usuarios = self.listarUsuario()

        for usuario in usuarios:
            if usuario.nombre == name:
                print(usuario.pregunta)
                return usuario.pregunta

    def verificar_respuesta(self, user, respuesta):
        usuarios = self.listarUsuario()

        for usuario in usuarios:
            if usuario.nombre == user:
                if usuario.respuesta == respuesta:
                    return True

        return False

    def actualizar_clave(self, nombrecito, clavecita):
        conexion = Conexion.getConnection()
        cursor = conexion.cursor()
        try:
            _UPDATE = f"""UPDATE `sermiccsa`.`usuario` SET `clave` = {clavecita} WHERE(`nombre` = '{nombrecito}');"""
            cursor.execute(_UPDATE)
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Sermiccsa")
            mensaje.setText("Su clave se ha reiniciado de manera correcta. Inicise sesion y siga disfrutando de la aplicacion")
            mensaje.setIcon(QMessageBox.Information)
            mensaje.exec_()
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Sermiccsa")
            mensaje.setText("Erro al editar su clave. Le pedimos que intente de nuevo. Si el problema persiste, contacte a un administrador")
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.exec_()
            print(f'Exception {e}')




if __name__ == '__main__':
    #LISTAR USUARIOS
    users = DT_Usuario.listarUsuario()
    for x in users:
        print(x)