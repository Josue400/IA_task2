import random
import time

# Dimensiones del mapa
N, M = 5, 5  # Matriz de 5x5

# Movimientos posibles (arriba, abajo, izquierda, derecha)
direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Posición inicial del agente (aleatoria)
posicion_actual = (random.randint(0, N-1), random.randint(0, M-1))

# Almacenar posiciones visitadas
visitadas = set()
visitadas.add(posicion_actual)

def obtener_movimientos_validos(posicion):
    """Retorna una lista de movimientos posibles que aún no han sido visitados."""
    x, y = posicion
    movimientos = []
    for dx, dy in direcciones:
        nueva_pos = (x + dx, y + dy)
        if 0 <= nueva_pos[0] < N and 0 <= nueva_pos[1] < M and nueva_pos not in visitadas:
            movimientos.append(nueva_pos)
    return movimientos

# Bucle de exploración
en_marcha = True
while en_marcha:
    time.sleep(0.5)  # Simula el tiempo de movimiento del agente
    
    movimientos = obtener_movimientos_validos(posicion_actual)
    if movimientos:
        nueva_pos = random.choice(movimientos)
        visitadas.add(nueva_pos)
        posicion_actual = nueva_pos
        print(f"Agente se movió a {posicion_actual}")
    else:
        print("No hay más movimientos posibles. Exploración finalizada.")
        en_marcha = False
