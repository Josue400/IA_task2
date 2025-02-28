from collections import deque

def mejor_ruta(recompensas, inicio):
    filas, columnas = len(recompensas), len(recompensas[0])
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, Abajo, Izquierda, Derecha
    
    mejor_camino = []
    mejor_valor = float('-inf')
    
    # Cola para BFS con acumulación de recompensa
    cola = deque([(inicio, [inicio], recompensas[inicio[0]][inicio[1]])])
    
    while cola:
        (x, y), ruta, valor = cola.popleft()
        
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_camino = ruta
        
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas and (nx, ny) not in ruta:
                nueva_ruta = ruta + [(nx, ny)]
                nuevo_valor = valor + recompensas[nx][ny]
                cola.append(((nx, ny), nueva_ruta, nuevo_valor))
    
    return mejor_camino, mejor_valor

# Definir la matriz de recompensas
recompensas = [
    [5, 3, -1, 2, 4],
    [1, 7, -2, 3, 2],
    [4, 6, 5, 1, 0],
    [2, -1, 3, 4, 6],
    [0, 2, 8, -3, 7]
]

inicio = (0, 0)  # Posición inicial

ruta_optima, max_valor = mejor_ruta(recompensas, inicio)
print("Mejor ruta:", ruta_optima)
print("Valor total de recompensa:", max_valor)
