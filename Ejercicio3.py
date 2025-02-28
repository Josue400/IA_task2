from collections import deque

def encontrar_ruta(laberinto, inicio, meta):
    filas, columnas = len(laberinto), len(laberinto[0])
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, Abajo, Izquierda, Derecha
    
    # Cola para BFS
    cola = deque([(inicio, [inicio])])
    visitado = set()
    visitado.add(inicio)
    
    while cola:
        (x, y), ruta = cola.popleft()
        
        if (x, y) == meta:
            return ruta  # Retorna la ruta más corta encontrada
        
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas and laberinto[nx][ny] != 1 and (nx, ny) not in visitado:
                cola.append(((nx, ny), ruta + [(nx, ny)]))
                visitado.add((nx, ny))
    
    return None  # No se encontró ruta

# Definir el laberinto (0: libre, 1: pared)
laberinto = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0]
]

inicio = (0, 0)  # Posición inicial (S)
meta = (0, 4)   # Posición de la meta (M)

ruta = encontrar_ruta(laberinto, inicio, meta)
if ruta:
    print("Ruta encontrada:", ruta)
else:
    print("No hay ruta disponible.")
    