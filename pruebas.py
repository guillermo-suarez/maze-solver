from genlab import getMaze
from pp import recorrerLabPP
from pa import recorrerLabPA
from funciones import crearArbolExpansion
from anytree import Node, LevelOrderIter
import time

def pruebaTiempo():
    #Procedimiento que registra el tiempo promedio de los algoritmos PP y PA recorriendo una matriz simétrica
    filas = columnas = 10
    rango = 10000
    acumuladoPP = acumuladoPA = promedioPP = promedioPA = 0
    inicio = fin = inicioBucle = finBucle = 0.0
    
    inicioBucle = time.time()
    for i in range(rango):
        #print("Vuelta ", i)
        laberinto = getMaze(filas, columnas)
        inicio = time.time()
        recorrerLabPP(laberinto)
        fin = time.time()
        acumuladoPP += fin-inicio
        inicio = time.time()
        recorrerLabPA(laberinto)
        fin = time.time()
        acumuladoPA += fin-inicio
    finBucle = time.time()

    promedioPP = acumuladoPP / rango
    promedioPA = acumuladoPA / rango

    print('Duración del bucle: ', finBucle - inicioBucle)
    print('Promedio primero en profundidad: ', promedioPP)
    print('Promedio primero en amplitud: ', promedioPA)

def pruebaOptimo():
    #Procedimiento que busca probar si PP y PA encuentran la misma salida
    laberinto = [
        ['F','0','0','0','0','0','0','0','0','0'],
        ['X','X','X','X','X','X','X','X','X','0'],
        ['X','X','X','X','X','X','X','X','X','0'],
        ['X','X','X','X','X','X','X','X','X','0'],
        ['X','X','X','X','X','X','X','X','X','0'],
        ['X','X','X','X','X','X','X','X','X','0'],
        ['X','X','X','X','X','X','X','X','X','0'],
        ['X','X','X','X','X','X','X','X','X','0'],
        ['X','X','X','X','X','X','X','X','X','0'],
        ['X','X','X','X','X','X','X','F','0','I']
    ]
    visitadosPP, pendientesPP = recorrerLabPP(laberinto)
    visitadosPA, pendientesPA = recorrerLabPA(laberinto)
    arbolPP = crearArbolExpansion(visitadosPP, pendientesPP)
    arbolPA = crearArbolExpansion(visitadosPA, pendientesPA)
    for nodo in LevelOrderIter(arbolPP):
        if nodo.est == 'F':
            print('Primero en profundidad')
            print('La salida fue en la casilla [',nodo.cordX,'][',nodo.cordY,']')
            print('La profundidad del árbol es de',nodo.depth)
    for nodo in LevelOrderIter(arbolPA):
        if nodo.est == 'F':
            print('Primero en amplitud')
            print('La salida fue en la casilla [',nodo.cordX,'][',nodo.cordY,']')
            print('La profundidad del árbol es de',nodo.depth)

pruebaOptimo()