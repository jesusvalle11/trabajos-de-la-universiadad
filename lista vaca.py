
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
