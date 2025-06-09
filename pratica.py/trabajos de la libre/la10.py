# Laboratorio 10 - Clasificación con el Dataset Iris
# Autor: Jesús Portacio Valle


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# . Cargar los datos (solo las dos primeras características)
iris = load_iris()
X = iris.data[:, :2]  # Longitud y ancho del sépalo
y = iris.target

# . Dividir el conjunto de datos (70% entrenamiento, 30% prueba)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# . Crear el modelo de clasificación
model = LogisticRegression()

# . Entrenar el modelo
model.fit(X_train, y_train)

# . Hacer predicciones
y_pred = model.predict(X_test)

# . Calcular la precisión
precision = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {precision:.2f}")

# 8. Visualización de los resultados
df_test = pd.DataFrame(X_test, columns=['Sepal Length', 'Sepal Width'])
df_test['Real'] = y_test
df_test['Predicho'] = y_pred

# Gráfico de especies reales
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.scatterplot(
    x='Sepal Length', y='Sepal Width',
    hue='Real', data=df_test, palette='deep'
)
plt.title("Especies Reales")
plt.xlabel("Longitud del Sépalo")
plt.ylabel("Ancho del Sépalo")

# Gráfico de especies predichas
plt.subplot(1, 2, 2)
sns.scatterplot(
    x='Sepal Length', y='Sepal Width',
    hue='Predicho', data=df_test, palette='pastel'
)
plt.title("Especies Predichas")
plt.xlabel("Longitud del Sépalo")
plt.ylabel("Ancho del Sépalo")

plt.tight_layout()
plt.show()
