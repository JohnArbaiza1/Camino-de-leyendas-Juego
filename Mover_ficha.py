#En este archivo se trabaja la logica de movimiento de lafichas en el tablero

from colorama import init, Fore 
init()

#Definimos un conjunto de listas que empleamos para almacenar valores 
casillas_seguras = [9,16,27,33,43]
casillas_penalizacion = [5,17,25,31,45]
tunel_Seguridad = [46,47,48,49,50]

#Definimos la funcion que se encargara del desplazamiento de las fichas en el tablero de juego
def mover_fichas(posicion_jugador,paso1):
    posicion_jugador += paso1
    if posicion_jugador in casillas_seguras:
        print(Fore.LIGHTGREEN_EX +"Caíste en tierra protegida: Tienes mucha suerte." + Fore.RESET)
    elif posicion_jugador in casillas_penalizacion:
        print(Fore.LIGHTMAGENTA_EX + "Un mago usa un hechizo contra ti: ahora retrocedes dos casillas " + Fore.RESET)
        posicion_jugador -= 2
    elif posicion_jugador in tunel_Seguridad:
        print(Fore.LIGHTGREEN_EX + "Has llegado al bosque sagrado: Estás en túnel de seguridad"+ Fore.RESET)
        if posicion_jugador == casillas_seguras[4] or posicion_jugador > casillas_seguras[4]:
            print(Fore.LIGHTMAGENTA_EX +"El jugador ha superado la casilla 50. Debe regresar al inicio"+ Fore.RESET)
            posicion_jugador = 0
    elif posicion_jugador == 50: 
        print(Fore.LIGHTGREEN_EX +"Has ganado el juego: Ahora eres una leyenda"+ Fore.RESET)
            
    return posicion_jugador

