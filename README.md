# Parcial matemáticas discretas

Edward Jampiere Patiño Guerrero

Algoritmo de Dijkstra para encontrar la ruta más corta en un grafo.

Funcionamiento general:
El grafo se representa como un diccionario, donde cada nodo tiene vecinos con pesos.
Se usa una cola de prioridad para ir siempre por el nodo con menor costo en total.
Se calcula la distancia más corta desde un nodo de inicio hasta un nodo destino.
Se reconstruye y muestra la ruta óptima y su costo total.
Se visualiza el grafo con la libreria matplotlib, incluyendo la ruta más corta.
Estructura de el grafo:  
los nodos puntos como 'A', 'B', 'C' etc. que representan ubicaciones.
las aristas simples conexiones entre nodos.
Ejemplo de el fromato del grafo:

# 'A': {'B': 2, 'C': 4}

Esto significa que desde el nodo 'A' tiene una conexión a 'B' con un peso de 2 y a 'C' con un peso de 4.
Qué hace el usuario:
Ingresa el nodo de inicio y el nodo de destino.
El programa muestra por consola la ruta más corta y su costo total.
Luego se genera un gráfico del grafo.
