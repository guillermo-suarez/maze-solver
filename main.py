from genlab import maze
from colorama import Fore
from funciones import imprimirMatriz, crearArbolExpansion, imprimirArbol, getMatrizRecorrida, getCaminoSolucion
from pp import recorrerLabPP
from pa import recorrerLabPA
from anytree.exporter import UniqueDotExporter
import PySimpleGUI as sg

print("\n" + Fore.WHITE + "LABERINTO A RECORRER:\n")
imprimirMatriz(maze)

filas = len(maze)
columnas = len(maze[0])

visitadosPP, pendientesPP = recorrerLabPP(maze)

# print("\n" + Fore.WHITE + "[PP] VISITADOS")
# for x in visitadosPP:
#     print(x)
# print("\n" + Fore.WHITE + "[PP] PENDIENTES")
# for x in pendientesPP:
#     print(x)

arbolPP = crearArbolExpansion(visitadosPP, pendientesPP)
print(Fore.WHITE + "[PP] ÁRBOL DE EXPANSIÓN:\n")
imprimirArbol(arbolPP)

configDotExporter = []
configDotExporter.append("bgcolor = \"#ffffff00\"")
configDotExporter.append("edge[color = white]")
arbolPPDot = UniqueDotExporter(arbolPP, nodeattrfunc = lambda n: "label = \"#%s\n%s\nNivel: %s\", fillcolor = %s, style = filled, color = white, fontcolor = white" % (n.id, n.name, n.level, "darkgreen" if n.est == '0' else ("red" if n.est == 'X' else "blue")), options = configDotExporter, )
arbolPPDot.to_picture("expPP.png")

# im = Image.open("expPP.png")
# print("Tamaño de la imagen antes de resize: (%s, %s)" % (im.size[0], im.size[1]))
# newsize = (int(im.size[0] * 0.35), int(im.size[1] * 0.35))
# im = im.resize(newsize)
# im.save("expPPrs.png")
# print("Tamaño de la imagen después de resize: (%s, %s)" % (im.size[0], im.size[1]))

sg.theme("DarkAmber")
column = [[sg.Image(source = "expPP.png")]]
layout = [[sg.Column(column, size = (1920, 1080), scrollable = True)]]
ventana = sg.Window(title = "hola", layout = layout).read()

# matrizPP = getMatrizRecorrida(arbolPP, filas, columnas)
# print(Fore.WHITE + "\n[PP] MATRIZ RECORRIDA:\n")
# imprimirMatriz(matrizPP)

# solucionPP = getCaminoSolucion(arbolPP)
# print(Fore.WHITE + "\n[PP] ÁRBOL SOLUCIÓN:\n")
# imprimirArbol(solucionPP)

# UniqueDotExporter(solucionPP, nodeattrfunc = lambda n: 'label = "#%s\n%s\n%s"' % (n.id, n.name, n.est)).to_picture("solPP.png")

# matrizSolucionPP = getMatrizRecorrida(solucionPP, filas, columnas)
# print(Fore.WHITE + "\n[PP] CAMINO SOLUCIÓN:\n")
# imprimirMatriz(matrizSolucionPP)

# visitadosPA, pendientesPA = recorrerLabPA(maze)

# print("\n" + Fore.WHITE + "[PA] VISITADOS")
# for x in visitadosPA:
#     print(x)
# print("\n" + Fore.WHITE + "[PA] PENDIENTES")
# for x in pendientesPA:
#     print(x)

# arbolPA = crearArbolExpansion(visitadosPA, pendientesPA)
# print(Fore.WHITE + "\n[PA] ARBOL DE EXPANSIÓN:\n")
# imprimirArbol(arbolPA)

# UniqueDotExporter(arbolPA, nodeattrfunc = lambda n: 'label = "#%s\n%s\n%s"' % (n.id, n.name, n.est)).to_picture("expPA.png")

# matrizPA = getMatrizRecorrida(arbolPA, filas, columnas)
# print(Fore.WHITE + "\n[PA] MATRIZ RECORRIDA:\n")
# imprimirMatriz(matrizPA)

# solucionPA = getCaminoSolucion(arbolPA)
# print(Fore.WHITE + "\n[PA] ÁRBOL SOLUCIÓN:\n")
# imprimirArbol(solucionPA)

# UniqueDotExporter(solucionPA, nodeattrfunc = lambda n: 'label = "#%s\n%s\n%s"' % (n.id, n.name, n.est)).to_picture("solPA.png")

# matrizSolucionPA = getMatrizRecorrida(solucionPA, filas, columnas)
# print(Fore.WHITE + "\n[PA] CAMINO SOLUCIÓN:\n")
# imprimirMatriz(matrizSolucionPA)