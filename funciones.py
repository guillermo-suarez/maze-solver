from anytree import Node, RenderTree, PreOrderIter
from anytree.exporter import DotExporter
from colorama import Fore

import numpy as np
import matplotlib as mpl
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
        
def hijoNodoActual(laberinto: int, y: int, x: int, estadoActual: Estado, listaVisitados):
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

def getNodoFinal(arbol: Node):
    nodoFinal = None
    for nodo in arbol.leaves:
        if nodo.est == 'F':
            nodoFinal = nodo
            break
    return nodoFinal

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
    plt.close()

def crearReferenciasLaberintos():
    mpl.rcParams['text.color'] = 'white'
    fig, ax = plt.subplots()
    ax.set_axis_off()
    table = ax.table(
        cellText = [['       ', 'Libre'], ['       ', 'Pared'], ['       ', 'Inicio y fin']],
        cellColours = [['none'] * 2] * 3,
        cellLoc = 'left',
        loc = 'upper left'
    )
    table.auto_set_font_size(False)
    table.set_fontsize(48)
    table.auto_set_column_width(col = [0, 1])
    for i in range(0, 3):
        for j in range(0, 2):
            table[i, j].set_height(0.45)
            table[i, j].set_edgecolor('white')
            table[i, j].set_linewidth(2.0)
    table[(0, 0)].set_facecolor('white')
    table[(1, 0)].set_facecolor('grey')
    table[(2, 0)].set_facecolor('blue')
    plt.savefig('IMG-referencias-laberinto.png', bbox_inches = 'tight', transparent = True, dpi = 25)
    plt.close()
    
    plt.figure().clear()

    fig, ax = plt.subplots()
    ax.set_axis_off()
    table = ax.table(
        cellText = [['       ', 'Libre'], ['       ', 'Pared'], ['       ', 'Inicio y fin'], ['       ', 'Camino solución']],
        cellColours = [['none'] * 2] * 4,
        cellLoc = 'left',
        loc = 'upper left'
    )
    table.auto_set_font_size(False)
    table.set_fontsize(48)
    table.auto_set_column_width(col = [0, 1])
    for i in range(0, 4):
        for j in range(0, 2):
            table[i, j].set_height(0.45)
            table[i, j].set_edgecolor('white')
            table[i, j].set_linewidth(2.0)
    table[(0, 0)].set_facecolor('white')
    table[(1, 0)].set_facecolor('grey')
    table[(2, 0)].set_facecolor('blue')
    table[(3, 0)].set_facecolor('darkgreen')
    plt.savefig('IMG-referencias-laberinto-completo.png', bbox_inches = 'tight', transparent = True, dpi = 25)
    plt.close()