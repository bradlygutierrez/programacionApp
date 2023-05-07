import copy
class Gasto:
    def __init__(self, idGasto, idRubro, idBeneficiario, idFactura, idEtapa, nombre, descripcion):
        self._idGasto = idGasto
        self._idRubro = idRubro
        self._idBeneficiario = idBeneficiario
        self._idFactura = idFactura
        self._idEtapa = idEtapa
        self._nombre = nombre
        self._descripcion = descripcion

    def __str__(self):
        return f'''
        idGasto: {self._idGasto},
        idRubro: {self._idRubro},
        idBeneficiario: {self._idBeneficiario},
        idFactura: {self._idFactura},
        idEtapa: {self._idEtapa},
        nombre: {self._nombre},
        descripcion: {self._descripcion}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.idGasto = u._idGasto
        u.idRubro = u._idRubro
        u.idBeneficiario = u._idBeneficiario
        u.idFactura = u._idFactura
        u.idEtapa = u._idEtapa
        u.nombre = u._nombre
        u.descripcion = u._descripcion
        return u

    #GET
    @property
    def idGasto(self):
        return self._idGasto

    #SET
    @idGasto.setter
    def idGasto(self, idGasto):
        self._idGasto = idGasto

    @property
    def idRubro(self):
        return self._idRubro

    # SET
    @idRubro.setter
    def idRubro(self, idRubro):
        self._idRubro = idRubro

    @property
    def idBeneficiario(self):
        return self._idBeneficiario

    # SET
    @idBeneficiario.setter
    def idBeneficiario(self, idBeneficiario):
        self._idBeneficiario= idBeneficiario

    @property
    def idFactura(self):
        return self._idFactura

    # SET
    @idFactura.setter
    def idFactura(self, idFactura):
        self._idFactura = idFactura

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
        self._nombre=nombre

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self,descripcion):
        self._descripcion = descripcion


if __name__ == '__main__':
    gasto1 = Gasto(idGasto=1, idRubro=2, idBeneficiario=3, idFactura=4, idEtapa=5, nombre="Gasto1", descripcion="DEscripcion1")
    print(gasto1)