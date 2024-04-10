class Vidas:
    #funcion para determinar la cantidad de fichas
    def cantidadfichas(self, jugadores):
        numero = 0
        if jugadores >= 2 and jugadores <= 3:
            numero = 3
        elif jugadores ==4:
            numero = 2
        return numero
    
    #-------------------------------------------------------------------------------------
    #funcion para generar la cantidad de vidas
    def vidas(self, jugadores, numeroFichas):
        vidasFichas = {}#diccionario que contendra el estado de cada vida
        fichas = []#lista para almacenar el estado individual de una ficha
        for i in range(jugadores):
            fichas.append(True)#inicializamos en verdadero todas las fichas
        for i in range(numeroFichas):
            vidasFichas[f"ficha{i+1}"] = fichas
        return vidasFichas