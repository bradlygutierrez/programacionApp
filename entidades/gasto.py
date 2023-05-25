import copy


class Gasto:
    def __init__(self, idGasto, idEtapa, nombre, descripcion):
        self._idGasto = idGasto
        self._idEtapa = idEtapa
        self._nombre = nombre
        self._descripcion = descripcion

    def __str__(self):
        return f'''
        idGasto: {self._idGasto},
        idEtapa: {self._idEtapa},
        nombre: {self._nombre},
        descripcion: {self._descripcion}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.idGasto = u._idGasto
        u.idEtapa = u._idEtapa
        u.nombre = u._nombre
        u.descripcion = u._descripcion
        return u

    # GET
    @property
    def idGasto(self):
        return self._idGasto

    # SET
    @idGasto.setter
    def idGasto(self, idGasto):
        self._idGasto = idGasto



    @property
    def idEtapa(self):
        return self._idEtapa

    # SET
    @idEtapa.setter
    def idEtapa(self, idEtapa):
        self._idEtapa = idEtapa

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion


