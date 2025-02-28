Ejercicio 1
  Agente_de_Patinaje
    
    ruta = [(x, 0) for x in range(10)] + [(9, y) for y in range(1, 10)] + [(x, 9) for x in range(8, -1, -1)] + [(0, y) for y in range(8, 0, -1)]
   
      Aquí definimos una lista de coordenadas (x, y) que representan el camino que seguirá el agente.
      Un camino horizontal de izquierda a derecha en la fila y = 0.
      Un camino vertical hacia abajo en la columna x = 9.
      Un camino horizontal de derecha a izquierda en la fila y = 9.
      Un camino vertical hacia arriba en la columna x = 0

    obstaculos = {(5, 0), (7, 7), (3, 9)}
      Los obstáculos son posiciones fijas en la ruta, definidos como un conjunto {}.
      Si el agente llega a una de estas posiciones, debe cambiar de dirección.
    
    posicion_actual = ruta[0]
        indice = 0

En este ejercicio utilizaremos dos funciones la de detectar obstaculos que ira verificando y la de cambiar direccion que como su nombre lo dice ir[a cambiando la direccion de forma aleatoriamente saltando en posiciones aleatorias en la ruta

Odef detectar_obstaculo(posicion):
    """Verifica si la posición tiene un obstáculo."""
    return posicion in obstaculos
Por ultimo tenemos un Bucle principal que hace que el agente se mueva. tiene un tiempo el cual hace que cada movimiento tarde medio segundo y luego verifica si hay un obstaculo y determina si hay el agente cambia de direccion, si detecta que no hay obstaculo sigue patrullando.


Ejercicio 2:
  Agente_Explorador_de_Mapa

las variables N, M = 5 , 5 son para crear una matriz de 5*5
se determinan las posibles direcciones, en tal caso arriba, abajo, izquierda, derecha.

luego en la siguiente parte se verifica la posicion actual del agente el cual empieza en una posicion aleatoria dentro del mapa.

la funcion obtener_movimientos_cvalidos (posicion): calcula los movimientos dentro de los limites del mapa y evita posiciones ya visitadas.

dentro de nuestro bucle principal, valida que haya movimientos disponibles; selecciona un movimiento aleatorio y actualiza la posicion en la que se encuentra el agente y guarda la nueva posicion visitada.


Ejercicio 3

Agente_De_Naavegacion_autonoma


Se le implementa el algoritmo ya realizado de BFS para encontrar la ruta mas corta, usa una sola cola para explorar los cambio y guarda las posiciones ya exploradas en visitado


el agente puede moverse arriba, abajo, izquierda, derecha y evita parees y posiciones ya visitadas.



Ejercicio 4 

Agente_De_seleccion_de_rutas
  Una Matriz donde cada celda tiene un valor de recompensa, tanto positivo, como negativo 

  el agente va evaluando diferentes caminos desde un punto de inicio, tambien utilizamos un BFS para explorar todas las rutas posibles.

  el programa guarda la ruta que maximiza la recompensa total, y luego imprime el mejor camino y su recompensa acumulada
  



