import random
import time

# Definimos el entorno con una ruta de patrullaje
ruta = [(x, 0) for x in range(10)] + [(9, y) for y in range(1, 10)] + [(x, 9) for x in range(8, -1, -1)] + [(0, y) for y in range(8, 0, -1)]

# Simulación de obstáculos
obstaculos = {(5, 0), (7, 7), (3, 9)}

# Posición inicial del agente
posicion_actual = ruta[0]
indice = 0

def detectar_obstaculo(posicion):
    """Verifica si la posición tiene un obstáculo."""
    return posicion in obstaculos

def cambiar_direccion():
    """Cambia la dirección aleatoriamente saltando a una posición aleatoria en la ruta."""
    return random.choice(ruta)

# Simulación del patrullaje
en_marcha = True
while en_marcha:
    time.sleep(0.5)  # Simula el tiempo de movimiento del agente
    
    # Verifica si hay un obstáculo en la posición actual
    if detectar_obstaculo(posicion_actual):
        print(f"Obstáculo detectado en {posicion_actual}, cambiando dirección...")
        posicion_actual = cambiar_direccion()
    else:
        print(f"Agente en posición: {posicion_actual}")
        indice = (indice + 1) % len(ruta)
        posicion_actual = ruta[indice]