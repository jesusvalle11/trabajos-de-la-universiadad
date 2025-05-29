
from collections import deque
class Cola:
    def __init__(self):
        self.elementos = deque()
    
    def encolar(self, item):
        """Añade un elemento al final de la cola"""
        self.elementos.append(item)
    
    def desencolar(self):
        """Elimina y retorna el elemento del frente"""
        if not self.esta_vacia():
            return self.elementos.popleft()
        raise IndexError("La cola está vacía")
    
    def frente(self):
        """Muestra el primer elemento sin eliminarlo"""
        if not self.esta_vacia():
            return self.elementos[0]
        raise IndexError("La cola está vacía")
    
    def esta_vacia(self):
        """Verifica si la cola no contiene elementos"""
        return len(self.elementos) == 0
    
    def tamaño(self):
        """Devuelve el número de elementos en la cola"""
        return len(self.elementos)

# Ejemplo de uso completo
def simulacion_banco():
    cola_banco = Cola()
    
    # Llegan clientes al banco
    clientes = ["Cliente A", "Cliente B", "Cliente C", "Cliente D"]
    for cliente in clientes:
        print(f"Llega {cliente} y se forma en la cola")
        cola_banco.encolar(cliente)
    
    print(f"\nEstado actual de la cola: {cola_banco.tamaño()} clientes esperando")
    print(f"Próximo cliente a atender: {cola_banco.frente()}\n")
    
    # Proceso de atención
    while not cola_banco.esta_vacia():
        cliente_actual = cola_banco.desencolar()
        print(f"Atendiendo a {cliente_actual}")
        print(f"Clientes restantes: {cola_banco.tamaño()}\n")
    
    print("¡Todos los clientes han sido atendidos!")

simulacion_banco()