# Importar librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
    "Ventas": [25, 30, 28, 35, 40, 50, 55, 60, 70, 80, 75, 90]
}

df = pd.DataFrame(data)


print("Datos de ventas mensuales:")
print(df)


ventas_array = np.array(df["Ventas"])


media = np.mean(ventas_array)
mediana = np.median(ventas_array)
desviacion_std = np.std(ventas_array)
total_ventas = np.sum(ventas_array)
mes_mayor_venta = df.loc[df["Ventas"].idxmax()]
mes_menor_venta = df.loc[df["Ventas"].idxmin()]


print("\nEstadísticas de ventas:")
print(f"Media de ventas: {media:.2f} mil")
print(f"Mediana de ventas: {mediana:.2f} mil")
print(f"Desviación estándar: {desviacion_std:.2f}")
print(f"Total de ventas del año: {total_ventas} mil")
print(f"Mes con mayor venta: {mes_mayor_venta['Mes']} ({mes_mayor_venta['Ventas']} mil)")
print(f"Mes con menor venta: {mes_menor_venta['Mes']} ({mes_menor_venta['Ventas']} mil)")


plt.figure(figsize=(10, 6))
plt.plot(df["Mes"], df["Ventas"], marker='o', linestyle='-', color='blue')
plt.title("Ventas Mensuales del Negocio (en miles)", fontsize=14)
plt.xlabel("Mes", fontsize=12)
plt.ylabel("Ventas (mil)", fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
