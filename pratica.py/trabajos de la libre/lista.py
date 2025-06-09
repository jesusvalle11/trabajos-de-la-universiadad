
tareas = []

# . Definir funciones para agregar, eliminar y mostrar tareas
def agregar_tarea():
    tarea = input("Ingrese la tarea: ")
    tareas.append(tarea)
    print("Tarea agregada con éxito.")

def eliminar_tarea():
    try:
        mostrar_tareas()
        indice = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            print(f"Tarea eliminada: {tarea_eliminada}")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Por favor ingrese un número válido.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def mostrar_tareas():
    if not tareas:
        print("No hay tareas en la lista.")
    else:
        print("Lista de tareas:")
        # . Usar un bucle for para mostrar las tareas
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")

# . Implementar un menú principal usando un bucle while
def menu():
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar tareas")
        print("4. Salir")

        # . Usar if-elif-else para manejar las opciones del menú
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            eliminar_tarea()
        elif opcion == "3":
            mostrar_tareas()
        elif opcion == "4":
            print("Saliendo del programa...")
            break  # 7. Usar break para salir
        else:
            print("Opción inválida. Intente de nuevo.")


menu()
