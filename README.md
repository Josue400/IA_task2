Ejercicio 1
  Agente_de_Patinaje
    
    ruta = [(x, 0) for x in range(10)] + [(9, y) for y in range(1, 10)] + [(x, 9) for x in range(8, -1, -1)] + [(0, y) for y in range(8, 0, -1)]
   
    Aquí definimos una lista de coordenadas (x, y) que representan el camino que seguirá el agente.
      Un camino horizontal de izquierda a derecha en la fila y = 0.
      Un camino vertical hacia abajo en la columna x = 9.
      Un camino horizontal de derecha a izquierda en la fila y = 9.
      Un camino vertical hacia arriba en la columna x = 0
