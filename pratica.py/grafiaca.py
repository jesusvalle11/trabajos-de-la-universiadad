import matplotlib.pyplot as plt

# Datos
nivel_asistencia = [90, 80, 95, 75, 85, 70, 95, 85, 75, 100]
puntaje_examen = [75, 60, 85, 55, 80, 50, 90, 82, 55, 95]

# Crear el scatter plot
plt.figure(figsize=(8,5))
plt.scatter(nivel_asistencia, puntaje_examen, color='blue', s=100)

# Etiquetas y título
plt.title('Relación entre Nivel de Asistencia y Puntaje en Examen')
plt.xlabel('Nivel de Asistencia (%)')
plt.ylabel('Puntaje en Examen')
plt.grid(True)

# Mostrar gráfico
plt.show()
