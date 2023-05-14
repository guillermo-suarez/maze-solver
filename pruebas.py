from genlab import getMaze
from pp import recorrerLabPP
from pa import recorrerLabPA
from funciones import crearArbolExpansion
from anytree import LevelOrderIter
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
        ['X','X','X','X','X','X','X','0','F','I']
    ]
    visitadosPP, pendientesPP = recorrerLabPP(laberinto)
    visitadosPA, pendientesPA = recorrerLabPA(laberinto)
    arbolPP = crearArbolExpansion(visitadosPP, pendientesPP)
    arbolPA = crearArbolExpansion(visitadosPA, pendientesPA)
    print('Primero en profundidad')
    for nodo in LevelOrderIter(arbolPP):
        if nodo.est == 'F':
            print('\tLa salida de la casilla [',nodo.cordX,'][',nodo.cordY,'] fue encontrada.')
            print('\tLa profundidad del árbol allí es de',nodo.depth)
    print('Primero en amplitud')
    for nodo in LevelOrderIter(arbolPA):
        if nodo.est == 'F':
            print('\tLa salida de la casilla [',nodo.cordX,'][',nodo.cordY,'] fue encontrada.')
            print('\tLa profundidad del árbol allí es de',nodo.depth)


def pruebaEspacio():
    #Procedimiento que busca factor de ramificación y profundidad máxima de PP y PA
    filas = columnas = 10
    rango = 10000
    bMaxPP = bMaxPA = 0 #Factor de ramificación máximo de todos los laberintos
    dMaxPP = dMaxPA = 0 #Profundidad de la salida del árbol con el bMax
    encontrado = False

    for i in range(rango):
        #print("Vuelta ", i)
        laberinto = getMaze(filas, columnas)
        visitadosPP, pendientesPP = recorrerLabPP(laberinto)
        visitadosPA, pendientesPA = recorrerLabPA(laberinto)
        arbolPP = crearArbolExpansion(visitadosPP, pendientesPP)
        arbolPA = crearArbolExpansion(visitadosPA, pendientesPA)
        for nodo in LevelOrderIter(arbolPP):
            if len(nodo.children) > bMaxPP:
                bMaxPP = len(nodo.children)
                encontrado = True
            if nodo.est == 'F' and encontrado:
                dMaxPP = nodo.depth
                encontrado = False
        for nodo in LevelOrderIter(arbolPA):
            if len(nodo.children) > bMaxPA:
                bMaxPA = len(nodo.children)
                encontrado = True
            if nodo.est == 'F' and encontrado:
                dMaxPA = nodo.depth
                encontrado = False
    print('Prueba de',rango,'laberintos')
    print('Primero en profundidad:')
    print('\tbMax = ',bMaxPP)
    print('\tdMax = ',dMaxPP)
    print('Primero en amplitud:')
    print('\tbMax = ',bMaxPA)
    print('\tdMax = ',dMaxPA)
    if bMaxPP == bMaxPP and dMaxPP == dMaxPA:
        print('Ambos algoritmos poseen la misma complejidad')
    else:
        print('La complejidad máxima de primero en profundidad es de', bMaxPP**dMaxPP)
        print('La complejidad máxima de primero en amplitud es de', bMaxPA**dMaxPA)


def pruebaCantNodos():
    filas = columnas = 10
    rango = 10000
    acumuladoPP = acumuladoPA = promedioPP = promedioPA = 0
    idMax = 0

    for i in range(rango):
        #print("Vuelta ", i)
        laberinto = getMaze(filas, columnas)
        visitadosPP, pendientesPP = recorrerLabPP(laberinto)
        visitadosPA, pendientesPA = recorrerLabPA(laberinto)
        arbolPP = crearArbolExpansion(visitadosPP, pendientesPP)
        arbolPA = crearArbolExpansion(visitadosPA, pendientesPA)
        for nodo in arbolPP.leaves:
            if nodo.id > idMax:
                idMax = nodo.id
        acumuladoPP += idMax
        idMax = 0
        for nodo in arbolPA.leaves:
            if nodo.id > idMax:
                idMax = nodo.id
        acumuladoPA += idMax
        idMax = 0
    
    promedioPP = acumuladoPP // rango
    promedioPA = acumuladoPA // rango

    print('Cantidad de nodos promedio:')
    print('\tPrimero en profundidad: ', promedioPP)
    print('\tPrimero en amplitud: ', promedioPA)