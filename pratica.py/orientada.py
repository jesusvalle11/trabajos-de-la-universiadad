

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
      resultado.__num=(f1.__num*f2.__den)+(f1.den*f2.__num)
      resultado.__den=f1.__den*f2.__den
    return resultado
 
  def resta(self,f1,f2):
    resultado = Fraccion()
    if f1.__den==f2.__den:
      resultado.__num=f1.__num - f2.__num
      resultado.__den=f1.__den
 
    else:
      resultado.__num=(f1.__num*f2.__den)-(f1.den*f2.__num)
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


class Planeta:
    def __init__(self, nombre, cantidadsatelites, masa, volumen, diametro, distancia):
        self.__nombre = nombre
        self.__cantidadsatelites = int(cantidadsatelites)
        self.__masa = float(masa)
        self.__volumen = float(volumen)
        self.__diametro = int(diametro)
        self.__distancia = int(distancia)

    def mostrar(self):
        print("El nombre del planeta es", self.__nombre, "\n"
              "La cantidad de satélites es", self.__cantidadsatelites, "\n"
              "La masa es", self.__masa, "\n"
              "El volumen es", self.__volumen, "\n"
              "El diámetro es", self.__diametro, "\n"
              "La distancia es", self.__distancia)

    def densidad(self):
        densidad = self.__masa / self.__volumen
        print("La densidad es", densidad)

    def unidad_astronomica(self):
        ua = self.__distancia / 149597870  
        print("Unidad astronómica:", ua)
        return ua

    def es_observable(self):
        ua = self.unidad_astronomica()
        if ua > 3.4:
            print("El planeta es observable porque está más allá del cinturón de asteroides.")
        else:
            print("El planeta no es observable porque está dentro o antes del cinturón de asteroides.")


planeta = Planeta("Saturno", "41", "4545423", "2323233", "722323234", "1195000000")  #utile el propio valor de distacia de saturno
planeta.mostrar()
planeta.densidad()
planeta.es_observable()



def esta_vivo(vida):
  vida = int(input("ingrese el valor de vida: "))
  if vida > 0:
    return True
  else:
    return False
  
resultado = esta_vivo(0)  

