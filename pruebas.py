from genlab import getMaze, printMaze
from pp import recorrerLabPP
from pa import recorrerLabPA
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

pruebaTiempo()