from funciones import crearNodo, existeNodo
from anytree import Node

def recorrerLabPP(arbolPP: Node, nodoActual: Node, laberinto: int):
    termino = False
    
    if not termino:
        # Recorrer arriba
        if nodoActual.cordY > 0:
            x = nodoActual.cordX
            y = nodoActual.cordY - 1
            celda = laberinto[y][x]
            nivel = nodoActual.level + 1
            if (celda == '0' or celda == 'I') and existeNodo(arbolPP, x, y):
                celda = 'B'
            nuevoNodo = crearNodo(x, y, celda, nivel)
            nuevoNodo.parent = nodoActual
            if nuevoNodo.est == '0':
                termino = recorrerLabPP(arbolPP, nuevoNodo, laberinto)
            elif nuevoNodo.est == 'F':
                termino = True
    
    if not termino:
        # Recorrer izquierda
        if nodoActual.cordX > 0:
            x = nodoActual.cordX - 1
            y = nodoActual.cordY
            celda = laberinto[y][x]
            nivel = nodoActual.level + 1
            if (celda == '0' or celda == 'I') and existeNodo(arbolPP, x, y):
                celda = 'B'
            nuevoNodo = crearNodo(x, y, celda, nivel)
            nuevoNodo.parent = nodoActual
            if nuevoNodo.est == '0':
                termino = recorrerLabPP(arbolPP, nuevoNodo, laberinto)
            elif nuevoNodo.est == 'F':
                termino = True
    
    if not termino:
        # Recorrer abajo
        if nodoActual.cordY < 9:
            x = nodoActual.cordX
            y = nodoActual.cordY + 1
            celda = laberinto[y][x]
            nivel = nodoActual.level + 1
            if (celda == '0' or celda == 'I') and existeNodo(arbolPP, x, y):
                celda = 'B'
            nuevoNodo = crearNodo(x, y, celda, nivel)
            nuevoNodo.parent = nodoActual
            if nuevoNodo.est == '0':
                termino = recorrerLabPP(arbolPP, nuevoNodo, laberinto)
            elif nuevoNodo.est == 'F':
                termino = True
    
    if not termino:
        # Recorrer derecha
        if nodoActual.cordX < 9:
            x = nodoActual.cordX + 1
            y = nodoActual.cordY
            celda = laberinto[y][x]
            nivel = nodoActual.level + 1
            if (celda == '0' or celda == 'I') and existeNodo(arbolPP, x, y):
                celda = 'B'
            nuevoNodo = crearNodo(x, y, celda, nivel)
            nuevoNodo.parent = nodoActual
            if nuevoNodo.est == '0':
                termino = recorrerLabPP(arbolPP, nuevoNodo, laberinto)
            elif nuevoNodo.est == 'F':
                termino = True
    return termino