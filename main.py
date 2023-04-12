from genlab import maze, printMaze
from pp import crearNodo, recorrerLabPP
from pa import recorrerLabPA
from funciones import imprimirArbol, crearMatrizRecorrida, imprimirMatriz
from colorama import Fore

print("\n" + Fore.WHITE + "LABERINTO A RECORRER:\n")
imprimirMatriz(maze)

arbolPP = crearNodo(9, 9, 'I', 1)
terminoPP = recorrerLabPP(arbolPP, arbolPP, maze)
print(Fore.WHITE + "PRIMERO EN PROFUNDIDAD:\n")
if not terminoPP:
    print(Fore.WHITE + "¡No tiene solución!")
else:
    imprimirArbol(arbolPP)

arbolPA = crearNodo(9, 9, 'I', 1)
terminoPA = recorrerLabPA(arbolPA, maze)
print(Fore.WHITE + "PRIMERO EN AMPLITUD:\n")
if not terminoPA:
    print(Fore.WHITE + "¡No tiene solución!")
else:
    imprimirArbol(arbolPA)