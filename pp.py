from genlab import maze
from anytree import Node, RenderTree, findall_by_attr
from colorama import Fore

contNodos = 0

def crearNodo(x: int, y: int, estado: str):
    global contNodos
    nombre = "(" + str(x) + ", " + str(y) + ")"
    contNodos = contNodos + 1
    nuevoNodo = Node(name = nombre, cordX = x, cordY = y, est = estado, id = contNodos)
    return nuevoNodo

def existeNodo(arbol: Node, x: int, y: int):
    existe = True
    nombre = "(" + str(x) + ", " + str(y) + ")"
    if len(findall_by_attr(arbol, nombre, name = 'name')) == 0:
        existe = False
    return existe

def getCelda(x: int, y: int):
    return maze[y][x]

def recorrerArbol(nodoActual: Node):
    termino = False
    
    if not termino:
        # Recorrer arriba
        if nodoActual.cordY > 0:
            celda = getCelda(nodoActual.cordX, nodoActual.cordY - 1)
            if celda == 'F':
                nuevoNodo = crearNodo(nodoActual.cordX, nodoActual.cordY - 1, celda)
                nuevoNodo.parent = nodoActual
                termino = True
            elif celda == '0':
                if not existeNodo(arbolPP, nodoActual.cordX, nodoActual.cordY - 1):
                    nuevoNodo = crearNodo(nodoActual.cordX, nodoActual.cordY - 1, celda)
                    nuevoNodo.parent = nodoActual
                    termino = recorrerArbol(nuevoNodo)
                else:
                    nuevoNodo = crearNodo(nodoActual.cordX, nodoActual.cordY - 1, 'B')
                    nuevoNodo.parent = nodoActual
            else:
                nuevoNodo = crearNodo(nodoActual.cordX, nodoActual.cordY - 1, 'X')
                nuevoNodo.parent = nodoActual
    
    if not termino:
        # Recorrer izquierda
        if nodoActual.cordX > 0:
            celda = getCelda(nodoActual.cordX - 1, nodoActual.cordY)
            if celda == 'F':
                nuevoNodo = crearNodo(nodoActual.cordX - 1, nodoActual.cordY, celda)
                nuevoNodo.parent = nodoActual
                termino = True
            elif celda == '0':
                if not existeNodo(arbolPP, nodoActual.cordX - 1, nodoActual.cordY):
                    nuevoNodo = crearNodo(nodoActual.cordX - 1, nodoActual.cordY, celda)
                    nuevoNodo.parent = nodoActual
                    termino = recorrerArbol(nuevoNodo)
                else:
                    nuevoNodo = crearNodo(nodoActual.cordX - 1, nodoActual.cordY, 'B')
                    nuevoNodo.parent = nodoActual
            else:
                nuevoNodo = crearNodo(nodoActual.cordX - 1, nodoActual.cordY, 'X')
                nuevoNodo.parent = nodoActual
    
    if not termino:
        # Recorrer abajo
        if nodoActual.cordY < 9:
            celda = getCelda(nodoActual.cordX, nodoActual.cordY + 1)
            if celda == 'F':
                nuevoNodo = crearNodo(nodoActual.cordX, nodoActual.cordY + 1, celda)
                nuevoNodo.parent = nodoActual
                termino = True
            elif celda == '0':
                if not existeNodo(arbolPP, nodoActual.cordX, nodoActual.cordY + 1):
                    nuevoNodo = crearNodo(nodoActual.cordX, nodoActual.cordY + 1, celda)
                    nuevoNodo.parent = nodoActual
                    termino = recorrerArbol(nuevoNodo)
                else:
                    nuevoNodo = crearNodo(nodoActual.cordX, nodoActual.cordY + 1, 'B')
                    nuevoNodo.parent = nodoActual
            else:
                nuevoNodo = crearNodo(nodoActual.cordX, nodoActual.cordY + 1, 'X')
                nuevoNodo.parent = nodoActual
    
    if not termino:
        # Recorrer derecha
        if nodoActual.cordX < 9:
            celda = getCelda(nodoActual.cordX + 1, nodoActual.cordY)
            if celda == 'F':
                nuevoNodo = crearNodo(nodoActual.cordX + 1, nodoActual.cordY, celda)
                nuevoNodo.parent = nodoActual
                termino = True
            elif celda == '0':
                if not existeNodo(arbolPP, nodoActual.cordX + 1, nodoActual.cordY):
                    nuevoNodo = crearNodo(nodoActual.cordX + 1, nodoActual.cordY, celda)
                    nuevoNodo.parent = nodoActual
                    termino = recorrerArbol(nuevoNodo)
                else:
                    nuevoNodo = crearNodo(nodoActual.cordX + 1, nodoActual.cordY, 'B')
                    nuevoNodo.parent = nodoActual
            else:
                nuevoNodo = crearNodo(nodoActual.cordX + 1, nodoActual.cordY, 'X')
                nuevoNodo.parent = nodoActual
    return termino

arbolPP = crearNodo(9, 9, 'I')
recorrerArbol(arbolPP)

for pre, _, node in RenderTree(arbolPP):
    print(Fore.WHITE + "%s" % (pre), end="")
    if node.est == 'I':
        print(Fore.BLUE, end="")
    elif node.est == '0':
        print(Fore.WHITE, end="")
    elif node.est == 'F':
        print(Fore.GREEN, end="")
    elif node.est == 'B':
        print(Fore.YELLOW, end="")
    elif node.est == 'X':
        print(Fore.RED, end="")
    print("[%s] %s Estado: %s" % (node.id, node.name, node.est))
