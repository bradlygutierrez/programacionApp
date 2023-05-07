import copy
class Factura:
    def __init__(self, idFactura, fecha, referencia, subtotal, ir, iva):
        self._idFactura = idFactura
        self._fecha = fecha
        self._referencia = referencia
        self._subtotal = subtotal
        self._ir = ir
        self._iva = iva

    def __str__(self):
        return f'''
        idFactura: {self._idFactura},
        fecha: {self._fecha},
        referencia {self._referencia},
        subtotal: {self._subtotal},
        ir: {self._ir},
        iva: {self._iva},
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.idFactura = u._idFactura
        u.fecha = u._fecha
        u.referencia = u._referencia
        u.subtotal = u._subtotal
        u.ir = u._ir
        u.iva = u._iva
        return u

    #GET
    @property
    def idFactura(self):
        return self._idFactura

    #SET
    @idFactura.setter
    def idFactura(self, idFactura):
        self._idFactura=idFactura

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        self._fecha=fecha

    @property
    def referencia(self):
        return self._referencia

    @referencia.setter
    def referencia(self,referencia):
        self._referencia = referencia

    @property
    def subtotal(self):
        return self._subtotal

    @subtotal.setter
    def pregunta(self, subtotal):
        self._subtotal = subtotal

    @property
    def ir(self):
        return self._ir

    @ir.setter
    def ir(self,ir):
        self._ir = ir

    @property
    def iva(self):
        return self._iva

    @iva.setter
    def iva(self,iva):
        self._iva = iva

if __name__ == '__main__':
    factura1 = Factura(idFactura=1, fecha= " 2023/05/07", referencia = "fffe8423", subtotal=100.675, ir=100.67, iva=187.09)
    print(factura1)