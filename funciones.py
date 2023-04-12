import numpy as np

from anytree import Node, RenderTree, findall_by_attr, PreOrderIter
from colorama import Fore

contNodos = 0

def crearNodo(x: int, y: int, estado: str, nivel: int):
    global contNodos
    if estado == 'I':
        contNodos = 0
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
    lab = []
    for x in range(0, 10):
        fila = ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
        lab.append(fila)
    for nodo in PreOrderIter(arbol):
        lab[nodo.cordY][nodo.cordX] = nodo.est
    return lab

def imprimirMatriz(matriz):
    for i in range(0, 10):
        for j in range(0, 10):
            if (matriz[i][j] == 'I' or matriz[i][j] == 'F'):
                print(Fore.BLUE, end = "")
            elif (matriz[i][j] == '0'):
                print(Fore.GREEN, end = "")
            elif(matriz[i][j] == 'B'):
                print(Fore.YELLOW, end = "")	
            elif(matriz[i][j] == 'X'):
                print(Fore.RED, end = "")	
            else:
                print(Fore.WHITE, end = "")
            print(str(matriz[i][j]), end = " ")

        print('\n')
    print(Fore.WHITE)
