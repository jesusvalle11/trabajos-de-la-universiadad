class cuenta:

  def __init__(self,saldo):
    self._saldo=saldo
    self._nucons=0
    self._nuret=0

  def setsaldo(self,saldo):
    self._saldo=saldo

  def getsaldo(self):
    return self._saldo

  def consignar(self,monto):
    self._saldo=self._saldo+monto
    self._nucons = self._nucons+1

  def retirar(self,monto):
    if monto > self._saldo:
      print("saldo insuficiente")
    else:
      self._saldo=self._saldo-monto
      self._nuret=self._nuret+1

  def imprimir(self):
    print("saldo:",self._saldo,"\n",
    "numero de consinaciones:",self._nucons,"\n",
    "numero de retiros:",self._nuret,"\n")


class cuentaahorro(cuenta):
  def __init__(self,saldo):
    super().__init__(saldo)
    if(super().getsaldo()>=10000):
      self._activa=True
      print("cuenta activa  fue creada")
    else:
      self._activa=False
      print("cuenta inactiva")

  def consignar(self, monto):
    if(self._activa==True):
      super().consignar(monto)
    else:
      print("la cuenta no esta activa no se puede consignar")

  def retirar(self, monto):
    flag=super().getsaldo()-monto
    if(self._activa==True and flag>10000):
      super().retirar(monto)
    else:
      print("no puede retirar en una cuenta inactiva")

  def imprimir(self):
     super().imprimir()
     print("Cuenta Activa",self._activa)



class CuentaCorriente(cuenta):

    def __init__(self, saldo, sobregiro=0):
        super().__init__(saldo)
        self._sobregiro = sobregiro

    def retirar(self, monto):
        saldo_actual = self.getsaldo()
        if monto > saldo_actual + self._sobregiro:
            self._sobregiro += monto - (saldo_actual + self._sobregiro)
            self._saldo = 0
            self._nuret += 1
        else:
            self._saldo -= monto
        

    def consignar(self, monto):
        if self._sobregiro > 0:
            if monto >= self._sobregiro:
                monto -= self._sobregiro
                self._sobregiro = 0
            else:
                self._sobregiro -= monto
                monto = 0
        self._saldo += monto
        self._nucons += 1
       
    def imprimir(self):
        super().imprimir()
        print("Sobregiro:", self._sobregiro)


c = cuenta(24000)
c.imprimir()
c.consignar(20000)
print("nuevo saldo:",c.getsaldo())
c.retirar(44000)
print("nuevo saldo:",c.getsaldo())
c.imprimir()
print(" ")


ca = cuentaahorro(50000)
ca.imprimir()
ca.retirar(20000)
print("Nuevo saldo: ",ca.getsaldo())
ca.imprimir()


cc = CuentaCorriente(50000)
cc.imprimir()
cc.retirar(100000)
cc.imprimir()
cc.consignar(80000)
cc.imprimir()
cc.retirar(50000)
cc.imprimir()


