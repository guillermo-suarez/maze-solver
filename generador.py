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
    laberintoAPng(laberinto, filas, columnas, "lab.png")
    arbolAPng(arbolPP, "PP-arbol-exp.png")
    laberintoAPng(labPP, filas, columnas, "PP-lab-solucion.png")
    arbolAPng(arbolPA, "PA-arbol-exp.png")
    laberintoAPng(labPA, filas, columnas, "PA-lab-solucion.png")
    crearReferenciasLaberintos()

    return iterPP, iterPA
