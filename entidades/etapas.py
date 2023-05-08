import  copy
class Etapa:
    def __init__(self, idEtapa, idProyecto, nombreEtapa, descripcion, presupuestoEtapa, NumEtapa):
        self._idEtapa = idEtapa
        self._idProyecto = idProyecto
        self._nombreEtapa = nombreEtapa
        self._descripcion = descripcion
        self._presupuestoEtapa = presupuestoEtapa
        self._NumEtapa = NumEtapa

    # getters y setters usando @property
    @property
    def idEtapa(self):
        return self._idEtapa

    @idEtapa.setter
    def idEtapa(self, value):
        self._idEtapa = value

    @property
    def idProyecto(self):
        return self._idProyecto

    @idProyecto.setter
    def idProyecto(self, value):
        self._idProyecto = value

    @property
    def nombreEtapa(self):
        return self._nombreEtapa

    @nombreEtapa.setter
    def nombreEtapa(self, value):
        self._nombreEtapa = value

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value

    @property
    def presupuestoEtapa(self):
        return self._presupuestoEtapa

    @presupuestoEtapa.setter
    def presupuestoEtapa(self, value):
        self._presupuestoEtapa = value

    @property
    def NumEtapa(self):
        return self._NumEtapa
    @NumEtapa.setter
    def  NumEtapa(self,value):
        self._NumEtapa = value

    # método to string (str)
    def __str__(self):
        return f"ID de etapa: {self._idEtapa}\n" \
               f"ID de proyecto: {self._idProyecto}\n" \
               f"Nombre de etapa: {self._nombreEtapa}\n" \
               f"Descripción: {self._descripcion}\n" \
               f"Presupuesto de etapa: {self._presupuestoEtapa}"

    # método __getitem__
    def __getitem__(self, item):
        u = copy.copy(self)
        u._idEtapa = u._idEtapa
        u.idProyecto = u._idProyecto
        u.nombreEtapa = u._nombreEtapa
        u.descripcion = u._descripcion
        u.presupuestoEtapa = u._presupuestoEtapa

if __name__ == '__main__':
    etapa = Etapa(idEtapa='1',idProyecto='2',nombreEtapa='fase1',descripcion='asd',presupuestoEtapa=200)
    print(etapa)