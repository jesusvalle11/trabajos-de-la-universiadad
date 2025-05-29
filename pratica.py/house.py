
class Fraccion:
  def __init__(self,num,den):
    self.__num=num
    self.__den=den
 
  def __init__(self):
    self.__num=0
    self.__den=0
 
  def getNum(self):
    return self.__num
 
  def setNum(self,num):
    self.__num=num
 
  def getDen(self):
    return self.__den
 
  def setDen(self,den):
    self.__den=den
 
  def suma(self,f1,f2):
    resultado = Fraccion()
    if f1.__den==f2.__den:
      resultado.__num=f1.__num + f2.__num
      resultado.__den=f1.__den
 
    else:
      resultado.__num=(f1.__num*f2.__den)+(f2.num*f1.__den)
      resultado.__den=f1.__den*f2.__den
    return resultado
 
  def resta(self,f1,f2):
    resultado = Fraccion()
    if f1.__den==f2.__den:
      resultado.__num=f2.__num - f1.__num
      resultado.__den=f1.__den
 
    else:
      resultado.__num=(f1.__num*f2.__den)-(f2.num*f1.__den)
      resultado.__den=f1.__den*f2.__den
    return resultado

  def mul(self,f1,f2):
    resultado = Fraccion()
    resultado.__num=f1.__num*f2._Fraccion__num
    resultado.__den=f1.__den*f2.__den
    return resultado

  def div(self,f1,f2):
    resultado = Fraccion()
    resultado.__num=f1.__num * f2._Fraccion__den
    resultado.__den=f1.__den * f2.__num
    return resultado
    


 
f1=Fraccion()
f1.setNum(2)
f1.setDen(3)
f2=Fraccion()
f2.setNum(4)
f2.setDen(3)
f3=Fraccion()
f3=f1.suma(f1,f2)

print(f3.getNum(),"/",f3.getDen())
f3=f1.resta(f1,f2)
print(f3.getNum(), "/", f3.getDen())
f3=f1.mul(f1,f2)
print(f3.getNum(), "/", f3.getDen())
f3=f1.div(f1,f2)
print(f3.getNum(), "/", f3.getDen())
print("")

class hora:
  
    def __init__(self,h=0, mm=0,ss=0 ):
        self.__h=h
        self.__mm=mm
        self.__ss=ss
    def lee(self):
      self.__h= int(input("ingrese las horas:")) 
      self.__mm=int(input("ingrese el valor de minutos:"))
      self.__ss= int(input("ingrese los segundos: "))
      
    def validar(self):
        if (0 <=self.__h <= 24) and (0 <= self.__mm <= 60) and (0 <= self.__ss <= 60):
          print("hora correcta")
        else:
          print("hora incorrecta")
            
    def get_h(self):
      return self.__h
    
    def get_mm(self):
      return self.__mm
    
    def get_ss(self):
      return self.__ss
    
    def set_h(self,h):
      self.__h=h
    def set_mm(self,mm):
      self.__mm=mm 
    def set_ss(self,ss):
      self.__ss=ss   
      
    def print(self):
        print(f"{self.__h:02}:{self.__mm:02}:{self.__ss:02}")
    
    def aSegundos(self):
        return self.__h* 3600 + self.__mm * 60 + self.__ss

    def siguiente(self):
        self.__ss += 1
        if self.__ss == 60:
            self.__ss = 0
            self.__mm += 1
            if self.__mm == 60:
                self.__mm = 0
                self.__h += 1
                if self.__h == 24:
                    self.__h = 0

    def anterior(self):
        self.__ss -= 2
        if self.__ss == -2:
            self.__ss = 59
            self.__mm -= 2
            if self.__mm == -2:
                self.__mm = 59
                self.__h -= 2
                if self.__h == -2:
                    self.__h = 23

    def igualQue(self, otra_h):
        return self.aSegundos() == otra_h.aSegundos()


    def menorQue(self, otra_h):
        return self.aSegundos() < otra_h.aSegundos()

    def mayorQue(self, otra_h):
        return self.aSegundos() > otra_h.aSegundos()    
    
    
horaA= hora(7,3,21)    
horaN= hora(8,33,12)
horaA.print()
horaN.print()
print(horaA.aSegundos())
horaA.siguiente()
horaA.print()
horaA.anterior()
horaA.print()
print(horaA.igualQue(horaN))  # es falso poque son  ahora diferente
print(horaA.menorQue(horaN))  # es verdadero por mayo a horaN 
print(horaA.mayorQue(horaN))  # Falso 