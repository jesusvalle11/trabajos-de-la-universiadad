import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def grafo():
    #crea y retorna la conexiones de grafo son predefinidas
    G = nx.Graph()
    G.add_edges_from([('A','B'),('A','C'),('B','D'),('B','E'),('C','F'),('E','F')])
    return G
# se visualiza el grafo y resalta como los nodos y las aristas
def dgrafo(G, pos, titulo, nodos=[], aristas=[]):
    nx.draw(G, pos, with_labels=True, node_color='lightblue')
    nx.draw_networkx_nodes(G, pos, nodelist=nodos, node_color='red')
    nx.draw_networkx_edges(G, pos, edgelist=aristas, edge_color='red', width=2)
    plt.title(titulo)
    plt.show()

def bfs(G, inicio):
    # es algoritmo breadth-first search
    visitados, cola = set(), deque([inicio]) # el conjunto de los nodos
    nodos, aristas = [inicio], [] 
    while cola:  #cola que procesa los nodos
        v = cola.popleft()
        for vecino in G.neighbors(v):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
                nodos.append(vecino)
                aristas.append((v, vecino))
    return nodos, aristas

def dfs(G, inicio):
    visitados, pila = set(), [inicio]
    nodos, aristas = [], []
    while pila:
        v = pila.pop()
        if v not in visitados:
            visitados.add(v)
            nodos.append(v)
            for vecino in reversed(list(G.neighbors(v))):
                if vecino not in visitados:
                    pila.append(vecino)
                    aristas.append((v, vecino))
    return nodos, aristas


print("") 

G = grafo()
pos = nx.spring_layout(G)

bfs_nodos, bfs_aristas = bfs(G, 'A')
print("BFS:", bfs_nodos)
dgrafo(G, pos, "BFS", bfs_nodos, bfs_aristas)

dfs_nodos, dfs_aristas = dfs(G, 'A')
print("DFS:", dfs_nodos)
dgrafo(G, pos, "DFS", dfs_nodos, dfs_aristas)