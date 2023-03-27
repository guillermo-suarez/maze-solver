import anytree

from genlab import maze
from anytree import Node, RenderTree, find_by_attr
from colorama import Fore

arbol = Node(name = "(10, 10)", cordY = 10, cordX = 10)

print(Fore.WHITE)

rel = []

# Se recorre el arbol desde abajo a la derecha hacia arriba a la izquierda
# Se recorre cada fila de derecha a izquierda
# Y se van recorriendo las filas desde abajo hacia arriba
for j in range(10, 0, -1):
    for i in range (10, 0, -1):
        padre = None
        if maze[j-1][i-1] == '0':
            # Si existe un nodo a la DERECHA para que sea su padre...
            if find_by_attr(arbol, "(" + str(j) + ", " + str(i + 1) + ")") != None:
                padre = find_by_attr(arbol, "(" + str(j) + ", " + str(i + 1) + ")")
            # Si existe un nodo ABAJO para que sea su padre...
            elif find_by_attr(arbol, "(" + str(j + 1) + ", " + str(i) + ")") != None:
                padre = find_by_attr(arbol, "(" + str(j + 1) + ", " + str(i) + ")")
            # Si existe un nodo a la IZQUIERDA para que sea su padre...
            elif find_by_attr(arbol, "(" + str(j) + ", " + str(i - 1) + ")") != None:
                padre = find_by_attr(arbol, "(" + str(j) + ", " + str(i - 1) + ")")
            # Si existe un nodo ARRIBA para que sea su padre...
            elif find_by_attr(arbol, "(" + str(j - 1) + ", " + str(i) + ")") != None:
                padre = find_by_attr(arbol, "(" + str(j - 1) + ", " + str(i) + ")")
            # Si se le pudo encontrar un padre, se lo agrega al árbol
            if padre != None:
                nodo = Node(name = "(" + str(j) + ", " + str(i) + ")", parent = padre, cordY = j, cordX = i)
            # Si su nodo padre todavía no se agregó al árbol... ¿?¿?¿?¿?
            else:
                rel.append(Node(name = "(" + str(j) + ", " + str(i) + ")", cordY = j, cordX = i))

# print(RenderTree(arbol))

# print('\n')
# print("Cantidad de nodos que no se pudieron agregar: " + str(len(rel)))
# for nodo in rel:
#     print(nodo)
# print('\n')

a = 0

while len(rel) != 0:
    padre = None
    # Si ahora si existe un nodo a la DERECHA para que sea su padre
    if find_by_attr(arbol, "(" + str(rel[a].cordY) + ", " + str(rel[a].cordX + 1) + ")") != None:
        padre = find_by_attr(arbol, "(" + str(rel[a].cordY) + ", " + str(rel[a].cordX + 1) + ")")
    # Si ahora si existe un nodo ABAJO para que sea su padre
    elif find_by_attr(arbol, "(" + str(rel[a].cordY + 1) + ", " + str(rel[a].cordX) + ")") != None:
        padre = find_by_attr(arbol, "(" + str(rel[a].cordY + 1) + ", " + str(rel[a].cordX) + ")")
    # Si ahora si existe un nodo a la IZQUIERDA para que sea su padre
    elif find_by_attr(arbol, "(" + str(rel[a].cordY) + ", " + str(rel[a].cordX - 1) + ")") != None:
        padre = find_by_attr(arbol, "(" + str(rel[a].cordY) + ", " + str(rel[a].cordX - 1) + ")")
    # Si ahora si existe un nodo ARIBA para que sea su padre
    elif find_by_attr(arbol, "(" + str(rel[a].cordY - 1) + ", " + str(rel[a].cordX) + ")") != None:
        padre = find_by_attr(arbol, "(" + str(rel[a].cordY - 1) + ", " + str(rel[a].cordX) + ")")
    if padre != None:
        nodo = rel.pop(a)
        nodo.parent = padre
        a = a - 1
    a = a + 1
    if a > (len(rel) - 1):
        a = 0

# print("Cantidad de nodos en la lista DESPUÉS del bucle: " + str(len(rel)))
# for nodo in rel:
#     print(nodo)
# print('\n')

final = Node(name = "(1, 1)", cordX = 1, cordY = 1)
padre = None
if find_by_attr(arbol, "(" + str(final.cordY) + ", " + str(final.cordX + 1) + ")") != None:
    padre = find_by_attr(arbol, "(" + str(final.cordY) + ", " + str(final.cordX + 1) + ")")
else:
    padre = find_by_attr(arbol, "(" + str(final.cordY + 1) + ", " + str(final.cordX) + ")")
final.parent = padre

for pre, _, node in RenderTree(arbol):
    print("%s%s" % (pre, node.name))

# print(RenderTree(arbol))