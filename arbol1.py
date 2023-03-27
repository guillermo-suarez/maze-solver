from genlab import maze
from anytree import Node, RenderTree, find_by_attr
from colorama import Fore

print(Fore.WHITE)

arbol = Node(name = "(10, 10)", cordX = 10, cordY = 10)

relegados = []

# Se recorre el arbol desde abajo a la derecha hacia arriba a la izquierda
# Se recorre cada fila de derecha a izquierda
# Y se van recorriendo las filas desde abajo hacia arriba
for j in range(10, 0, -1):
    for i in range (10, 0, -1):
        padre = None
        if maze[j-1][i-1] == '0':
            nodo = Node(name = "(" + str(i) + ", " + str(j) + ")", cordY = j, cordX = i)
            # Si existe un nodo a la DERECHA para que sea su padre...
            if find_by_attr(arbol, "(" + str(i + 1) + ", " + str(j) + ")") != None:
                padre = find_by_attr(arbol, "(" + str(i + 1) + ", " + str(j) + ")")
            # Si existe un nodo ABAJO para que sea su padre...
            elif find_by_attr(arbol, "(" + str(i) + ", " + str(j + 1) + ")") != None:
                padre = find_by_attr(arbol, "(" + str(i) + ", " + str(j + 1) + ")")
            # Si existe un nodo a la IZQUIERDA para que sea su padre...
            elif find_by_attr(arbol, "(" + str(i - 1) + ", " + str(j) + ")") != None:
                padre = find_by_attr(arbol, "(" + str(i - 1) + ", " + str(j) + ")")
            # Si existe un nodo ARRIBA para que sea su padre...
            elif find_by_attr(arbol, "(" + str(i) + ", " + str(j - 1) + ")") != None:
                padre = find_by_attr(arbol, "(" + str(i) + ", " + str(j - 1) + ")")
            # Si se le pudo encontrar un padre, se lo agrega al árbol
            if padre != None:
                nodo.parent = padre
            # Si su nodo padre todavía no se agregó al árbol... ¿?¿?¿?¿?
            else:
                relegados.append(nodo)

a = 0

while len(relegados) != 0:
    padre = None
    # Si ahora si existe un nodo a la DERECHA para que sea su padre
    if find_by_attr(arbol, "(" + str(relegados[a].cordY) + ", " + str(relegados[a].cordX + 1) + ")") != None:
        padre = find_by_attr(arbol, "(" + str(relegados[a].cordY) + ", " + str(relegados[a].cordX + 1) + ")")
    # Si ahora si existe un nodo ABAJO para que sea su padre
    elif find_by_attr(arbol, "(" + str(relegados[a].cordY + 1) + ", " + str(relegados[a].cordX) + ")") != None:
        padre = find_by_attr(arbol, "(" + str(relegados[a].cordY + 1) + ", " + str(relegados[a].cordX) + ")")
    # Si ahora si existe un nodo a la IZQUIERDA para que sea su padre
    elif find_by_attr(arbol, "(" + str(relegados[a].cordY) + ", " + str(relegados[a].cordX - 1) + ")") != None:
        padre = find_by_attr(arbol, "(" + str(relegados[a].cordY) + ", " + str(relegados[a].cordX - 1) + ")")
    # Si ahora si existe un nodo ARIBA para que sea su padre
    elif find_by_attr(arbol, "(" + str(relegados[a].cordY - 1) + ", " + str(relegados[a].cordX) + ")") != None:
        padre = find_by_attr(arbol, "(" + str(relegados[a].cordY - 1) + ", " + str(relegados[a].cordX) + ")")
    if padre != None:
        nodo = relegados.pop(a)
        nodo.parent = padre
        a = a - 1
    a = a + 1
    if a > (len(relegados) - 1):
        a = 0

final = Node(name = "(1, 1)", cordX = 1, cordY = 1)
padre = None
if find_by_attr(arbol, "(" + str(final.cordY) + ", " + str(final.cordX + 1) + ")") != None:
    padre = find_by_attr(arbol, "(" + str(final.cordY) + ", " + str(final.cordX + 1) + ")")
else:
    padre = find_by_attr(arbol, "(" + str(final.cordY + 1) + ", " + str(final.cordX) + ")")
final.parent = padre

for pre, _, node in RenderTree(arbol):
    print("%s%s" % (pre, node.name))