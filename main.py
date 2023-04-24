from genlab import maze
from colorama import Fore
import dibujarArbol as draw

arbolPP = crearNodo(9, 9, 'I', 1)
terminoPP = recorrerLabPP(arbolPP, arbolPP, maze)
print(Fore.WHITE + "PRIMERO EN PROFUNDIDAD:\n")
if not terminoPP:
    print(Fore.WHITE + "¡No tiene solución!")
else:
    imprimirArbol(arbolPP)
    draw.dibujarArbol(arbolPP)


arbolPA = crearNodo(9, 9, 'I', 1)
terminoPA = recorrerLabPA(arbolPA, maze)
print(Fore.WHITE + "PRIMERO EN AMPLITUD:\n")
if not terminoPA:
    print(Fore.WHITE + "¡No tiene solución!")
else:
    imprimirArbol(arbolPA)
    draw.dibujarArbol(arbolPA)