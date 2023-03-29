from genlab import maze
from anytree import Node, RenderTree, find_by_attr
from colorama import Fore

def crearNodo(x: int, y: int, estado: str):
    nombre = "(" + str(x) + ", " + str(y) + ")"
    nuevoNodo = Node(name = nombre, cordX = x, cordY = y, est = estado)
    return nuevoNodo

def existeNodo(arbol: Node, x: int, y: int):
    existe = True
    nombre = "(" + str(x) + ", " + str(y) + ")"
    if find_by_attr(arbol, nombre) == None:
        existe = False
    return existe

def recorrerMatriz(matriz: int):
    pass

