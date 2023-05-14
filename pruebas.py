from genlab import getMaze
from pp import recorrerLabPP
from pa import recorrerLabPA
from funciones import crearArbolExpansion, imprimirArbol, imprimirMatriz
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

def pruebaEspacio():
    filas = columnas = 10
    rango = 10000
    bMaxPP = bMaxPA = 0 #Factor de ramificación máximo de todos los laberintos
    dMaxPP = dMaxPA = 0 #Profundidad de la salida del árbol con el bMax
    encontrado = False

    for i in range(rango):
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
    print('\tPrimero en profundidad:')
    print('\t\tbMax = ',bMaxPP)
    print('\t\tdMax = ',dMaxPP)
    print('\tPrimero en amplitud:')
    print('\t\tbMax = ',bMaxPA)
    print('\t\tdMax = ',dMaxPA)
    if bMaxPP == bMaxPP and dMaxPP == dMaxPA:
        print('Ambos algoritmos poseen la misma complejidad')
    else:
        print('La complejidad máxima de primero en profundidad es de', bMaxPP**dMaxPP)
        print('La complejidad máxima de primero en amplitud es de', bMaxPA**dMaxPA)


