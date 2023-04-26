from genlab import maze
from colorama import Fore
from funciones import imprimirMatriz, crearArbolExpansion, imprimirArbol, getMatrizRecorrida, getCaminoSolucion, arbolAPng
from pp import recorrerLabPP
from pa import recorrerLabPA

print("\n" + Fore.WHITE + "LABERINTO A RECORRER:\n")
imprimirMatriz(maze)

filas = len(maze)
columnas = len(maze[0])

# PP

visitadosPP, pendientesPP = recorrerLabPP(maze)

print("\n" + Fore.WHITE + "[PP] VISITADOS")
for x in visitadosPP:
    print(x)
print("\n" + Fore.WHITE + "[PP] PENDIENTES")
for x in pendientesPP:
    print(x)

arbolPP = crearArbolExpansion(visitadosPP, pendientesPP)
print(Fore.WHITE + "[PP] ÁRBOL DE EXPANSIÓN:\n")
imprimirArbol(arbolPP)

matrizPP = getMatrizRecorrida(arbolPP, filas, columnas)
print(Fore.WHITE + "\n[PP] MATRIZ RECORRIDA:\n")
imprimirMatriz(matrizPP)

solucionPP = getCaminoSolucion(arbolPP)
print(Fore.WHITE + "\n[PP] ÁRBOL SOLUCIÓN:\n")
imprimirArbol(solucionPP)

matrizSolucionPP = getMatrizRecorrida(solucionPP, filas, columnas)
print(Fore.WHITE + "\n[PP] CAMINO SOLUCIÓN:\n")
imprimirMatriz(matrizSolucionPP)

# PA

visitadosPA, pendientesPA = recorrerLabPA(maze)

print("\n" + Fore.WHITE + "[PA] VISITADOS")
for x in visitadosPA:
    print(x)
print("\n" + Fore.WHITE + "[PA] PENDIENTES")
for x in pendientesPA:
    print(x)

arbolPA = crearArbolExpansion(visitadosPA, pendientesPA)
print(Fore.WHITE + "\n[PA] ARBOL DE EXPANSIÓN:\n")
imprimirArbol(arbolPA)

matrizPA = getMatrizRecorrida(arbolPA, filas, columnas)
print(Fore.WHITE + "\n[PA] MATRIZ RECORRIDA:\n")
imprimirMatriz(matrizPA)

solucionPA = getCaminoSolucion(arbolPA)
print(Fore.WHITE + "\n[PA] ÁRBOL SOLUCIÓN:\n")
imprimirArbol(solucionPA)

matrizSolucionPA = getMatrizRecorrida(solucionPA, filas, columnas)
print(Fore.WHITE + "\n[PA] CAMINO SOLUCIÓN:\n")
imprimirMatriz(matrizSolucionPA)

arbolAPng(arbolPP, "expPP.png")
arbolAPng(arbolPA, "expPA.png")