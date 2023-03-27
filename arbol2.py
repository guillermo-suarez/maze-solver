from genlab import maze
from anytree import Node, RenderTree, find_by_attr
from colorama import Fore

print(Fore.WHITE)

def recorrer(nodoAnt: Node):
    # si en el laberinto hay celda a la izquierda, recorre por ahí...
    # PREGUNTAR SI ESENODO != NODOANT
    if (maze[nodoAnt.cordY - 1][nodoAnt.cordX - 2] == '0') or (maze[nodoAnt.cordY - 1][nodoAnt.cordX - 2] == 'F'):
        nuevoNodo = Node(name = "(" + str(nodoAnt.cordX - 1) + ", " + str(nodoAnt.cordY) + ")", cordX = nodoAnt.cordX - 1, cordY = nodoAnt.cordY)
        nuevoNodo.parent = nodoAnt
        recorrer(nuevoNodo)
    # Si además en el laberinto hay celda arriba, también recorre por ahí...
    if (maze[nodoAnt.cordY - 2][nodoAnt.cordX - 1] == '0') or (maze[nodoAnt.cordY - 2][nodoAnt.cordX - 1] == 'F'):
        nuevoNodo = Node(name = "(" + str(nodoAnt.cordX) + ", " + str(nodoAnt.cordY - 1) + ")", cordX = nodoAnt.cordX, cordY = nodoAnt.cordY - 1)
        nuevoNodo.parent = nodoAnt
        recorrer(nuevoNodo)
    # Si además en el laberinto hay celda a la derecha, también recorre por ahí...
    # if (maze[nodoAnt.cordY - 1][nodoAnt.cordX] == '0') or (maze[nodoAnt.cordY - 1][nodoAnt.cordX] == 'F'):
    #     nuevoNodo = Node(name = "(" + str(nodoAnt.cordX + 1) + ", " + str(nodoAnt.cordY) + ")", cordX = nodoAnt.cordX + 1, cordY = nodoAnt.cordY)
    #     nuevoNodo.parent = nodoAnt
    #     recorrer(nuevoNodo)
    # Si además en el laberinto hay celda abajo, también recorre por ahí...
    # if (maze[nodoAnt.cordY][nodoAnt.cordX - 1] == '0') or (maze[nodoAnt.cordY][nodoAnt.cordX - 1] == 'F'):
    #     nuevoNodo = Node(name = "(" + str(nodoAnt.cordX) + ", " + str(nodoAnt.cordY + 1) + ")", cordX = nodoAnt.cordX, cordY = nodoAnt.cordY + 1)
    #     nuevoNodo.parent = nodoAnt
    #     recorrer(nuevoNodo)

arbol = Node(name = "(10, 10)", cordX = 10, cordY = 10)
recorrer(arbol)

for pre, _, node in RenderTree(arbol):
    print("%s%s" % (pre, node.name))