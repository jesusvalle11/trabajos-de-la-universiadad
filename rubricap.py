
class vaca_corp:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso
        self.siguiente = None

class listav:
    def __init__(self):
        self.primero = None

    def agregar(self, nombre, peso):
        nueva_v = vaca_corp(nombre, peso)
        if not self.primero:
            self.primero = nueva_v
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_v
    
    def lista_nombres(self):
        actual = self.primero
        while actual:
            print(f"vaca: {actual.nombre} , peso: {actual.peso} kg")
            actual = actual.siguiente

    def lista_menos_ps(self, peso_max=500):
        actual = self.primero
        while actual:
            if actual.peso < peso_max:
                print(f"vaca: {actual.nombre}, peso: {actual.peso} kg ")
            actual = actual.siguiente
    
    def remplazar_v(self, nombre_vaca, lista_reemplazo):
        actual = self.primero
        previo = None
        while actual:
            if actual.nombre == nombre_vaca:
                if lista_reemplazo.primero:
                    vaca_reemplazo = lista_reemplazo.primero
                    lista_reemplazo.primero = lista_reemplazo.primero.siguiente
                    vaca_reemplazo.siguiente = actual.siguiente
                    if previo:
                        previo.siguiente = vaca_reemplazo
                    else:
                        self.primero = vaca_reemplazo
                    print(f"Reemplazada {nombre_vaca} por {vaca_reemplazo.nombre}")
                    return
            previo = actual
            actual = actual.siguiente
        print(f"Vaca {nombre_vaca} no encontrada en la lista.")


lista_vacas = listav()
for nombre, peso in [
    ("jesus", 500), ("Lope", 300), ("mariba", 450), ("Pancha", 380), ("Braulio", 520),
    ("Carmela", 410), ("ippo", 470), ("Margarita", 360), ("pasio", 490), ("Pepe", 430),
    ("sapeee", 400), ("Mano", 390), ("valle", 515), ("zapatoca", 370), ("Nubia", 445),
    ("Chipi", 395), ("Padre", 405), ("tubara", 455), ("pero sabe cuando cambia", 385), ("esmelada", 465),
    ("Felipe", 375), ("Petunia", 425), ("Gaspar", 410), ("Florinda", 395), ("Tiburcio", 505),
    ("Josefa", 480), ("Anacleto", 460), ("Maruja", 435), ("Clemente", 495), ("Bartola", 375)
]:
    lista_vacas.agregar(nombre, peso)


lista_vacas_r = listav()
for nombre, peso in [
    ("tacio", 305), ("Lucero", 340), ("Toribio", 390), ("Bambina", 420), ("Nicanor", 370),
    ("Estrellita", 310), ("Pascual", 450), ("Malena", 465), ("Firulais", 335), ("Ventura", 480),
    ("Cascabel", 410), ("Tronquito", 360), ("Flor", 395), ("Relámpago", 500), ("Aurorita", 445),
    ("Maxi", 520), ("Bruni", 375), ("PericoWw", 430), ("Cleotilde", 460), ("Donatella", 385)
]:
    lista_vacas_r.agregar(nombre, peso)

print("\nLista de vacas en línea de ordeño:")
lista_vacas.lista_nombres()

print("\nLista de vacas de reemplazo:")
lista_vacas_r.lista_nombres()

print("\nReemplazando una vaca...")
lista_vacas.remplazar_v("Pancha", lista_vacas_r)

print("\nLista de vacas actualizada en línea de ordeño:")
lista_vacas.lista_nombres()

print("\nVacas con peso menor a 500 kg:")
lista_vacas.lista_menos_ps()