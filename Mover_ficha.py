#En este archivo se trabaja la logica de movimiento de lafichas en el tablero
from Vidas import *
fi =  Vidas()
from colorama import init, Fore 
init()

#Definimos un conjunto de listas que empleamos para almacenar valores 
casillas_seguras = [9,16,27,33,43]
casillas_penalizacion = [5,17,25,31,45]
tunel_Seguridad = [46,47,48,49]

#Definimos la funcion que se encargara del desplazamiento de las fichas en el tablero de juego
def mover_fichas(posicion_jugador,paso1,fichas,cantidadFichas, jugador,listaJugadores):
    posicion_jugador += paso1
    if posicion_jugador in casillas_seguras:
        print(Fore.LIGHTGREEN_EX +"Caíste en tierra protegida: Tienes mucha suerte." + Fore.RESET)
    elif posicion_jugador in casillas_penalizacion:
        print(Fore.LIGHTMAGENTA_EX + "Un mago usa un hechizo contra ti: ahora retrocedes dos casillas " + Fore.RESET)
        posicion_jugador -= 2
    elif posicion_jugador in tunel_Seguridad:
        print(Fore.LIGHTGREEN_EX + "Has llegado al bosque sagrado: Estás en túnel de seguridad"+ Fore.RESET)
    elif posicion_jugador >= 50:
        print(Fore.LIGHTGREEN_EX +"Caiste en el abismo:Pierdes una ficha"+ Fore.RESET)
        posicion_jugador = 0
        fichasRestantes = 0
        for i in range(cantidadFichas):
            # Hacer una copia independiente de la lista asociada a la clave
            fichas_jugador_i = fichas[f"ficha{i+1}"][:]
            if fichas_jugador_i[jugador]:
                fichas_jugador_i[jugador] = False
                fichas[f"ficha{i+1}"] = fichas_jugador_i
                print("Has perdido una ficha")
                break
            
            next_index = i + 1
            if next_index < cantidadFichas:
                fichas_jugador_next = fichas[f"ficha{next_index}"][:]
                if fichas_jugador_next[jugador]:
                    fichas_jugador_next[jugador] = False
                    fichas[f"ficha{next_index}"] = fichas_jugador_next
                    if not fichas_jugador_i[jugador] and not fichas_jugador_next[jugador]:
                       # print(f"El Jugador {jugador + 1} ha perdido las vidas de una ficha")
                        print(f"El jugador {jugador + 1} No tiene mas Fichas")
                        #listaJugadores[jugador] = False
                    break

        for j in range(cantidadFichas):
            if fichas[f"ficha{j+1}"][jugador]:
                fichasRestantes+=1
        print(f"Te quedan {fichasRestantes} fichas")

        if fichasRestantes == 0:
            listaJugadores[jugador] = False
            print(f"Jugador {jugador+1} ha perdido")
    elif posicion_jugador == 49: 
        print(Fore.LIGHTGREEN_EX +"Has ganado el juego: Ahora eres una leyenda"+ Fore.RESET)
            
    return posicion_jugador