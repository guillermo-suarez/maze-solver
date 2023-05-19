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

def crearNodo(id: int, x: int, y: int, estado: str, nivel: int):
    nombre = "(" + str(x) + ", " + str(y) + ")"
    nuevoNodo = Node(name = nombre, cordX = x, cordY = y, est = estado, id = id, level = nivel, esSolucion = False)
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
        nuevoNodo = crearNodo(id, estado.x, estado.y, estado.estado, estado.nivel)
        id = id + 1
        if estado.padre:
            nuevoNodo.parent = getNodo(nodoAnterior.root, estado.padre.x, estado.padre.y)
        nodoAnterior = nuevoNodo
    for estado in pendientes:
        nuevoNodo = crearNodo(id, estado.x, estado.y, 'P', estado.nivel)
        id = id + 1
        if estado.padre:
            nuevoNodo.parent = getNodo(nodoAnterior.root, estado.padre.x, estado.padre.y)
        nodoAnterior = nuevoNodo
    arbolExpansion = nodoAnterior.root
    nodoFinal = getNodoFinal(arbolExpansion)
    if nodoFinal != None:
        nodoActual = nodoFinal
        while nodoActual.parent != None:
            nodoActual.esSolucion = True
            nodoActual = nodoActual.parent
        nodoActual.esSolucion = True
    return arbolExpansion


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
            elif node.est == 'P':
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
            if nodo.esSolucion == True and nodo.est == '0':
                lab[nodo.cordY][nodo.cordX] = 'S'
            else:
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
                elif(matriz[i][j] == 'P'):
                    print(Fore.YELLOW, end = "")	
                elif(matriz[i][j] == 'X'):
                    print(Fore.RED, end = "")
                elif(matriz[i][j] == 'S'):
                    print(Fore.CYAN, end = "")	
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
            nodoActual.esSolucion = True
            nodos.insert(0, nodoActual)
            nodoActual = nodoActual.parent
        nodoActual.esSolucion = True
        solucion = crearNodo(1, arbol.root.cordX, arbol.root.cordY, 'I', 1)
        nodoAnt = solucion
        for nodo in nodos:
            nuevoNodo = crearNodo(nodoAnt.id + 1, nodo.cordX, nodo.cordY, nodo.est, nodo.level)
            nuevoNodo.parent = nodoAnt
            nodoAnt = nuevoNodo
    return solucion

def marcarCaminoSolucion(laberinto, arbol: Node):
    solucion = copiarLaberinto(laberinto)
    if arbol:
        for pre, _, node in RenderTree(arbol):
            if node.esSolucion and node.est == '0':
                solucion[node.cordY][node.cordX] = 'S'
    return solucion

def copiarLaberinto(laberinto):
    copia = []
    for fila in laberinto:
        copiaFila = list(fila)
        copia.append(copiaFila)
    return copia

def arbolAPng(arbol: Node, path: str):
    config = []
    config.append("bgcolor = transparent")
    config.append("edge[color = white]")
    config.append('''subgraph REF {
        pos = "0,0!"
        Referencias[shape=none, color=white, margin=0, width=2, label=<
            <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
                <TH>
                    <TD COLSPAN="3" COLOR="white"><FONT FACE="Arial" COLOR="white" POINT-SIZE="32"><B>Referencias</B></FONT></TD>
                </TH>
                <TR>
                    <TD COLSPAN="2" COLOR="white">
                        <TABLE BORDER="0">
                            <TR>
                                <TD BORDER="1" STYLE="rounded" COLOR="white" BGCOLOR="darkgreen">       </TD>
                            </TR>
                        </TABLE>
                    </TD>
                    <TD COLSPAN="1" ALIGN="LEFT" COLOR="white"><FONT FACE="Arial" COLOR="white" POINT-SIZE="24">Celda del laberinto libre (camino)</FONT></TD>
                </TR>
                <TR>
                    <TD COLSPAN="2" COLOR="white">
                        <TABLE BORDER="0">
                            <TR>
                                <TD BORDER="1" STYLE="rounded" COLOR="white" BGCOLOR="darkred"></TD>
                            </TR>
                        </TABLE>
                    </TD>
                    <TD COLSPAN="1" ALIGN="LEFT" COLOR="white"><FONT FACE="Arial" COLOR="white" POINT-SIZE="24">Celda del laberinto bloqueada (pared)</FONT></TD>
                </TR>
                <TR>
                    <TD COLSPAN="2" COLOR="white">
                        <TABLE BORDER="0">
                            <TR>
                                <TD BORDER="1" STYLE="rounded" COLOR="white" BGCOLOR="darkblue"></TD>
                            </TR>
                        </TABLE>
                    </TD>
                    <TD COLSPAN="1" ALIGN="LEFT" COLOR="white"><FONT FACE="Arial" COLOR="white" POINT-SIZE="24">Celda inicial o final</FONT></TD>
                </TR>
                <TR>
                    <TD COLSPAN="2" COLOR="white">
                        <TABLE BORDER="0">
                            <TR>
                                <TD BORDER="1" STYLE="rounded" COLOR="white"></TD>
                            </TR>
                        </TABLE>
                    </TD>
                    <TD COLSPAN="1" ALIGN="LEFT" COLOR="white"><FONT FACE="Arial" COLOR="white" POINT-SIZE="24">Celda expandida pero no visitada (quedó en memoria)</FONT></TD>
                </TR>
                <TR>
                    <TD COLSPAN="2" COLOR="white">
                        <TABLE BORDER="0">
                            <TR>
                                <TD BORDER="1" STYLE="rounded" COLOR="yellow"></TD>
                            </TR>
                        </TABLE>
                    </TD>
                    <TD COLSPAN="1" ALIGN="LEFT" COLOR="white"><FONT FACE="Arial" COLOR="white" POINT-SIZE="24">Celda que es parte del camino solución</FONT></TD>
                </TR>
            </TABLE>
        >]
    }''')
    arbolDot = DotExporter(arbol,
                           nodeattrfunc = lambda n: 'label = "#%s\n%s", style = %s, fillcolor = %s, color = %s, fontcolor = white, fontname = \"Arial\"'
                           % (n.id, n.name,
                              "dashed" if n.est == 'P' else "filled",
                              "darkgreen" if n.est == '0' else ("darkred" if n.est == 'X' else "darkblue"),
                              "yellow" if n.esSolucion else "white"),
                           edgeattrfunc = lambda n, c: 'style = %s, color = %s'
                           % ("dashed" if c.est == 'P' else "solid",
                              "yellow" if c.esSolucion else "white"),
                           options = config)
    arbolDot.to_picture(path)

def laberintoAPng(laberinto, filas: int, columnas: int, path: str):

    array = np.zeros((filas, columnas))

    for i in range(0, columnas):
        for j in range(0, filas):
            if laberinto[j][i] == 'X':
                array[j][i] = 0
            elif laberinto[j][i] == '0':
                array[j][i] = 1
            elif laberinto[j][i] == 'I' or laberinto[j][i] == 'F':
                array[j][i] = 2
            elif laberinto[j][i] == 'P':
                array[j][i] = 3
            elif laberinto[j][i] == 'S':
                array[j][i] = 4
            else:
                array[j][i] = 5

    cmap = colors.ListedColormap(['grey', 'white', 'blue', 'yellow', 'green', 'black'])
    bounds = [0, 1, 2, 3, 4, 5, 6]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    ax.imshow(array, cmap = cmap, norm = norm)

    ax.grid(which = 'minor', axis = 'both', linestyle = '-', color = 'black', linewidth = 2)
    plt.xticks(range(columnas), range(columnas), color = 'white')
    plt.yticks(range(filas), range(filas), color = 'white')
    ax.set_xticks([x - 0.5 for x in range(1, columnas)], minor = True)
    ax.set_yticks([y - 0.5 for y in range(1, filas)], minor = True)
    ax.spines['top'].set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    plt.savefig(path, bbox_inches = 'tight', transparent = True)

def iteracionesAPng(iteraciones: list, path: str):
    
    filas = len(iteraciones)
    columnas = 0

    for iter in iteraciones:
        if len(iter) > columnas:
            columnas = len(iter)

    i = 0
    datos = []
    labels = []
    for iter in iteraciones:
        labels.append("$t_{" + str(i) + "}$")
        i = i + 1
        fila = []
        for j in range(0, columnas):
            if j >= len(iter):
                fila.append("")
            else:
                if iter[j].padre:
                    fila.append("$(" + str(iter[j].x) + ", " + str(iter[j].y) + ")^{" + "(" + str(iter[j].padre.x) + ", " + str(iter[j].padre.y) + ")}$")
                else:
                    fila.append("$(" + str(iter[j].x) + ", " + str(iter[j].y) + ")$")
        datos.append(fila)

    fig, ax = plt.subplots()
    ax.set_axis_off()
    table = ax.table(
        cellText = datos,
        # rowLabels = labels,
        # rowLoc = 'center',
        # rowColours = ['grey'] * i,
        cellLoc = 'center',
        loc = 'upper left'
    )

    table.auto_set_font_size(False)
    table.set_fontsize(2)
    table.auto_set_column_width(col = list(range(0, columnas)))
    for i in range(0, filas):
        for j in range(0, columnas):
            table[i, j].set_height(0.017)
            table[i, j].set_edgecolor('white')
            table[i, j].set_linewidth(0.1)

    for i in range(0, filas):
        table[(i, 0)].set_facecolor('yellow')

    plt.savefig(path, bbox_inches = 'tight', transparent = True, dpi = 450)