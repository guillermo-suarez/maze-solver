from genlab import getMaze
from colorama import Fore
from funciones import imprimirMatriz, crearArbolExpansion, imprimirArbol, getMatrizRecorrida, getCaminoSolucion, arbolAPng, laberintoAPng
from pp import recorrerLabPP
from pa import recorrerLabPA
from ventanas import crearVentanaArbol

import PySimpleGUI as sg
import graphviz
import matplotlib.pyplot as plt

filas = 10
columnas = 10

laberinto = getMaze(filas, columnas)

# Al descomentar esta línea nos aseguramos que el laberinto no tenga solución
# laberinto[0][1] = 'X'

laberintoAPng(laberinto, filas, columnas, "lab.png")

print("\n" + Fore.WHITE + "LABERINTO A RECORRER:\n")
imprimirMatriz(laberinto)

# PP

iterPP, visitadosPP, pendientesPP = recorrerLabPP(laberinto)

# i = 0
# for iter in iterPP:
#     print("Iteración en t_" + str(i))
#     for x in iter:
#         print(x)
#     i = i + 1

max = 0

for iter in iterPP:
    if len(iter) > max:
        max = len(iter)

i = 0
datos = []
labels = []
for iter in iterPP:
    labels.append("$t_" + str(i) + "$")
    i = i + 1
    fila = []
    for j in range(0, max):
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
    rowLabels = labels,
    rowLoc = 'center',
    cellLoc = 'center',
    loc = 'upper left'
)
plt.savefig("asd.png", bbox_inches = 'tight', transparent = True, dpi = 450)

# dot = graphviz.Graph()
# dot.attr(rankdir = 'LR')
# dot.node_attr['shape'] = 'box'
# dot.node_attr['style'] = 'filled'
# dot.node_attr['fillcolor'] = 'white'

# i = 0
# for iter in iterPP:
#     dot.attr('node', fillcolor = 'yellow')
#     dot.node(name = "h" + str(i), label = "t" + str(i))
#     dot.attr('node', fillcolor = 'white')
#     if i > 0:
#         dot.edge(tail_name = "h" + str(i - 1), head_name = "h" + str(i))
#     for j in range(0, max):
#         if len(iter) > j:
#             est = iter[j]
#             if est.padre:
#                 dot.node(name = str(i) + "." + str(j), label = "(" + str(est.x) + ", " + str(est.y) + ")^(" + str(est.padre.x) + ", " + str(est.padre.y) + ")")
#             else:
#                 dot.node(name = str(i) + "." + str(j), label = "(" + str(est.x) + ", " + str(est.y) + ")")
#         else:
#             dot.node(name = str(i) + "." + str(j), label = "")
#         if j > 0:
#             dot.edge(tail_name = str(i) + "." + str(j - 1), head_name = str(i) + "." + str(j))
#         else:
#             dot.edge(tail_name = "h" + str(i), head_name = str(i) + "." + str(j))
#         if i > 0:
#             dot.edge(tail_name = str(i - 1) + "." + str(j), head_name = str(i) + "." + str(j))
#     i = i + 1
# dot.view()

# print("\n" + Fore.WHITE + "[PP] VISITADOS")
# for x in visitadosPP:
#     print(x)
# print("\n" + Fore.WHITE + "[PP] PENDIENTES")
# for x in pendientesPP:
#     print(x)

# arbolPP = crearArbolExpansion(visitadosPP, pendientesPP)
# print(Fore.WHITE + "[PP] ÁRBOL DE EXPANSIÓN:\n")
# imprimirArbol(arbolPP)

# matrizPP = getMatrizRecorrida(arbolPP, filas, columnas)
# print(Fore.WHITE + "\n[PP] MATRIZ RECORRIDA:\n")
# imprimirMatriz(matrizPP)

# solucionPP = getCaminoSolucion(arbolPP)
# print(Fore.WHITE + "\n[PP] ÁRBOL SOLUCIÓN:\n")
# imprimirArbol(solucionPP)

# matrizSolucionPP = getMatrizRecorrida(solucionPP, filas, columnas)
# print(Fore.WHITE + "\n[PP] CAMINO SOLUCIÓN:\n")
# imprimirMatriz(matrizSolucionPP)

# # PA

# iterPA, visitadosPA, pendientesPA = recorrerLabPA(laberinto)

# print("\n" + Fore.WHITE + "[PA] VISITADOS")
# for x in visitadosPA:
#     print(x)
# print("\n" + Fore.WHITE + "[PA] PENDIENTES")
# for x in pendientesPA:
#     print(x)

# arbolPA = crearArbolExpansion(visitadosPA, pendientesPA)
# print(Fore.WHITE + "\n[PA] ARBOL DE EXPANSIÓN:\n")
# imprimirArbol(arbolPA)

# matrizPA = getMatrizRecorrida(arbolPA, filas, columnas)
# print(Fore.WHITE + "\n[PA] MATRIZ RECORRIDA:\n")
# imprimirMatriz(matrizPA)

# solucionPA = getCaminoSolucion(arbolPA)
# print(Fore.WHITE + "\n[PA] ÁRBOL SOLUCIÓN:\n")
# imprimirArbol(solucionPA)

# matrizSolucionPA = getMatrizRecorrida(solucionPA, filas, columnas)
# print(Fore.WHITE + "\n[PA] CAMINO SOLUCIÓN:\n")
# imprimirMatriz(matrizSolucionPA)

# arbolAPng(arbolPP, "expPP.png")
# arbolAPng(arbolPA, "expPA.png")

# ventanaPP = crearVentanaArbol("expPP.png", "PP")
# ventanaPA = crearVentanaArbol("expPA.png", "PA")

# while True:
#     ventana, evento, valor = sg.read_all_windows()
#     if evento == sg.WIN_CLOSED:
#         if ventana == ventanaPP:
#             ventanaPP.close()
#             ventanaPP = None
#             if ventanaPA == None:
#                 break
#         elif ventana == ventanaPA:
#             ventanaPA.close()
#             ventanaPA = None
#             if ventanaPP == None:
#                 break