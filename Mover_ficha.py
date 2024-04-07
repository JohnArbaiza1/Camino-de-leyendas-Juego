#En este archivo se trabaja la logica de movimiento de lafichas en el tablero

#Definimos un conjunto de listas que empleamos para almacenar valores 
casillas_seguras = [9,16,27,33,43]
casillas_penalizacion = [5,17,25,31,45]

#Definimos la funcion que se encargara del desplazamiento de las fichas en el tablero de juego
def mover_fichas(posicion_jugador,paso1):
    posicion_jugador += paso1
    if posicion_jugador in casillas_seguras:
        print("Caíste en tierra protegida: Tienes mucha suerte.")
    elif posicion_jugador in casillas_penalizacion:
        print("Un mago usa un hechizo contra ti: ahora retroceder dos casillas ")
        posicion_jugador -= 2
    elif posicion_jugador == 50: 
        print("Has ganado el juego: Ahora eres una leyenda")
    elif posicion_jugador >= 50:
        print("El jugador ha superado la casilla 50. Debe regresar al inicio")
        posicion_jugador = 0
    return posicion_jugador

