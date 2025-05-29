class NodoPerro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
        self.siguiente = None
        self.anterior = None

class ListaDoblePerros:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_perro(self, nombre, raza):
        nuevo_nodo = NodoPerro(nombre, raza)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    def buscar(self, nombre, raza):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre and actual.raza == raza:
                return actual
            actual = actual.siguiente
        return None

    def borrar(self, nombre, raza):
        actual = self.buscar(nombre, raza)
        if actual:
            if actual.anterior:
                actual.anterior.siguiente = actual.siguiente
            else:
                self.cabeza = actual.siguiente
            if actual.siguiente:
                actual.siguiente.anterior = actual.anterior
            else:
                self.cola = actual.anterior
        else:
            print(f"El perro con nombre {nombre} y raza {raza} no existe en la lista.")

    def agregarDespuesDe(self, nombre_e, raza_e, nombre_n, raza_n):
        existente = self.buscar(nombre_e, raza_e)
        if existente:
            nuevo_nodo = NodoPerro(nombre_n, raza_n)
            nuevo_nodo.siguiente = existente.siguiente
            nuevo_nodo.anterior = existente
            if existente.siguiente:
                existente.siguiente.anterior = nuevo_nodo
            else:
                self.cola = nuevo_nodo
            existente.siguiente = nuevo_nodo
        else:
            print(f"El perro con nombre {nombre_e} y raza {raza_e} no existe en la lista.")

    def mostrar_perros_adelante(self):
        actual = self.cabeza
        while actual:
            print(f"Nombre: {actual.nombre}, Raza: {actual.raza}")
            actual = actual.siguiente

    def mostrar_perros_atras(self):
        actual = self.cola
        while actual:
            print(f"Nombre: {actual.nombre}, Raza: {actual.raza}")
            actual = actual.anterior



lista_perros = ListaDoblePerros()
lista_perros.agregar_perro("Max", "Labrador")
lista_perros.agregar_perro("Bella", "Beagle")
lista_perros.agregar_perro("Rocky", "Bulldog")

print("Lista en orden:")
lista_perros.mostrar_perros_adelante()

print("\nLista en reversa:")
lista_perros.mostrar_perros_atras()


print("\nBorrando a Bella (Beagle):")
lista_perros.borrar("Bella", "Beagle")
lista_perros.mostrar_perros_adelante()


print("\nAgregando a Luna (Chihuahua) después de Max (Labrador):")
lista_perros.agregarDespuesDe("Max", "Labrador", "Luna", "Chihuahua")
lista_perros.mostrar_perros_adelante()


print("\n")


class Vaca:
    def __init__(self, nombre, codigo, raza, next=None):
        self.nombre = nombre
        self.codigo = codigo
        self.raza = raza
        self.next = next

class Corral:
    def __init__(self):
        self.head = None

    def agregar(self, vaca):
        if self.head is None:
            self.head = vaca
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = vaca

    def borrar(self, codigo):
      actual = self.head
      anterior = None

      while actual and actual.codigo != codigo:
        anterior = actual
        actual = actual.next
      if not actual: 
          return False
      if not anterior:  
         self.head = actual.next
      else: 
         anterior.next = actual.next
      return True

    def agregarDespuesDe(self, codigo, nueva_vaca): 
        actual = self.head
        while actual is not None:
            if actual.codigo == codigo:
                nueva_vaca.next = actual.next
                actual.next = nueva_vaca
                return True  
            actual = actual.next
        return False  

    def buscar(self, codigo):
        actual = self.head
        while actual is not None:
            if actual.codigo == codigo:
                return actual  
            actual = actual.next
        return None  

    def mostrar(self):
        actual = self.head
        while actual is not None:
            print(actual.nombre, actual.codigo, actual.raza)
            actual = actual.next


corral = Corral()
corral.agregar(Vaca(nombre="Juanita", codigo=1001, raza="Holstein"))
corral.agregar(Vaca(nombre="Lola", codigo=1002, raza="Jersey"))
corral.mostrar()


corral.agregarDespuesDe(1001, Vaca(nombre="Mimi", codigo=1003, raza="Angus"))
print("\nDespués de agregar Mimi:")
corral.mostrar()


vaca_encontrada = corral.buscar(1002)
if vaca_encontrada:
    print(f"\nVaca encontrada: {vaca_encontrada.nombre}, {vaca_encontrada.codigo}, {vaca_encontrada.raza}")
else:
    print("\nVaca no encontrada")


if corral.borrar(1001):
    print("\nVaca con código 1001 eliminada")
else:
    print("\nVaca no encontrada")

print("\nDespués de eliminar Juanita:")
corral.mostrar()
