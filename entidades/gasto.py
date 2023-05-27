import copy


class Gasto:
    def __init__(self, idGasto, idEtapa, idRubro, idFactura, idBeneficiario, nombre, descripcion):
        self._idGasto = idGasto
        self._idEtapa = idEtapa
        self._idRUbro = idRubro
        self._idFactura = idFactura
        self._idBeneficiario = idBeneficiario
        self._nombre = nombre
        self._descripcion = descripcion

    def __str__(self):
        return f'''
        idGasto: {self._idGasto},
        idEtapa: {self._idEtapa},
        idRubro: {self._idRUbro},
        idFactura: {self._idFactura},
        idBeneficiario: {self._idBeneficiario}
        nombre: {self._nombre},
        descripcion: {self._descripcion}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.idGasto = u._idGasto
        u.idEtapa = u._idEtapa
        u.idRUbro = u._idRUbro
        u.idFactura = u._idFactura
        u.idBeneficiario = u._idBeneficiario
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
    def idRubro(self):
        return self._idRUbro

    # SET
    @idRubro.setter
    def idRubro(self, idRubro):
        self._idRUbro = idRubro

    @property
    def idFactura(self):
        return self._idFactura

    # SET
    @idFactura.setter
    def idFactura(self, valor):
        self._idFactura = valor

    @property
    def idBeneficiario(self):
        return self._idBeneficiario

    # SET
    @idBeneficiario.setter
    def idBeneficiario(self, valor):
        self._idBeneficiario = valor



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


