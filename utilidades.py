from collections import deque
grafo = {
    "Quito": [("Cuenca", 500), ("Latacunga", 90)],
    "Latacunga": [("Quito", 90), ("Ambato", 40)],
    "Ambato": [("Latacunga", 40), ("Riobamba", 60)],
    "Riobamba": [("Ambato", 60), ("Cuenca", 150)],
    "Cuenca": [("Quito", 500), ("Riobamba", 150), ("Loja", 200)],
    "Loja": [("Cuenca", 200)]
}
# R1
# Complejidad: O(V + E)

def mostrar_grados(grafo):

    print("\nGrado de cada ciudad\n")

    for ciudad in grafo:

        grado = len(grafo[ciudad])

        print(ciudad, "tiene", grado, "conexiones")
# R2
# Complejidad: O(V + E)

def bfs(grafo, inicio):

    visitados = set()

    cola = deque()

    niveles = {}

    visitados.add(inicio)

    cola.append((inicio, 0))

    while cola:

        ciudad, nivel = cola.popleft()

        niveles[ciudad] = nivel

        for vecino, distancia in grafo[ciudad]:

            if vecino not in visitados:

                visitados.add(vecino)

                cola.append((vecino, nivel + 1))

    return niveles
def obtener_ruta(grafo, inicio, destino):

    cola = deque([inicio])

    padre = {inicio: None}

    while cola:

        actual = cola.popleft()

        if actual == destino:
            break

        for vecino, _ in grafo[actual]:

            if vecino not in padre:

                padre[vecino] = actual

                cola.append(vecino)

    ruta = []

    while destino is not None:

        ruta.append(destino)

        destino = padre[destino]

    ruta.reverse()

    return ruta
import heapq
# Dijkstra: O((V + E) log V)
def dijkstra(grafo, origen):
    """Devuelve {ciudad: distancia_minima_desde_origen}."""

    dist = {ciudad: float('inf') for ciudad in grafo}
    dist[origen] = 0

    heap = [(0, origen)]  # cola de prioridad

    while heap:
        d, u = heapq.heappop(heap)  # el más cercano pendiente

        if d > dist[u]:
            continue  # ya teníamos una ruta mejor

        for vecino, peso in grafo[u]:
            if dist[u] + peso < dist[vecino]:  # relajación
                dist[vecino] = dist[u] + peso
                heapq.heappush(heap, (dist[vecino], vecino))

    return dist