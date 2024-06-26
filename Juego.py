#Importamos los modulos a emplear
import time #Para hacer unas pequeñas animaciones
import random
from colorama import init, Fore #Para poder dar color a los mensajes en consola
init()
#Llamamos a las demas clases
from Mover_ficha import *
from Vidas import Vidas
from validacion_dato import validar

#-------------------------------------------------------------------------------------
#Definimos una lista que contenga el mensaje a mostrar
mensajes = ["    BIENVENIDO","        AL ","CAMINO DE LEYENDAS"]
#Variables para colores de mensaje
red = Fore.RED+"^"+Fore.RESET
amarillo = Fore.YELLOW + "*" + Fore.RESET
#Definimos una lista vacia que almacene las posiciones de los jugadores
posicion_jugador = []
#lista para controlar los jugadores que siguen en juego
jugadoresActivos = []
#Varaibles a emplear para dibujar el tablero
filas_tablero = 2
columnas_tablero = 25
#Variables de juego
jugar = True
jugadores = 0
#-------------------------------------------------------------------------------------
                     #Objetos de clases 
#-------------------------------------------------------------------------------------
objeto_vida = Vidas()

#-------------------------------------------------------------------------------------
                     #Parte donde se encuentran las funciones 
#-------------------------------------------------------------------------------------

#Funcion encargada del mensaje de bienvenida
def bienvenida_animada(mensaje):
    print("*"*64, end="\n")
    time.sleep(0.9) #El mensaje se muestra despues de 0.9 seg
    #Empleamos un for que recorra la lista
    for palabras in mensaje:
        #Imprimimos el mensaje
        print(Fore.YELLOW+" "*22,palabras, end='' + Fore.RESET , flush=True )
        #Mostramos el mensaje con un tiempo de espera de 0.6 seg entre cada palabra.
        time.sleep(0.6)
        print()
        
    print()
    print(Fore.CYAN+" "*30,red)
    time.sleep(0.5)
    print(" "*29,f"{red}{amarillo}{red}")
    time.sleep(0.5)
    print(" "*29,f"{red}{amarillo}{red}\n"," "*28,f"{red}{amarillo}{red}\n"," "*28,f"{red}{amarillo}{red}\n"," "*25,f"\033[91m{'<<<<'}\033[0m{amarillo}\033[91m{'>>>>'}\033[0m")
    time.sleep(0.5)
    print(" "*30,f"{amarillo}\n"," "*29,f"{amarillo}\n"," "*29,f"\033[91m{'V'}\033[0m")

    time.sleep(0.6)
    print("*"*64, end="\n")
    time.sleep(0.8)
    print(Fore.YELLOW + "El juego consiste en atravesar un camino lleno de peligros ")
    print("y recompensas donde el primer jugador que lleve una de N fichas")
    print("sagradas gana el derecho de ser una leyenda y te animas a jugar."+Fore.RESET)
    print("*"*64, end="\n")
    time.sleep(1)

#Funcion encargada del lanzamiento de los dados.
def lanzar_dados():
    #Definimos las variables que almacenara el valor del lazamiento de los dados
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)

    return dado1, dado2

#Funcion encargada de dibujar el tablero de juego
def tablero(posicion_jugador, filas, columnas):
    #Definimos una matriz vacia que contenga nuestro tablero
    camino = [ ['[ ]'] * columnas for _ in range(filas) ] #El guion _ que vemos en el for es para indicar que no es necesario el valor de la variable de iteración en el bucle. 
    #Asignamos la posicion del jugador
    for i, posicion in enumerate(posicion_jugador):
        #convierte la posición del jugador en coordenadas de fila y columna en la matriz
        fila, columna = divmod(posicion, columnas)
        #actualiza la matriz camino para reflejar la posición de cada jugador en el tablero
        camino[fila][columna] = (Fore.YELLOW + f"[{i + 1}]" + Fore.RESET)
    print("=" * (columnas * 3)) #Fila superior del tablero
    for fila in camino:
        print(''.join(fila))
    print("=" * (columnas * 3)) #Linea inferior del tablero
#-------------------------------------------------------------------------------------

#Llamamos a la funcion del mensaje de inicio
bienvenida_animada(mensaje=mensajes)
time.sleep(0.6)
#Preguntamos el numero de jugadores
jugadores = validar()

# casillas de ejemplo
casillas_tiro_doble = [20,35,44]

#-------------------------------------------------------------------------------------
#llenado de elementos de la lista posicion y jugadores Activos
for i in range(jugadores):
    posicion_jugador.append(0)
    jugadoresActivos.append(True)
#-------------------------------------------------------------------------------------
#generamos las fichas
fichas = objeto_vida.cantidadfichas(jugadores)

#generamos el diccionario con el estado de cada ficha para cada jugador
fichasJugadores = objeto_vida.vidas(jugadores, fichas)

#Definimos un while que nos ayude con el control del juego
while jugar:
    for jugador in range(jugadores):
        if jugadoresActivos[jugador]:#para determinar si el jugador aun tiene fichas con vidas
            input(f"\nEs turno del jugador {jugador + 1}. Presione Enter para lanzar los dados")
            #llamamos a la funcion lanzar_dado y obtenemos el resultado del lanzamiento
            dado1, dado2 = lanzar_dados()
            #Verificamos si se obtuvo un par de numeros iguales
            if dado1 == dado2:
                print(f"\nEl jugador {jugador + 1}, Lanzo: ({dado1},{dado2})")
                print(Fore.YELLOW+"Adelante futura leyenda \n"+ Fore.RESET)
                posicion_jugador[jugador] = mover_fichas(posicion_jugador[jugador],dado1,fichasJugadores,fichas,jugador,jugadoresActivos,jugadores)

                tiro_doble_consecutivo = 0
                while posicion_jugador[jugador] in casillas_tiro_doble:
                    dado1, dado2 = lanzar_dados()
                    if dado1 == dado2:
                        print(f"Tienes tiro doble. Cantidad: {tiro_doble_consecutivo + 1}")
                        input(f"Es turno del jugador {jugador + 1}. Presione Enter para lanzar los dados")
                        print(f"\nEl jugador {jugador + 1}, Lanzo: ({dado1},{dado2})")
                        print(Fore.YELLOW+"Adelante futura leyenda \n"+ Fore.RESET)
                        posicion_jugador[jugador] = mover_fichas(posicion_jugador[jugador],dado1,fichasJugadores,fichas,jugador,jugadoresActivos,jugadores)
                        tiro_doble_consecutivo += 1
                        if tiro_doble_consecutivo == 3:
                            print(f"Jugador {jugador + 1} Vuelve al inicio")
                            posicion_jugador[jugador] = 0
                            tiro_doble_consecutivo = 0

                print(f"Posicion actual del jugador {jugador + 1}: {posicion_jugador[jugador]}")
                #validamos si un jugador cae en la misma casilla que otro jugador
                for indice, elemento in enumerate(posicion_jugador):
                    if indice != jugador and elemento == posicion_jugador[jugador] and not(elemento in casillas_seguras):
                        if posicion_jugador[jugador] != 0 :
                            posicion_jugador[jugador] += 10
                            if posicion_jugador[jugador] > 49:
                                print(f"Jugador {jugador + 1} Permanece en la misma casilla.")
                                posicion_jugador[jugador] -= 10
                            else:
                                print(f"Jugador {jugador + 1} avanza 10 casillas adicionales.")
                            if posicion_jugador[indice] in tunel_Seguridad:
                                print(f"Jugador {indice + 1} Estas a Salvo")
                            else:
                                print(f"Jugador {indice + 1} retrocedes 3 casillas")
                                posicion_jugador[indice] -= 3
                            if posicion_jugador[indice] < 0:
                                posicion_jugador[indice] = 0
                            break
                #Llamamos a las funcion de dibujar tablero
                time.sleep(0.6)
                tablero(posicion_jugador,filas=filas_tablero, columnas=columnas_tablero)
            else:
                print(f"\nEl jugador {jugador + 1}, Lanzo: ({dado1},{dado2})")
                print(Fore.LIGHTMAGENTA_EX+"¡Hoy no es tu día de suerte!"+ Fore.RESET)        