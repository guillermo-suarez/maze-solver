from funciones import Estado, hijoNodoActual, removerRepetidos
from collections import deque

def recorrerLabPP(laberinto: int):
    filas = len(laberinto) - 1
    columnas = len(laberinto[0]) - 1
    inicio = Estado(columnas, filas, 'I', 1, None)
    listaVisitados = []
    listaPendientes = []

    listaPendientes.append(inicio)
    indice = 0

    cont = 0
    
    while(listaPendientes and listaPendientes[0].estado != 'F'):
        estadoActual = listaPendientes.pop(0)
        if estadoActual.estado != 'X':
            if estadoActual.y > 0:
                x = estadoActual.x
                y = estadoActual.y - 1
                nuevoEstado = hijoNodoActual(laberinto, y, x, estadoActual, listaPendientes, listaVisitados)
                if(nuevoEstado is not None):
                    listaPendientes.insert(indice, nuevoEstado)
                    indice = indice + 1
            if estadoActual.x > 0:
                x = estadoActual.x - 1
                y = estadoActual.y
                nuevoEstado = hijoNodoActual(laberinto, y, x, estadoActual, listaPendientes, listaVisitados)
                if(nuevoEstado is not None):
                    listaPendientes.insert(indice, nuevoEstado)
                    indice = indice + 1
            if estadoActual.y < filas:
                x = estadoActual.x
                y = estadoActual.y + 1
                nuevoEstado = hijoNodoActual(laberinto, y, x, estadoActual, listaPendientes, listaVisitados)
                if(nuevoEstado is not None):
                    listaPendientes.insert(indice, nuevoEstado)
                    indice = indice + 1
            if estadoActual.x < columnas:
                x = estadoActual.x + 1
                y = estadoActual.y
                nuevoEstado = hijoNodoActual(laberinto, y, x, estadoActual, listaPendientes, listaVisitados)
                if(nuevoEstado is not None):
                    listaPendientes.insert(indice, nuevoEstado)
                    indice = indice + 1
        indice = 0
        listaPendientes = removerRepetidos(listaPendientes)
        listaVisitados.append(estadoActual)

    if listaPendientes[0].estado == 'F':
        listaVisitados.append(listaPendientes.pop(0))
    
    return listaVisitados, listaPendientes