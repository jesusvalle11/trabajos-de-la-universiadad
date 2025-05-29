import networkx as nx
import matplotlib.pyplot as plt
import heapq
import time

# Función original de Dijkstra (sin cambios)
def dijkstra(grafo, inicio, destino):
    distancia = {nodo: float('inf') for nodo in grafo}
    distancia[inicio] = 0
    anteriores = {nodo: None for nodo in grafo}
    cola = [(0, inicio)]

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)
        if nodo_actual == destino:
            break
        for vecino, peso in grafo[nodo_actual].items():
            nueva_distancia = distancia_actual + peso
            if nueva_distancia < distancia[vecino]:
                distancia[vecino] = nueva_distancia
                anteriores[vecino] = nodo_actual
                heapq.heappush(cola, (nueva_distancia, vecino))

    camino = []
    actual = destino
    while actual:
        camino.append(actual)
        actual = anteriores[actual]
    camino.reverse()
    return distancia[destino], camino

# Función para visualizar el grafo ponderado con el camino más corto
def visualizar(grafo_dict, camino, titulo):
    G = nx.Graph()
    for nodo, vecinos in grafo_dict.items():
        for vecino, peso in vecinos.items():
            G.add_edge(nodo, vecino, weight=peso)

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    
    # Crear lista de aristas del camino
    aristas_camino = [(camino[i], camino[i+1]) for i in range(len(camino)-1)]

    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_nodes(G, pos, nodelist=camino, node_color='orange')
    nx.draw_networkx_edges(G, pos, edgelist=aristas_camino, edge_color='red', width=2)
    plt.title(titulo)
    plt.show()

# Diccionario del grafo ponderado
grafo = {
    'A': {'B': 5, 'D': 9},
    'B': {'A': 5, 'C': 3, 'D': 2},
    'C': {'B': 3, 'D': 1, 'E': 6},
    'D': {'A': 9, 'B': 2, 'C': 1, 'E': 2},
    'E': {'C': 6, 'D': 2, 'F': 4},
    'F': {'E': 4}
}

#  Cálculo de rutas y visualización 
print(" RESULTADOS DEL ALGORITMO DE DIJKSTRA")

def resultado(inicio, destino, n):
    distancia, camino = dijkstra(grafo, inicio, destino)
    print(f"\n{n}. Ruta más corta de {inicio} a {destino}:")
    print(f"   - Distancia: {distancia}")
    print(f"   - Camino: {' → '.join(camino)}")
    visualizar(grafo, camino, f"Dijkstra: {inicio} → {destino}")
    time.sleep(1)

resultado('A', 'B', 1)
resultado('A', 'F', 2)
resultado('B', 'E', 3)
resultado('C', 'F', 4)
