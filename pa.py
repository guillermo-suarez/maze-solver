from funciones import existeEstadoEnLista, Estado
from collections import deque

def hijoNodoactual(laberinto: int, y: int, x: int, estadoActual: Estado, listaPendientes, listaVisitados):
    #Realiza todos los pasos de agregar a la lista cuando se busca en las cuatro direcciones
    if not existeEstadoEnLista(listaPendientes, x, y) and not existeEstadoEnLista(listaVisitados, x, y):
        celda = laberinto[y][x]
        nuevoEstado = Estado(x, y, celda, estadoActual.nivel + 1, estadoActual)
        listaPendientes.append(nuevoEstado)

def recorrerLabPA(laberinto: int):
    #Permite recorrer el laberinto mediante la técnica de primero en amplitud
    inicio = Estado(9, 9, 'I', 1, None)
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
                hijoNodoactual(laberinto, y, x, estadoActual, listaPendientes, listaVisitados)
            if estadoActual.x > 0:    # Recorrer izquierda
                x = estadoActual.x - 1
                y = estadoActual.y
                hijoNodoactual(laberinto, y, x, estadoActual, listaPendientes, listaVisitados)
            if estadoActual.y < 9:    # Recorrer abajo
                x = estadoActual.x
                y = estadoActual.y + 1
                hijoNodoactual(laberinto, y, x, estadoActual, listaPendientes, listaVisitados)
            if estadoActual.x < 9:    # Recorrer derecha
                x = estadoActual.x + 1
                y = estadoActual.y
                hijoNodoactual(laberinto, y, x, estadoActual, listaPendientes, listaVisitados)
        listaVisitados.append(estadoActual)
    return listaVisitados, listaPendientes