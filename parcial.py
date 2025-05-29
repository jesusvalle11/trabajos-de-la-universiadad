class vaca_corp:
    def __init__(self,nombre,peso):
        self.nombre=nombre
        self.peso=peso
        self.siguiente=None
        
class listav:
    def __init__(self):
        self.primero =None
        self.vaca_r=[]
        
    def vacia(self):
        return self.primero ==  None
        
    def agregar(self,nombre,peso,posicion=None):
        nueva_v= vaca_corp(nombre, peso)
        
        if self.vacia():
            self.primero= nueva_v
        elif posicion == "inicio":
            nueva_v.siguiente= self.primero
            self.primero=nueva_v
        elif posicion == "final" or posicion == None:
            actual = self.primero
            while actual.siguiente:
                actual= actual.siguiente
            actual.siguiente = nueva_v
        else:
            actual= self.primero
            for _ in range(posicion-1):
                if actual.siguiente is None:
                   break
                actual = actual.siguiente
            nueva_v.siguiente= actual.siguiente
            actual.siguiente = nueva_v
            
    def remplazar_v(self,posicion):
        if self.vacia():
            print("no hay vacas en la lista: ")
            return
        elif posicion < 0:
            print("posicion equivocada. ")
            return
        if not self.vaca_r:
            print("no hay vaacas de reemplazo disponible. ")
            return
            
        nueva_v = self.vaca_r.pop(0)
        
        if posicion == 0:
            vaca_reemplazada=self.primero
            self.primero= nueva_v
            self.primero.siguiente= vaca_reemplazada.siguiente
        else:
            actual = self.primero
            for _ in range(posicion-1):
                if actual.siguiente is None:
                    print(f"posicion {posicion} no es valida. ")
                    return
                actual = actual.siguiente
            vaca_reemplazada= actual.siguiente
            actual.siguiente = nueva_v
            nueva_v.siguiente = vaca_reemplazada.siguiente
            
        print(f"Se reemplazó la vaca en la posición {posicion}:")
        print(f"Vaca eliminada: {vaca_reemplazada.nombre}, Peso: {vaca_reemplazada.peso} kg")
        print(f"Vaca agregada: {nueva_v.nombre}, Peso: {nueva_v.peso} kg")

            
    def lista_nombres(self):
        actual = self.primero
        while actual:
            print(f"vaca: {actual.nombre} , peso: {actual.peso} kg")
            actual = actual.siguiente
    
    def lista_menos_ps(self,peso_max):
        actual = self.primero
        while actual:
            if actual.peso < peso_max:
                print(f"vaca: {actual.nombre}, peso: {actual.peso} kg ")
            actual= actual.siguiente
            
lista_vacas = listav()

for i in range(1,31):
    lista_vacas.agregar(f"vaca{i}", 500 + i*10, "final")
    
for i in range(31,51):
    lista_vacas.vaca_r.append(vaca_corp(f"vaca{i}",500+ i* 10))
    
    
print("listado de todas la vacas por nombre: ")
lista_vacas.lista_nombres()

print("\nlistado de vacas con menos de 600kg:")
lista_vacas.lista_menos_ps(600)

print("\n reemplazado la vaca en la posicion 2: ")
lista_vacas.remplazar_v(2)

print("\n listado de todas las vacas por nombre del rempazo: ")
lista_vacas.lista_nombres()
