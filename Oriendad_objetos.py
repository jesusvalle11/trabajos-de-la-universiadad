import math

class operaciones:
  def __init__(self,n1,n2):
    self.__n1=n1
    self.__n2=n2

  def suma(self):
    r=self.__n1+self.__n2
    print("la suma es:",r)

  def resta(self):
    r=self.__n1-self.__n2
    print("la resta es:", r)

  def multiplicacion(self):
    r=self.__n1*self.__n2
    print("multiplicacion es:", r)

  def divicion(self):
    r=self.__n1/self.__n2
    print("es divicion: ", r) 

  def raiz(self):
    r=math.sqrt(self.__n1)
    print("la raiz de esta vuelta es:", r)

  def potencia(self):
    r= pow(self.__n1,self.__n2)
    print("la portecia es:", r)

op =operaciones(5,10)
op.suma()
op.resta()
op.multiplicacion()  
op.divicion()
op.raiz()
op.potencia()    
print("")          
      
class planeta:
  def __init__(self,nombre,cantidadsatelites,masa,volumen,diametro,distacia,esobservable):
    self.__nombre=nombre
    self.__cantidadsatelites=int(cantidadsatelites)
    self.__masa=float(masa)
    self.__volumen=float(volumen)
    self.__diametro=int(diametro)
    self.__distacia=int(distacia)
    self.__esobservable=esobservable

  def mostrar(self):
    print("el nombre de planeta es",self.__nombre,"\n"
    "la cantidad de satalites es",self.__cantidadsatelites,"\n"
    "la masa es",self.__masa,"\n"
    "el volumen es",self.__volumen,"\n"
    "el diametro es",self.__diametro,"\n"
    "la distacias es",self.__distacia)

  def densidad(self):
    distancia = self.__masa / self.__volumen
    print("la densidad es", distancia)

  def unidad_astronomica(self):
    ua= self.__distacia / 149597870
    if ua > 2.1 and ua < 3.4:
      print("elEl planeta está dentro del cinturón de asteroides")
      print("unidad astronomica:",ua)
      return True
    else:
      print("el planeta no está dentro del cinturón de asteroides")
      print("unidad astronomica:",ua)
      return False

  def esobservable(self):
    if self.__esobservable== True:
      print("el planeta es observable")
    else:
      print("el planeta no es observable")

planeta = planeta("saturno","1","23","33","74","434",True and False)
planeta.mostrar()
planeta.densidad()
planeta.unidad_astronomica()
planeta.esobservable()

