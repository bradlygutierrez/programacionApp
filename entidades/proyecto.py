class Proyecto:
    def __init__(self, idproyecto, idUsuario, fechaInicio, presupuestoInicial, beneficiarioProyecto):
        self._idproyecto = idproyecto
        self._idUsuario = idUsuario
        self._fechaInicio = fechaInicio
        self._presupuestoInicial = presupuestoInicial
        self._beneficiarioProyecto = beneficiarioProyecto

    @property
    def idproyecto(self):
        return self._idproyecto

    @idproyecto.setter
    def idproyecto(self, value):
        self._idproyecto = value

    @property
    def idUsuario(self):
        return self.idUsuario

    @idUsuario.setter
    def idUsuario(self, value):
        self._idUsuario = value

    @property
    def fechaInicio(self):
        return self._fechaInicio

    @fechaInicio.setter
    def fechaInicio(self, value):
        self._fechaInicio = value

    @property
    def presupuestoInicial(self):
        return self._presupuestoInicial

    @presupuestoInicial.setter
    def presupuestoInicial(self, value):
        self._presupuestoInicial = value

    @property
    def beneficiarioProyecto(self):
        return self._beneficiarioProyecto

    @beneficiarioProyecto.setter
    def beneficiarioProyecto(self, value):
        self._beneficiarioProyecto = value

    # método to string (str)
    def __str__(self):
        return f"ID del proyecto: {self._idproyecto}\n" \
               f"ID del usuario: {self._idUsuario}\n" \
               f"Fecha de inicio: {self._fechaInicio}\n" \
               f"Presupuesto inicial: {self._presupuestoInicial}\n" \
               f"Beneficiario del proyecto: {self._beneficiarioProyecto}"

    # método __getitem__
    def __getitem__(self, item):
        u = copy.copy(self)
        u.idproyecto = u._idproyecto
        u.idusuario = u._idusuario
        u.fechaInicio = u._fechaInicial
        u.presupuestoInicial = u._presupuestoInicial
        u.beneficiarioProyecto = u._beneficiarioProyecto
        return u

if __name__ == '__main__':
    proyecto = Proyecto(idproyecto='1', idUsuario='2', fechaInicio='hoy', presupuestoInicial=2000, beneficiarioProyecto='Brad')
    print(proyecto)