import numpy as np

from anytree import Node, RenderTree, findall_by_attr, PreOrderIter
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

def imprimirArbol(arbol: Node):
    for pre, _, node in RenderTree(arbol):
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

def crearMatrizRecorrida(arbol: Node):
    for nodo in PreOrderIter(arbol):
        lab[nodo.cordY][nodo.cordX] = nodo.est
    return lab
