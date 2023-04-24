from funciones import Estado, hijoNodoActual
from collections import deque

def recorrerLabPA(laberinto: int):
    filas = len(laberinto) - 1
    columnas = len(laberinto[0]) - 1
    #Permite recorrer el laberinto mediante la técnica de primero en amplitud
    inicio = Estado(columnas, filas, 'I', 1, None)
    x = 0
    y = 0
    listaVisitados = []
    listaPendientes = deque()
    listaPendientes.append(inicio)

    while(listaPendientes and listaPendientes[0].estado != 'F'):
        estadoActual = listaPendientes.popleft()
        if estadoActual.estado == '0' or estadoActual.estado == 'I':
            if estadoActual.y > 0:    # Recorrer arriba
                x = estadoActual.x
                y = estadoActual.y - 1
                nuevoEstado = hijoNodoActual(laberinto, y, x, estadoActual, listaPendientes, listaVisitados)
                if(nuevoEstado is not None):
                    listaPendientes.append(nuevoEstado)
            if estadoActual.x > 0:    # Recorrer izquierda
                x = estadoActual.x - 1
                y = estadoActual.y
                nuevoEstado = hijoNodoActual(laberinto, y, x, estadoActual, listaPendientes, listaVisitados)
                if(nuevoEstado is not None):
                    listaPendientes.append(nuevoEstado)
            if estadoActual.y < filas:    # Recorrer abajo
                x = estadoActual.x
                y = estadoActual.y + 1
                nuevoEstado = hijoNodoActual(laberinto, y, x, estadoActual, listaPendientes, listaVisitados)
                if(nuevoEstado is not None):
                    listaPendientes.append(nuevoEstado)
            if estadoActual.x < columnas:    # Recorrer derecha
                x = estadoActual.x + 1
                y = estadoActual.y
                nuevoEstado = hijoNodoActual(laberinto, y, x, estadoActual, listaPendientes, listaVisitados)
                if(nuevoEstado is not None):
                    listaPendientes.append(nuevoEstado)
        listaVisitados.append(estadoActual)
    return listaVisitados, listaPendientes