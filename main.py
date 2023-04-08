from genlab import maze
from pp import crearNodo, recorrerLabPP
from funciones import imprimirArbol

raiz = crearNodo(9, 9, 'I', 1)
arbolPP = raiz
recorrerLabPP(arbolPP, raiz, maze)

imprimirArbol(arbolPP)