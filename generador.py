from genlab import getMaze
from funciones import crearArbolExpansion, arbolAPng, laberintoAPng, marcarCaminoSolucion, crearReferenciasLaberintos
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
    laberintoAPng(laberinto, filas, columnas, "IMG-laberinto.png")
    arbolAPng(arbolPP, "IMG-PP-arbol-expansion.png")
    laberintoAPng(labPP, filas, columnas, "IMG-PP-laberinto-solucion.png")
    arbolAPng(arbolPA, "IMG-PA-arbol-expansion.png")
    laberintoAPng(labPA, filas, columnas, "IMG-PA-laberinto-solucion.png")
    crearReferenciasLaberintos()

    return iterPP, iterPA
