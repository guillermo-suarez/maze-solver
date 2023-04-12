from genlab import maze, printMaze
from pp import crearNodo, recorrerLabPP
from pa import recorrerLabPA
from funciones import imprimirArbol, getMatrizRecorrida, imprimirMatriz, getCaminoSolucion
from colorama import Fore

print("\n" + Fore.WHITE + "LABERINTO A RECORRER:\n")
imprimirMatriz(maze)

print(Fore.WHITE + "--------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

arbolPP = crearNodo(9, 9, 'I', 1)
terminoPP = recorrerLabPP(arbolPP, arbolPP, maze)
print(Fore.WHITE + "PRIMERO EN PROFUNDIDAD:\n")
if not terminoPP:
    print(Fore.WHITE + "¡No tiene solución!\n")
else:
    print(Fore.WHITE + "PP: árbol de expansión\n")
    imprimirArbol(arbolPP)
    print(Fore.WHITE + "PP: matriz recorrida por el algoritmo\n")
    matrizPP = getMatrizRecorrida(arbolPP)
    imprimirMatriz(matrizPP)
    print(Fore.WHITE + "PP: árbol del camino solución\n")
    solucionPP = getCaminoSolucion(arbolPP)
    imprimirArbol(solucionPP)
    print(Fore.WHITE + "PP: matriz recorrida por el árbol del camino solución\n")
    matrizSolucionPP = getMatrizRecorrida(solucionPP)
    imprimirMatriz(matrizSolucionPP)

print(Fore.WHITE + "--------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

arbolPA = crearNodo(9, 9, 'I', 1)
terminoPA = recorrerLabPA(arbolPA, maze)
print(Fore.WHITE + "PRIMERO EN AMPLITUD:\n")
if not terminoPA:
    print(Fore.WHITE + "¡No tiene solución!\n")
else:
    print(Fore.WHITE + "PA: árbol de expansión\n")
    imprimirArbol(arbolPA)
    print(Fore.WHITE + "PA: matriz recorrida por el algoritmo\n")
    matrizPA = getMatrizRecorrida(arbolPA)
    imprimirMatriz(matrizPA)
    print(Fore.WHITE + "PA: árbol del camino solución\n")
    solucionPA = getCaminoSolucion(arbolPA)
    imprimirArbol(solucionPA)
    print(Fore.WHITE + "PA: matriz recorrida por el árbol del camino solución\n")
    matrizSolucionPA = getMatrizRecorrida(solucionPA)
    imprimirMatriz(matrizSolucionPA)