from genlab import maze
from anytree import Node, RenderTree, findall_by_attr
from colorama import Fore

contNodos = 0

def crearNodo(x: int, y: int, estado: str, nivel: int):
    global contNodos
    nombre = "(" + str(x) + ", " + str(y) + ")"
    contNodos = contNodos + 1
    nuevoNodo = Node(name = nombre, cordX = x, cordY = y, est = estado, id = contNodos, level = nivel)
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
            x = nodoActual.cordX
            y = nodoActual.cordY - 1
            celda = getCelda(x, y)
            nivel = nodoActual.level + 1
            if celda == '0' and existeNodo(arbolPP, x, y):
                celda = 'B'
            nuevoNodo = crearNodo(x, y, celda, nivel)
            nuevoNodo.parent = nodoActual
            if nuevoNodo.est == '0':
                termino = recorrerArbol(nuevoNodo)
            elif nuevoNodo.est == 'F':
                termino = True
    
    if not termino:
        # Recorrer izquierda
        if nodoActual.cordX > 0:
            x = nodoActual.cordX - 1
            y = nodoActual.cordY
            celda = getCelda(x, y)
            nivel = nodoActual.level + 1
            if (celda == '0' or celda == 'I') and existeNodo(arbolPP, x, y):
                celda = 'B'
            nuevoNodo = crearNodo(x, y, celda, nivel)
            nuevoNodo.parent = nodoActual
            if nuevoNodo.est == '0':
                termino = recorrerArbol(nuevoNodo)
            elif nuevoNodo.est == 'F':
                termino = True
    
    if not termino:
        # Recorrer abajo
        if nodoActual.cordY < 9:
            x = nodoActual.cordX
            y = nodoActual.cordY + 1
            celda = getCelda(x, y)
            nivel = nodoActual.level + 1
            if celda == '0' and existeNodo(arbolPP, x, y):
                celda = 'B'
            nuevoNodo = crearNodo(x, y, celda, nivel)
            nuevoNodo.parent = nodoActual
            if nuevoNodo.est == '0':
                termino = recorrerArbol(nuevoNodo)
            elif nuevoNodo.est == 'F':
                termino = True
    
    if not termino:
        # Recorrer derecha
        if nodoActual.cordX < 9:
            x = nodoActual.cordX + 1
            y = nodoActual.cordY
            celda = getCelda(x, y)
            nivel = nodoActual.level + 1
            if celda == '0' and existeNodo(arbolPP, x, y):
                celda = 'B'
            nuevoNodo = crearNodo(x, y, celda, nivel)
            nuevoNodo.parent = nodoActual
            if nuevoNodo.est == '0':
                termino = recorrerArbol(nuevoNodo)
            elif nuevoNodo.est == 'F':
                termino = True
    return termino

arbolPP = crearNodo(9, 9, 'I', 1)
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
    print("[#%s] %s | N: %s | E: %s" % (node.id, node.name, node.level, node.est))
