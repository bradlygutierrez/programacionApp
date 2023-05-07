import copy
class Rubro:
    def __init__(self, idRubro, nombre):
        self._idRubro = idRubro
        self._nombre = nombre

    def __str__(self):
        return f'''
        idRubro: {self._idRubro},
        nombre: {self._nombre}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.idRubro = u._idRubro
        u.nombre = u._nombre
        return u

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre=nombre

    @property
    def idRubro(self):
        return self._idRubro

    @idRubro.setter
    def idRubro(self, idRubro):
        self._idRubro=idRubro

if __name__ == '__main__':
    rubro1 = Rubro(idRubro=1, nombre='Hierro')
    print(rubro1)