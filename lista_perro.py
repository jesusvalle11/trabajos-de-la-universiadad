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

