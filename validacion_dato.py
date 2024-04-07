def validar():
    bandera = True
    while bandera:
        jugadores = input('\t Cuantos novatos jugaran: ')

        if len(jugadores) == 0:
            print('\t Error. Ingrese una cantidad numerica.')
        elif jugadores.isdigit() == False:
            print('\t Error. Debe ser una cantidad numerica.')
        elif int(jugadores) == 2 or int(jugadores) == 3 or int(jugadores) == 4:
            bandera = False
            return int(jugadores)
        else:
            print('\t Error. Debe ser un numero en el rango del 2 al 4.')