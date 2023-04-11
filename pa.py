from funciones import crearNodo, existeNodo
from anytree import Node, LevelOrderIter

def recorrerLabPA(arbolPA: Node, laberinto: int):
    #Función que permite recorrer el laberinto mediante la técnica de primero en amplitud
    termino = False
    agregoNodo = True #Bandera que permite controlar si se agregó por lo menos un nodo. Por si no hay salida del laberinto
    x = 0
    y = 0
    nivel = 1
    raiz = arbolPA
    nodoActual = arbolPA

    while (not termino and agregoNodo):
        agregoNodo = False
        nivel = nivel + 1
        for nodoActual in raiz.leaves:  # se itera únicamente sobre las hojas del árbol
            if nodoActual.est == '0' or nodoActual.est == 'I':   # Se agregan hijos únicamente a los nodos hojas
                if (nodoActual.cordY > 0 and not termino):    # Recorrer arriba
                    x = nodoActual.cordX
                    y = nodoActual.cordY - 1
                    celda = laberinto[y][x]
                    if (celda == '0' or celda == 'I') and existeNodo(arbolPA, x, y):
                        celda = 'B'
                    nuevoNodo = crearNodo(x, y, celda, nivel)
                    nuevoNodo.parent = nodoActual
                    agregoNodo = True
                    if nuevoNodo.est == 'F':
                        termino = True        
                if (nodoActual.cordX > 0 and not termino):    # Recorrer izquierda
                    x = nodoActual.cordX - 1
                    y = nodoActual.cordY
                    celda = laberinto[y][x]
                    if (celda == '0' or celda == 'I') and existeNodo(arbolPA, x, y):
                        celda = 'B'
                    nuevoNodo = crearNodo(x, y, celda, nivel)
                    nuevoNodo.parent = nodoActual
                    agregoNodo = True
                    if nuevoNodo.est == 'F':
                        termino = True
                if (nodoActual.cordY < 9 and not termino):    # Recorrer abajo
                    x = nodoActual.cordX
                    y = nodoActual.cordY + 1
                    celda = laberinto[y][x]
                    if (celda == '0' or celda == 'I') and existeNodo(arbolPA, x, y):
                        celda = 'B'
                    nuevoNodo = crearNodo(x, y, celda, nivel)
                    nuevoNodo.parent = nodoActual
                    agregoNodo = True
                    if nuevoNodo.est == 'F':
                        termino = True
                if (nodoActual.cordX < 9 and not termino):    # Recorrer derecha
                    x = nodoActual.cordX + 1
                    y = nodoActual.cordY
                    celda = laberinto[y][x]
                    if (celda == '0' or celda == 'I') and existeNodo(arbolPA, x, y):
                        celda = 'B'
                    nuevoNodo = crearNodo(x, y, celda, nivel)
                    nuevoNodo.parent = nodoActual
                    agregoNodo = True
                    if nuevoNodo.est == 'F':
                        termino = True
            '''if nodoActual.est == 'F':
                termino = True'''
    return termino
