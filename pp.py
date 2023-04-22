from funciones import existeEstadoEnLista, Estado

def busquedaPP(laberinto: int):
    inicio = Estado(9, 9, 'I', 1, None)
    listaVisitados = []
    listaPendientes = []

    listaPendientes.append(inicio)
    indice = 0
    
    while(listaPendientes and listaPendientes[0].estado != 'F'):
        estadoActual = listaPendientes.pop(0)

        # Se lo agrega a la lista de estados ya visitados
        listaVisitados.append(estadoActual)

        if estadoActual.estado != 'X':
            # Visitar celda arriba
            if estadoActual.y > 0:
                x = estadoActual.x
                y = estadoActual.y - 1
                if not existeEstadoEnLista(listaPendientes, x, y) and not existeEstadoEnLista(listaVisitados, x, y):
                    celda = laberinto[y][x]
                    nuevoEstado = Estado(x, y, celda, estadoActual.nivel + 1, estadoActual)
                    listaPendientes.insert(indice, nuevoEstado)
                    indice = indice + 1
            
            # Visitar celda izquierda
            if estadoActual.x > 0:
                x = estadoActual.x - 1
                y = estadoActual.y
                if not existeEstadoEnLista(listaPendientes, x, y) and not existeEstadoEnLista(listaVisitados, x, y):
                    celda = laberinto[y][x]
                    nuevoEstado = Estado(x, y, celda, estadoActual.nivel + 1, estadoActual)
                    listaPendientes.insert(indice, nuevoEstado)
                    indice = indice + 1

            # Visitar celda abajo
            if estadoActual.y < 9:
                x = estadoActual.x
                y = estadoActual.y + 1
                if not existeEstadoEnLista(listaPendientes, x, y) and not existeEstadoEnLista(listaVisitados, x, y):
                    celda = laberinto[y][x]
                    nuevoEstado = Estado(x, y, celda, estadoActual.nivel + 1, estadoActual)
                    listaPendientes.insert(indice, nuevoEstado)
                    indice = indice + 1

            # Visitar celda derecha
            if estadoActual.x < 9:
                x = estadoActual.x + 1
                y = estadoActual.y
                if not existeEstadoEnLista(listaPendientes, x, y) and not existeEstadoEnLista(listaVisitados, x, y):
                    celda = laberinto[y][x]
                    nuevoEstado = Estado(x, y, celda, estadoActual.nivel + 1, estadoActual)
                    listaPendientes.insert(indice, nuevoEstado)
                    indice = indice + 1
        
        indice = 0
    return listaVisitados, listaPendientes