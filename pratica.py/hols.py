import random

notas = []
suma= 0
prom = []

for fila in range(30):
    notas.append([])
    for col  in range(6):
        notas[fila].append(round(random.uniform(1,5),2))
        print(notas[fila][col],end= ' ')
    print(" ")

for i in range(6):
    for j in range(30):
      suma =suma+notas[j][i]
    prom = suma / 30
    suma = 0
print("el promedio de la asignatura es ", round(prom,2))

for i in range(30):
    for j in range(6):
        suma = suma + notas[i][j]
    prom = suma / 6
    suma = 0
print("el promedio de notas por estudiante es:" , round(prom,2))

suma_total = 0

for i in range (6):
    for j in range(30):
        suma_total += notas[i][j]
promedio = suma_total / (30* 6)
print("el promedio de notas de estudiantes y asinaturas",round(promedio,2))


from collections import deque

class VacunacionCola:
    def _init_(self):
        # Inicia cola vacía usando deque
        self.cola = deque()
    
    def registrar_llegada(self, nombre, id):
        paciente = {"nombre": nombre, "id": id}
        self.cola.append(paciente)
        return f"{nombre} (ID: {id}) ha sido registrado/a en la cola."
    
    def atender_siguiente(self):
        if not self.cola:
            return "No hay personas en la cola."
        
        paciente_atendido = self.cola.popleft()
        return f"Atendiendo a {paciente_atendido['nombre']} (ID: {paciente_atendido['id']})."
    
    def consultar_cantidad(self):
        return len(self.cola)
    
    def mostrar_siguiente(self):
        if not self.cola:
            return "No hay personas en la cola."
        
        return f"La siguiente persona es {self.cola[0]['nombre']} (ID: {self.cola[0]['id']})."
    
    def mostrar_cola_completa(self):
        if not self.cola:
            return "La cola está vacía."
        
        resultado = "Personas en la cola (orden de atención):\n"
        for i, paciente in enumerate(self.cola, 1):
            resultado += f"{i}. {paciente['nombre']} (ID: {paciente['id']})\n"
        return resultado


cola = VacunacionCola()
    
    # Registrar llegadas de pacientes
print(cola.registrar_llegada("Sarai", 1123890618))
print(cola.registrar_llegada("Ana", 1148938121))
print(cola.registrar_llegada("Carlos", 1042654565))
    
# Mostrar la cola completa
print("\n" + cola.mostrar_cola_completa())
    
# Mostrar al siguiente paciente a ser atendido
print(cola.mostrar_siguiente())
    
# Atender a la siguiente persona
print(cola.atender_siguiente())
    
# Consultar la cantidad de personas en la cola después de atender
print(f"Cantidad de personas en la cola: {cola.consultar_cantidad()}")
    
# Mostrar nuevamente la cola
print("\n" + cola.mostrar_cola_completa())