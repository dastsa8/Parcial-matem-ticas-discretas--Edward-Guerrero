
import matplotlib.pyplot as plt
import heapq

grafo = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 1, 'D': 7},
    'C': {'A': 4, 'B': 1, 'E': 3},
    'D': {'B': 7, 'E': 2, 'F': 1},
    'E': {'C': 3, 'D': 2, 'F': 5},
    'F': {'D': 1, 'E': 5}
}

#nodos
posiciones = {
    'A': (0, 0),
    'B': (1, 2),
    'C': (2, 0),
    'D': (3, 3),
    'E': (3, 0),
    'F': (4, 2)
}

#def para algoritmo de Dijkstra
def dijkstra(grafo, inicio, fin):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    anterior = {}
    cola = [(0, inicio)]

    while cola:
        costo_actual, nodo_actual = heapq.heappop(cola)

        if nodo_actual == fin:
            break

        for vecino, peso in grafo[nodo_actual].items():
            nueva_distancia = costo_actual + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anterior[vecino] = nodo_actual
                heapq.heappush(cola, (nueva_distancia, vecino))

    #camino
    camino = []
    actual = fin
    while actual in anterior:
        camino.insert(0, actual)
        actual = anterior[actual]
    if camino:
        camino.insert(0, inicio)
    
    return camino, distancias[fin]

#visualización del grafo
def visualizar_grafo(grafo, posiciones, camino=None):
    fig, ax = plt.subplots()
    for nodo, vecinos in grafo.items():
        x, y = posiciones[nodo]
        ax.scatter(x, y, s=100, color='skyblue')
        ax.text(x, y + 0.2, nodo, ha='center', fontsize=12)

        for vecino, peso in vecinos.items():
            x2, y2 = posiciones[vecino]
            ax.plot([x, x2], [y, y2], color='gray', linewidth=1)
            mx, my = (x + x2) / 2, (y + y2) / 2
            ax.text(mx, my, str(peso), fontsize=8, color='gray')

    #ruta mas corta
    if camino:
        for i in range(len(camino) - 1):
            n1, n2 = camino[i], camino[i + 1]
            x1, y1 = posiciones[n1]
            x2, y2 = posiciones[n2]
            ax.plot([x1, x2], [y1, y2], color='red', linewidth=3)

    ax.set_title("Grafo urbano - Ruta más corta")
    plt.axis('off')
    plt.show()

#def para interfaz
def main():
    print("Nodos disponibles:", list(grafo.keys()))
    inicio = input("Nodo de inicio (ej: A): ").strip().upper()
    destino = input("Nodo de destino (ej: F): ").strip().upper()

    if inicio not in grafo or destino not in grafo:
        print("Nodo inválido.")
        return

    camino, costo = dijkstra(grafo, inicio, destino)

    if camino:
        print(f"Ruta más corta: {' -> '.join(camino)}")
        print(f"Costo total: {costo}")
        visualizar_grafo(grafo, posiciones, camino)
    else:
        print("No se encontró una ruta.")

if __name__ == "__main__":
    main()