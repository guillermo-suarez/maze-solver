from genlab import maze
from anytree import Node, RenderTree, find_by_attr
from colorama import Fore

def crearNodo(x: int, y: int):
    nombre = "(" + str(x) + ", " + str(y) + ")"
    nuevoNodo = Node(name = nombre, cordX = x, cordY = y)
    return nuevoNodo

def existeNodo(arbol: Node, x: int, y: int):
    existe = True
    nombre = "(" + str(x) + ", " + str(y) + ")"
    if find_by_attr(arbol, nombre) == None:
        existe = False
    return existe

def recorrer(nodo: Node):
    # Si aplica, se comienza recorriendo la celda de arriba
    termino = False
    if not termino:
        if nodo.cordY > 0:
            if maze[nodo.cordY - 1][nodo.cordX] == '0' or maze[nodo.cordY - 1][nodo.cordX] == 'F':
                if not existeNodo(arbol, nodo.cordX, nodo.cordY - 1):
                    nuevoNodo = crearNodo(nodo.cordX, nodo.cordY - 1)
                    nuevoNodo.parent = nodo
                    if maze[nodo.cordY - 1][nodo.cordX] == 'F':
                        termino = True
                        return True
                    else:
                        termino = recorrer(nuevoNodo)
    # Luego se recorre hacia la derecha de la matriz
    if not termino:
        if nodo.cordX > 0:
            if maze[nodo.cordY][nodo.cordX - 1] == '0' or maze[nodo.cordY][nodo.cordX - 1] == 'F':
                if not existeNodo(arbol, nodo.cordX - 1, nodo.cordY):
                    nuevoNodo = crearNodo(nodo.cordX - 1, nodo.cordY)
                    nuevoNodo.parent = nodo
                    if maze[nodo.cordY][nodo.cordX - 1] == 'F':
                        termino = True
                        return True
                    else:
                        termino = recorrer(nuevoNodo)
    # Abajo
    if not termino:
        if nodo.cordY < 9:
            if maze[nodo.cordY + 1][nodo.cordX] == '0' or maze[nodo.cordY + 1][nodo.cordX] == 'F':
                if not existeNodo(arbol, nodo.cordX, nodo.cordY + 1):
                    nuevoNodo = crearNodo(nodo.cordX, nodo.cordY + 1)
                    nuevoNodo.parent = nodo
                    if maze[nodo.cordY + 1][nodo.cordX] == 'F':
                        termino = True
                        return True
                    else:
                        termino = recorrer(nuevoNodo)
    # Izquierda
    if not termino:
        if nodo.cordX < 9:
            if maze[nodo.cordY][nodo.cordX + 1] == '0' or maze[nodo.cordY][nodo.cordX + 1] == 'F':
                if not existeNodo(arbol, nodo.cordX + 1, nodo.cordY):
                    nuevoNodo = crearNodo(nodo.cordX + 1, nodo.cordY)
                    nuevoNodo.parent = nodo
                    if maze[nodo.cordY][nodo.cordX + 1] == 'F':
                        termino = True
                        return True
                    else:
                        termino = recorrer(nuevoNodo)
    return termino


arbol = crearNodo(9, 9)
recorrer(arbol)

print(Fore.WHITE)

for pre, _, node in RenderTree(arbol):
    print("%s%s" % (pre, node.name))