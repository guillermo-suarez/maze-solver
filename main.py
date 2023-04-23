from genlab import maze
from colorama import Fore
from funciones import imprimirMatriz, crearArbolExpansion, imprimirArbol, getMatrizRecorrida, getCaminoSolucion
from pp import busquedaPP

print("\n" + Fore.WHITE + "LABERINTO A RECORRER:\n")
imprimirMatriz(maze)

visitados, pendientes = busquedaPP(maze)

print("\n" + Fore.WHITE + "VISITADOS")
for x in visitados:
    print(x)
print("\n" + Fore.WHITE + "PENDIENTES")
for x in pendientes:
    print(x)

arbolPP = crearArbolExpansion(visitados, pendientes)
print("\nARBOL DE EXPANSIÓN:\n")
imprimirArbol(arbolPP)

matriz = getMatrizRecorrida(arbolPP)
print("\nMATRIZ RECORRIDA:\n")
imprimirMatriz(matriz)

solucion = getCaminoSolucion(arbolPP)
imprimirArbol(solucion)

matrizSolucion = getMatrizRecorrida(solucion)
imprimirMatriz(matrizSolucion)