
from abc import ABC, abstractmethod
import math
class Forma(ABC):
    @abstractmethod
    def calcularArea(self):
        pass

    @abstractmethod
    def calcularPerimetro(self):
        pass

class Triangulo(Forma):
    def __init__(self, b, a, h):
        self._b = b
        self._a = a
        self._h = h

    def calcularArea(self):
        area = (self._b * self._a) / 2
        return area

    def tipo(self):
        if self._b == self._a and self._a == self._h:
            tipo = "Equilatero"
        elif (self._b == self._a and self._a != self._h) or (self._b == self._h and self._h != self._a) or (self._a == self._h and self._h != self._b):
            tipo = "Isosceles"
        elif (self._b != self._a and self._a != self._h and self._h != self._b):
            tipo = "Escaleno"
        return tipo

    def calcularPerimetro(self):
        if self.tipo() == "Equilatero":  
            perimetro = self._a * 3
        elif self.tipo() == "Escaleno":
            perimetro = self._a + self._b + self._h
        elif self.tipo() == "Isosceles":
            if self._b == self._a:
                perimetro = (self._b * 2) + self._h
            elif self._h == self._a:
                perimetro = (self._h * 2) + self._b
            elif self._b == self._h:
                perimetro = (self._b * 2) + self._a
        return perimetro



class Cuadrado(Forma):
    def __init__(self, lado):
        self._lado=lado
        
    def calcularArea(self):
        area = self._lado*self._lado
        return area
    
    def calcularPerimetro(self):
        perimetro = self._lado *4 
        return perimetro
    


class Circulo(Forma):
    
    def __init__(self,diametro):
        self._diametro=diametro
        
    def calcularArea(self):
        radio = self._diametro / 2
        area = math.pi * math.pow(radio,2)
        return area
    
    def calcularPerimetro(self):
        perimetro = math.pi * self._diametro
        return perimetro
    

        
class Restagulo(Forma):        

    def __init__(self,b,a):
        self._b=b
        self._a=a
    
    def calcularArea(self):
        area = self._b * self._a
        return area
    
    def calcularPerimetro(self):
        perimetro = 2*(self._b + self._a)
        return perimetro
    

t = Triangulo(2, 5, 3)
print("el triangulo es: ", t.tipo())
print("el area es: ", t.calcularArea())
print("el perimetro es: ", t.calcularPerimetro())
print("")
        
c= Cuadrado(6)
print("el area de cuadrado es : ",c.calcularArea())
print("el perimetro  de cuadrado: ",c.calcularPerimetro())
print(" ")

C = Circulo(18)
print("el area de Circulo es : ",round(C.calcularArea()))
print("el perimetro  de Circulo: ",round(C.calcularPerimetro()))
print(" ")  

R = Restagulo(5,12)  
print("el area de Restagulo es : ",R.calcularArea())
print("el perimetro  de Restagulo: ",R.calcularPerimetro())  
        
        
def calcular_valor_lote(peso,cantidad):
    if 1000<= peso <= 1500:
        precio_kg=7200
    elif 1501 <= peso <= 2000:
        precio_kg= 7000
    elif peso < 1000:
        precio_kg = 7500
    else:
        return "no tiene la logistica para hacer el negocio."     
    
    valor_total = peso * precio_kg
    promedio_t = valor_total /cantidad
    return f"Valor total del lote: {valor_total} \nPromedio por ternero: {promedio_t}"


peso_total = float(input("Ingrese el peso total del lote en kg: "))
cantidad_terneros = int(input("Ingrese la cantidad de terneros: "))
resultado = calcular_valor_lote(peso_total, cantidad_terneros)
print(resultado)
print("")

#persintencia basada en archivos
from  io import open
import random
mayor = 0

objecto= open("archivo.txt","a")
lista = objecto.read()
objecto.close()
for i in range(len(lista)):
    print(lista[i])
        
from io import open

objeto = open("archivo.txt","w")
objeto.write("esto es una prueba\n"
"hoy estudiamos python y manejo de archivos")
objeto.close()
