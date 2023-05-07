import copy
class Pregunta:
    def __init__(self, idpregunta, contenidoPregunta):
        self._idpregunta = idpregunta
        self._contenidoPregunta = contenidoPregunta

    def __str__(self):
        return f'''
        idPregunta: {self._idpregunta},
        contenidoPregunta: {self._contenidoPregunta}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u._idpregunta = u._idpregunta
        u._contenidoPregunta = u._contenidoPregunta
        return u

    @property
    def idPregunta(self):
        return self._idpregunta

    # SET
    @idPregunta.setter
    def idPregunta(self, idPregunta):
        self._idpregunta = idPregunta

    @property
    def contenidoPregunta(self):
        return self._contenidoPregunta

    # SET
    @contenidoPregunta.setter
    def contenido(self, contenido):
        self._contenidoPregunta = contenido

if __name__ == '__main__':
    pregunta = Pregunta(idpregunta=1, contenidoPregunta='hola')
    print(pregunta)