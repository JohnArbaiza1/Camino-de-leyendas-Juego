class Logica:
    def perder_Vida(self, fichasJugadores, cantidadFichas, jugador, listaJugadores):
        for i in range(cantidadFichas):
            # Hacer una copia independiente de la lista asociada a la clave
            fichas_jugador_i = fichasJugadores[f"ficha{i+1}"][:]
            if fichas_jugador_i[jugador]:
                fichas_jugador_i[jugador] = False
                fichasJugadores[f"ficha{i+1}"] = fichas_jugador_i
                break
            
            next_index = i + 1 + cantidadFichas
            if next_index < 2 * cantidadFichas:
                fichas_jugador_next = fichasJugadores[f"ficha{next_index}"][:]
                if fichas_jugador_next[jugador]:
                    fichas_jugador_next[jugador] = False
                    fichasJugadores[f"ficha{next_index}"] = fichas_jugador_next
                    if not fichas_jugador_i[jugador] and not fichas_jugador_next[jugador]:
                        print(f"El Jugador {jugador + 1} ha perdido las vidas de una ficha")
                    if all(not fichasJugadores[f"ficha{j+1}"][jugador] for j in range(cantidadFichas)):
                        print(f"El jugador {jugador + 1} No tiene mas Fichas")
                        listaJugadores[jugador] = False
                    break