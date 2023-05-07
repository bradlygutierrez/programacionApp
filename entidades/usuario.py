import copy
class Usuario:
    def __init__(self, nombre, correo, idUsuario, pregunta, contrasenia, respuesta):
        self._nombre = nombre
        self._correo = correo
        self._idUsuario = idUsuario
        self._pregunta = pregunta
        self._contrasenia = contrasenia
        self._respuesta = respuesta

    def __str__(self):
        return f'''
        nombre: {self._nombre},
        correo: {self._correo},
        idUsuario: {self._idUsuario},
        idPregunta: {self._pregunta},
        password: {self._contrasenia},
        respuesta: {self._respuesta},
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.nombre = u._nombre
        u.correo = u._correo
        u.pregunta = u._pregunta
        u.contrasenia = u._contrasenia
        u.respuesta = u._respuesta
        return u

    #GET
    @property
    def idUsuario(self):
        return self._idUsuario

    #SET
    @idUsuario.setter
    def idusuario(self, idUsuario):
        self._idUsuario=idUsuario

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre=nombre

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self,correo):
        self._correo = correo

    @property
    def pregunta(self):
        return self._pregunta

    @pregunta.setter
    def pregunta(self, pregunta):
        self._pregunta = pregunta

    @property
    def contrasenia(self):
        return self._contrasenia

    @contrasenia.setter
    def contrasenia(self,contrasenia):
        self._contrasenia = contrasenia

    @property
    def respuesta(self):
        return self._respuesta

    @respuesta.setter
    def fecha_creacion(self,respuesta):
        self._respuesta = respuesta

if __name__ == '__main__':
    usuario1 = Usuario(nombre='Jorge', correo='moreales@gmail.com', idUsuario=2, pregunta='2', contrasenia='123', respuesta='resp')
    print(usuario1)