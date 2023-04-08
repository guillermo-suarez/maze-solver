from genlab import maze
from pp import crearNodo, recorrerLabPP
from funciones import imprimirArbol
from colorama import Fore

raiz = crearNodo(9, 9, 'I', 1)

arbolPP = raiz
termino = recorrerLabPP(arbolPP, raiz, maze)
print(Fore.WHITE + "PRIMERO EN PROFUNDIDAD:\n")
imprimirArbol(arbolPP)
if not termino:
    print(Fore.WHITE + "¡No tiene solución!")