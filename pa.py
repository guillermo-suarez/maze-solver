from funciones import crearNodo, existeNodo
from anytree import Node, LevelOrderIter

def hijoNodoactual(laberinto: int, y: int, x: int, nodoActual: Node, arbolPA: Node, nodosAceptados: Node):
    #Realiza todos los pasos de agregar un nodo al árbol y a la lista cuando se busca en las cuatro direcciones
    nivel = nodoActual.level + 1
    termino = False
    celda = laberinto[y][x]
    if (celda == '0' or celda == 'I') and existeNodo(arbolPA, x, y):
        celda = 'B'
    nuevoNodo = crearNodo(x, y, celda, nivel)
    nuevoNodo.parent = nodoActual
    agregoNodo = True
    match nuevoNodo.est:
        case 'F':
            termino = True
        case '0':
            nodosAceptados.append(nuevoNodo)
    return agregoNodo, termino

def recorrerLabPA(arbolPA: Node, laberinto: int):
    #Permite recorrer el laberinto mediante la técnica de primero en amplitud
    termino = False
    agregoNodo = True #Bandera que permite controlar si se agregó por lo menos un nodo. Por si no hay salida del laberinto
    x = 0
    y = 0
    nodosAceptados = [] #Lista que solamente incluye los nodos cuyo estado sea 0
    nodosAceptados.append(arbolPA)

    while (not termino and agregoNodo):
        agregoNodo = False
        for nodoActual in LevelOrderIter(arbolPA): #Recorre únicamente los nodos hojas
            for nodo in nodosAceptados:
                if nodoActual == nodo:
                    if (nodoActual.cordY > 0 and not termino):    # Recorrer arriba
                        x = nodoActual.cordX
                        y = nodoActual.cordY - 1
                        agregoNodo,termino = hijoNodoactual(laberinto,y,x,nodoActual,arbolPA,nodosAceptados)
                    if (nodoActual.cordX > 0 and not termino):    # Recorrer izquierda
                        x = nodoActual.cordX - 1
                        y = nodoActual.cordY
                        agregoNodo,termino = hijoNodoactual(laberinto,y,x,nodoActual,arbolPA,nodosAceptados)
                    if (nodoActual.cordY < 9 and not termino):    # Recorrer abajo
                        x = nodoActual.cordX
                        y = nodoActual.cordY + 1
                        agregoNodo,termino = hijoNodoactual(laberinto,y,x,nodoActual,arbolPA,nodosAceptados)
                    if (nodoActual.cordX < 9 and not termino):    # Recorrer derecha
                        x = nodoActual.cordX + 1
                        y = nodoActual.cordY
                        agregoNodo,termino = hijoNodoactual(laberinto,y,x,nodoActual,arbolPA,nodosAceptados)
                    nodosAceptados.remove(nodoActual)   #Se quita de la lista aquel nodo con el que ya se haya trabajado
    return termino
