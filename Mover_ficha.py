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
def mover_fichas(posicion_jugador,paso1,fichas,cantidadFichas, jugador,listaJugadores,jugadores):
    posicion_jugador += paso1
    if posicion_jugador in casillas_seguras:
        print(Fore.LIGHTGREEN_EX +"-"*60,"\nCaíste en tierra protegida: Tienes mucha suerte.(▀̿Ĺ̯▀̿ ̿) \n","-"*60 + Fore.RESET)
    elif posicion_jugador in casillas_penalizacion:
        print(Fore.LIGHTMAGENTA_EX +"-"*70, "\nUn mago usa un hechizo contra ti: ahora retrocedes dos casillas (⊙_⊙;) \n","-"*70 + Fore.RESET)
        posicion_jugador -= 2
    elif posicion_jugador in tunel_Seguridad:
        if posicion_jugador == 49: 
            print(Fore.LIGHTGREEN_EX +"\n","-"*70)
            print(f"       FELICIDADES JUGADOR {jugador+1} LO HAS LOGRADO")
            print(Fore.LIGHTGREEN_EX +"-"*70,"\nHas ganado el juego: Ahora eres una leyenda (⌐■_■)\n","-"*70 + Fore.RESET)
            exit()
        else:
            print(Fore.LIGHTGREEN_EX +"-"*70, "\nHas llegado al bosque sagrado: Estás en túnel de seguridad ヾ(⌐■_■)ノ♪\n","-"*70 + Fore.RESET)
    elif posicion_jugador >= 50:
        print(Fore.LIGHTMAGENTA_EX +"-"*50,"\nCaíste en el abismo de las serpientes (X_X) \n","-"*50 + Fore.RESET)
        posicion_jugador = 0
        fichasRestantes = 0
        for i in range(cantidadFichas):
            # Hacer una copia independiente de la lista asociada a la clave
            fichas_jugador_i = fichas[f"ficha{i+1}"][:]
            if fichas_jugador_i[jugador]:
                fichas_jugador_i[jugador] = False
                fichas[f"ficha{i+1}"] = fichas_jugador_i
                print("\nHas perdido una ficha (ㆆ_ㆆ)")
                break

        for j in range(cantidadFichas):
            if fichas[f"ficha{j+1}"][jugador]:
                fichasRestantes+=1
        print(f"Te quedan {fichasRestantes} fichas")

        if fichasRestantes == 0:
            listaJugadores[jugador] = False
            print(f"Jugador {jugador+1} ha perdido ಥ_ಥ")
        
        #Definimos una lista vacia
        list_novatos = []
        #Definimos un for para llenar la lista con el numero de jugadores de la partida
        for i in range(jugadores):
            list_novatos.append(i+1) 
        #Transformamos las listas de nuestro jugadores a un diccionario
        dic_jugadores = dict(zip(list_novatos,listaJugadores))
        
        #Verificamos que solo quede un jugador con fichaz
        jugadores_activos = sum(1 for estado in dic_jugadores.values() if estado)
        if jugadores_activos == 1:
            #Obtenemos el indice de la lista del jugador que gano para mostrarlo
            ganador = listaJugadores.index(True)
            print(Fore.LIGHTGREEN_EX +"\n","-"*70)
            print(f"       FELICIDADES JUGADOR {ganador+1} LO HAS LOGRADO")
            #De ser asi mostramos el siguiente mensaje y salimos de la ejecucion
            print("Has ganado el juego: Ahora eres una leyenda (⌐■_■)\n","-"*70 + Fore.RESET)
            exit()
    
    return posicion_jugador