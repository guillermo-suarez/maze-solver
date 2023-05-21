from genlab import getMaze
from funciones import crearArbolExpansion, arbolAPng, laberintoAPng, marcarCaminoSolucion, iteracionesAPng
from pp import recorrerLabPP
from pa import recorrerLabPA



def generarLaberintoYArboles():
    filas = 10
    columnas = 10
    laberinto = getMaze(filas, columnas)
    iterPP, visitadosPP, pendientesPP = recorrerLabPP(laberinto)
    arbolPP = crearArbolExpansion(visitadosPP, pendientesPP)
    labPP = marcarCaminoSolucion(laberinto, arbolPP)
    iterPA, visitadosPA, pendientesPA = recorrerLabPA(laberinto)
    arbolPA = crearArbolExpansion(visitadosPA, pendientesPA)
    labPA = marcarCaminoSolucion(laberinto, arbolPA)
    laberintoAPng(laberinto, filas, columnas, "lab.png")
    arbolAPng(arbolPP, "PP-arbol-exp.png")
    laberintoAPng(labPP, filas, columnas, "PP-lab-solucion.png")
    arbolAPng(arbolPA, "PA-arbol-exp.png")
    laberintoAPng(labPA, filas, columnas, "PA-lab-solucion.png")
    return iterPP, iterPA

def generarIteraciones(tipo, iter):    
    if tipo == 'PP':
        iteracionesAPng(iter, "PP-tabla-iteraciones.png")
    else:
        iteracionesAPng(iter, "PA-tabla-iteraciones.png")
