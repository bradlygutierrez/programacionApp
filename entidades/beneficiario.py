import copy


class Beneficiario:
    def __init__(self, idBeneficiario, nombre, identificacion):
        self._idBeneficiario = idBeneficiario
        self._nombre = nombre
        self._identificacion = identificacion

    def __str__(self):
        return f'''
        id: {self._idBeneficiario},
        nombre: {self._nombre},
        identificacion: {self._identificacion}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.nombre = u._nombre
        u.identificacion = u._identificacion
        u.idBeneficiario = u._idBeneficiario
        return u

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def identificacion(self):
        return self._identificacion

    @identificacion.setter
    def correo(self, identificacion):
        self._identificacion = identificacion

    @property
    def id_Beneficiario(self):
        return self._idBeneficiario

    @id_Beneficiario.setter
    def id_Beneficiario(self, idBeneficiario):
        self._idBeneficiario = idBeneficiario
