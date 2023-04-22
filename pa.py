from funciones import crearNodo, existeNodo
from anytree import Node

def hijoNodoactual(laberinto: int, y: int, x: int, nodoActual: Node, arbolPA: Node, nodosPorRecorrer):
    #Realiza todos los pasos de agregar un nodo al árbol y a la lista cuando se busca en las cuatro direcciones
    nivel = nodoActual.level + 1
    celda = laberinto[y][x]
    if (celda == '0' or celda == 'I') and existeNodo(arbolPA, x, y):
        celda = 'B'
    nuevoNodo = crearNodo(x, y, celda, nivel)
    nuevoNodo.parent = nodoActual
    nodosPorRecorrer.append(nuevoNodo)

def recorrerLabPA(arbolPA: Node, laberinto: int):
    #Permite recorrer el laberinto mediante la técnica de primero en amplitud
    termino = False
    x = 0
    y = 0
    nodosPorRecorrer = []
    nodosPorRecorrer.append(arbolPA)
    for nodoActual in nodosPorRecorrer:
        if nodoActual.est == 'F':
            termino = True
            break
        if nodoActual.est == '0' or nodoActual.est == 'I':
            if nodoActual.cordY > 0:    # Recorrer arriba
                x = nodoActual.cordX
                y = nodoActual.cordY - 1
                hijoNodoactual(laberinto, y, x, nodoActual, arbolPA, nodosPorRecorrer)
            if nodoActual.cordX > 0:    # Recorrer izquierda
                x = nodoActual.cordX - 1
                y = nodoActual.cordY
                hijoNodoactual(laberinto, y, x, nodoActual, arbolPA, nodosPorRecorrer)
            if nodoActual.cordY < 9:    # Recorrer abajo
                x = nodoActual.cordX
                y = nodoActual.cordY + 1
                hijoNodoactual(laberinto, y, x, nodoActual, arbolPA, nodosPorRecorrer)
            if nodoActual.cordX < 9:    # Recorrer derecha
                x = nodoActual.cordX + 1
                y = nodoActual.cordY
                hijoNodoactual(laberinto, y, x, nodoActual, arbolPA, nodosPorRecorrer)
    return termino