from colorama import init, Fore 
init()

def validar():
    bandera = True
    while bandera:
        jugadores = input('\nCuantos novatos jugaran: ')

        if len(jugadores) == 0:
            print(Fore.LIGHTMAGENTA_EX +'Error. Ingrese una cantidad numerica.\n'+ Fore.RESET)
        elif jugadores.isdigit() == False:
            print(Fore.LIGHTMAGENTA_EX +'Error. Debe ser una cantidad numerica.\n'+ Fore.RESET)
        elif int(jugadores) == 2 or int(jugadores) == 3 or int(jugadores) == 4:
            bandera = False
            return int(jugadores)
        else:
            print(Fore.LIGHTMAGENTA_EX +'Error. Debe ser un numero en el rango del 2 al 4.\n'+ Fore.RESET)