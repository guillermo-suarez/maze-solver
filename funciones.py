from anytree import Node, RenderTree, PreOrderIter
from anytree.exporter import DotExporter
from colorama import Fore

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

class Estado:
    def __init__(self, x, y, estado, nivel, padre):
        self.x = x
        self.y = y
        self.estado = estado
        self.nivel = nivel
        self.padre = padre
    def __str__(self):
        if self.padre:
            return f"({self.x}, {self.y}) - {self.estado} - Padre: ({self.padre.x}, {self.padre.y})"
        else:
            return f"({self.x}, {self.y}) - {self.estado} - Padre: NO TIENE"
        
def hijoNodoActual(laberinto: int, y: int, x: int, estadoActual: Estado, listaPendientes, listaVisitados):
    if not existeEstadoEnLista(listaVisitados, x, y):
        celda = laberinto[y][x]
        nuevoEstado = Estado(x, y, celda, estadoActual.nivel + 1, estadoActual)
        return nuevoEstado
    else:
        return None
    
def removerRepetidos(lista):
    noRepetidos = []
    for estado in lista:
        if not existeEstadoEnLista(noRepetidos, estado.x, estado.y):
            noRepetidos.append(estado)
        else:
            lista.remove(estado)
    return lista

def existeEstadoEnLista(lista, x, y):
    existe = False
    for estado in lista:
        if estado.x == x and estado.y == y:
            existe = True
            break
    return existe

def crearNodo(id: int, x: int, y: int, estado: str, nivel: int, pendiente: bool):
    nombre = "(" + str(x) + ", " + str(y) + ")"
    nuevoNodo = Node(name = nombre, cordX = x, cordY = y, est = estado, id = id, level = nivel, pend = pendiente)
    return nuevoNodo

def getNodo(arbol: Node, x: int, y: int):
    nodoBuscado = None
    for nodo in PreOrderIter(arbol):
        if nodo.cordX == x and nodo.cordY == y:
            nodoBuscado = nodo
            break
    return nodoBuscado

def crearArbolExpansion(visitados, pendientes):
    id = 1
    for estado in visitados:
        nuevoNodo = crearNodo(id, estado.x, estado.y, estado.estado, estado.nivel, False)
        id = id + 1
        if estado.padre:
            nuevoNodo.parent = getNodo(nodoAnterior.root, estado.padre.x, estado.padre.y)
        nodoAnterior = nuevoNodo
    for estado in pendientes:
        nuevoNodo = crearNodo(id, estado.x, estado.y, estado.estado, estado.nivel, True)
        id = id + 1
        if estado.padre:
            nuevoNodo.parent = getNodo(nodoAnterior.root, estado.padre.x, estado.padre.y)
        nodoAnterior = nuevoNodo
    return nodoAnterior.root


def imprimirArbol(arbol: Node):
    if arbol:
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
        print(Fore.WHITE)

def getMatrizRecorrida(arbol: Node, filas: int, columnas: int):
    if arbol:
        lab = []
        for x in range(0, filas):
            fila = []
            for y in range (0, columnas):
                fila.append('N')
            lab.append(fila)
        for nodo in PreOrderIter(arbol):
            lab[nodo.cordY][nodo.cordX] = nodo.est
        return lab
    else:
        return None

def imprimirMatriz(matriz):
    if matriz:
        filas = len(matriz)
        columnas = len(matriz[0])
        for i in range(0, filas):
            for j in range(0, columnas):
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

def getNodoFinal(arbol: Node):
    nodoFinal = None
    for nodo in arbol.leaves:
        if nodo.est == 'F':
            nodoFinal = nodo
            break
    return nodoFinal

def getCaminoSolucion(arbol: Node):
    solucion = None
    nodoFinal = getNodoFinal(arbol)
    if nodoFinal != None:
        nodoActual = nodoFinal
        nodos = []
        while nodoActual.parent != None:
            nodos.insert(0, nodoActual)
            nodoActual = nodoActual.parent
        solucion = crearNodo(1, arbol.root.cordX, arbol.root.cordY, 'I', 1, False)
        nodoAnt = solucion
        for nodo in nodos:
            nuevoNodo = crearNodo(nodoAnt.id + 1, nodo.cordX, nodo.cordY, nodo.est, nodo.level, False)
            nuevoNodo.parent = nodoAnt
            nodoAnt = nuevoNodo
    return solucion

def arbolAPng(arbol: Node, path: str):
    config = []
    config.append("bgcolor = transparent")
    config.append("edge[color = white]")
    config.append('''
    {
        mindist=0;
        ranksep=0;
        nodesep=0;

        node[shape = box, margin="0,0", width = 1, height = 1, color = white, fontcolor = white];
        edge[style=invis];

        Legend[width=2];
        Legend -> Foo;
        Legend -> FooValue;
        Foo -> Bar;
        FooValue -> BarValue
        Bar -> Baz;
        BarValue -> BazValue;

        edge [constraint=false];
        Foo -> FooValue;
        Bar -> BarValue
        Baz -> BazValue;
    }''')
    arbolDot = DotExporter(arbol,
                           nodeattrfunc = lambda n: 'label = "#%s\n%s", style = %s, fillcolor = %s, color = %s, fontcolor = white, fontname = \"Arial\"'
                           % (n.id, n.name,
                              "dashed" if n.pend else "filled",
                              "darkgreen" if n.est == '0' else ("darkred" if n.est == 'X' else "darkblue"),
                              "white" if n.pend else "white"),
                           edgeattrfunc = lambda n, c: 'style = %s'
                           % ("dashed" if c.pend else "solid"),
                           options = config)
    arbolDot.to_picture(path)

def laberintoAPng(laberinto, filas: int, columnas: int, path: str):


    array = np.zeros((filas, columnas))

    for i in range(0, columnas):
        for j in range(0, filas):
            if laberinto[j][i] == 'X':
                array[j][i] = -1.0
            elif laberinto[j][i] == '0':
                array[j][i] = 0.0
            elif laberinto[j][i] == 'I' or laberinto[j][i] == 'F':
                array[j][i] = 1.0

    cmap = colors.ListedColormap(['red', 'green', 'blue'])
    bounds = [-1.0, 0.0, 1.0, 2.0]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    ax.imshow(array, cmap = cmap, norm = norm)

    ax.grid(which = 'minor', axis = 'both', linestyle = '-', color = 'white', linewidth = 2)
    plt.xticks(range(columnas), range(columnas), color = 'white')
    plt.yticks(range(filas), range(filas), color = 'white')
    ax.set_xticks([x - 0.5 for x in range(1, columnas)], minor = True)
    ax.set_yticks([y - 0.5 for y in range(1, filas)], minor = True)
    ax.spines['top'].set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    plt.savefig(path, bbox_inches = 'tight', transparent = True)