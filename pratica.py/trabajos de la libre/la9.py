import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = {
    "Estudiante": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack"],
    "Matemáticas": [85, 92, 78, 90, 88, 76, 95, 89, 82, 94],
    "Ciencias": [90, 85, 80, 88, 92, 75, 95, 87, 81, 93],
    "Historia": [78, 82, 88, 90, 85, 80, 92, 84, 79, 91],
}

df = pd.DataFrame(data)


notas = df[["Matemáticas", "Ciencias", "Historia"]].to_numpy()

# Promedio por estudiante
promedios_estudiantes = np.mean(notas, axis=1)
df["Promedio"] = promedios_estudiantes

# Promedio, máximo y mínimo por asignatura
promedios_asignaturas = np.mean(notas, axis=0)
maximos = np.max(notas, axis=0)
minimos = np.min(notas, axis=0)

# Mostrar los resultados
print("DataFrame con promedios:")
print(df)
print("\nPromedios por asignatura:")
for i, materia in enumerate(["Matemáticas", "Ciencias", "Historia"]):
    print(f"{materia}: {promedios_asignaturas[i]:.2f} (Máx: {maximos[i]}, Mín: {minimos[i]})")

#  Visualización - Promedio por asignatura
asignaturas = ["Matemáticas", "Ciencias", "Historia"]

plt.figure(figsize=(8, 5))
plt.bar(asignaturas, promedios_asignaturas, color=['blue', 'green', 'orange'])
plt.title("Promedio de Calificaciones por Asignatura")
plt.ylabel("Promedio")
plt.ylim(70, 100)
plt.grid(axis='y')
plt.show()

#  Visualización - Promedio por estudiante
plt.figure(figsize=(10, 5))
plt.plot(df["Estudiante"], df["Promedio"], marker='o', linestyle='-', color='purple')
plt.title("Promedio de Calificaciones por Estudiante")
plt.ylabel("Promedio")
plt.xticks(rotation=45)
plt.ylim(70, 100)
plt.grid(True)
plt.tight_layout()
plt.show()
