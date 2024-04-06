#Importamos los modulos a emplear
import time #Para hacer unas pequeñas animaciones
import random
#-------------------------------------------------------------------------------------
#Definimos una lista que contenga el mensaje a mostrar
mensajes = ["    BIENVENIDO","        AL ","CAMINO DE LEYENDAS"]
#Establecemos las posiciones de los jugadores
posicion_jugador = [0,0]
#Varaibles a emplear para dibujar el tablero
filas_tablero = 2
columnas_tablero = 25
#Variables de juego
jugar = True
jugadores = 0
#-------------------------------------------------------------------------------------
                     #Parte donde se encuentran las funciones 
#-------------------------------------------------------------------------------------
#Funcion encargada del mensaje de bienvenida
def bienvenida_animada(mensaje):
    print("\n\t","*"*36, end="\n")
    time.sleep(0.9) #El mensaje se muestra despues de 0.9 seg
    #Empleamos un for que recorra la lista
    for palabras in mensajes:
        #Imprimimos el mensaje
        print("\033[31;33m"+"\t\t",palabras, end='' + "\033[0;m" , flush=True )
        #Mostramos el mensaje con un tiempo de espera de 0.6 seg entre cada palabra.
        time.sleep(0.6)
        print()
    time.sleep(0.6)
    print("\t","*"*36, end="\n")

#Funcion encargada de dibujar el tablero
def tablero(posicion_jugador,filas,columnas):
    #Mostramos la posicion del jugador
    camino = [' # '] * (filas * columnas)
    for i, posicion in enumerate(posicion_jugador):
        camino[posicion] = str(i + 1)
    print("=" * (columnas * 3)) #Fila superior del tablero
    for i in range(filas):
        print(''.join(camino[i * columnas : (i + 1) * columnas])) #Casillas del tablero
    print("=" * (columnas * 3)) #Linea inferior del tablero
#-------------------------------------------------------------------------------------
#Llamamos a la funcion del mensaje de inicio
bienvenida_animada(mensaje=mensajes)
time.sleep(0.6)
#Preguntamos el numero de jugadores
jugadores = int(input("\t Cuantos novatos jugaran:"))
#Definimos un while que nos ayude con el control del juego
while jugar:
    for jugador in range(jugadores):
        input(f"\nEs turno del jugador {jugador + 1}. Presione Enter para lanzar los dados")

    #Llamamos a las funcion de dibujar tablero
    time.sleep(0.6)
    tablero(posicion_jugador,filas=filas_tablero, columnas=columnas_tablero)

        