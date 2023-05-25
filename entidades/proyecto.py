class Proyecto:
    def __init__(self, id_proyecto, id_usuario, fecha_inicio, presupuesto_inicial, beneficiario_proyecto):
        self._id_proyecto = id_proyecto
        self._id_usuario = id_usuario
        self._fecha_inicio = fecha_inicio
        self._presupuesto_inicial = presupuesto_inicial
        self._beneficiario_proyecto = beneficiario_proyecto

    @property
    def id_proyecto(self):
        return self._id_proyecto

    @id_proyecto.setter
    def id_proyecto(self, value):
        self._id_proyecto = value

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, value):
        self._id_usuario = value

    @property
    def fecha_inicio(self):
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value):
        self._fecha_inicio = value

    @property
    def presupuesto_inicial(self):
        return self._presupuesto_inicial

    @presupuesto_inicial.setter
    def presupuesto_inicial(self, value):
        self._presupuesto_inicial = value

    @property
    def beneficiario_proyecto(self):
        return self._beneficiario_proyecto

    @beneficiario_proyecto.setter
    def beneficiario_proyecto(self, value):
        self._beneficiario_proyecto = value

    # método to string (str)
    def __str__(self):
        return f"ID del proyecto: {self._id_proyecto}\n" \
               f"ID del usuario: {self._id_usuario}\n" \
               f"Fecha de inicio: {self._fecha_inicio}\n" \
               f"Presupuesto inicial: {self._presupuesto_inicial}\n" \
               f"Beneficiario del proyecto: {self._beneficiario_proyecto}"

    # método __getitem__
    def __getitem__(self, item):
        u = copy.copy(self)
        u.id_proyecto = u._id_proyecto
        u.id_usuario = u._id_usuario
        u.fecha_inicio = u._fecha_inicial
        u.presupuesto_inicial = u._presupuesto_inicial
        u.beneficiario_proyecto = u._beneficiario_proyecto
        return u

if __name__ == '__main__':
    proyecto = Proyecto(id_proyecto='1', id_usuario='2', fecha_inicio='hoy', presupuesto_inicial=2000, beneficiario_proyecto='Brad')
    print(proyecto)
