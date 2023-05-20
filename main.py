from genlab import getMaze
from colorama import Fore
from funciones import imprimirMatriz, crearArbolExpansion, imprimirArbol, getMatrizRecorrida, getCaminoSolucion, arbolAPng, laberintoAPng, marcarCaminoSolucion, iteracionesAPng
from pp import recorrerLabPP
from pa import recorrerLabPA
from ventanas import crearVentanaArbol

import PySimpleGUI as sg
import matplotlib.pyplot as plt

filas = 10
columnas = 10

laberinto = getMaze(filas, columnas)

# Al descomentar esta línea nos aseguramos que el laberinto no tenga solución
# laberinto[0][1] = 'X'

# print("\n" + Fore.WHITE + "LABERINTO A RECORRER:\n")
# imprimirMatriz(laberinto)

# PP

iterPP, visitadosPP, pendientesPP = recorrerLabPP(laberinto)
arbolPP = crearArbolExpansion(visitadosPP, pendientesPP)
# matrizPP = getMatrizRecorrida(arbolPP, filas, columnas)
# solucionPP = getCaminoSolucion(arbolPP)
# matrizSolucionPP = getMatrizRecorrida(solucionPP, filas, columnas)
labPP = marcarCaminoSolucion(laberinto, arbolPP)

# print("\n" + Fore.WHITE + "[PP] VISITADOS")
# for x in visitadosPP:
#     print(x)
# print("\n" + Fore.WHITE + "[PP] PENDIENTES")
# for x in pendientesPP:
#     print(x)
# print(Fore.WHITE + "[PP] ÁRBOL DE EXPANSIÓN:\n")
# imprimirArbol(arbolPP)
# print(Fore.WHITE + "\n[PP] MATRIZ RECORRIDA:\n")
# imprimirMatriz(matrizPP)
# print(Fore.WHITE + "\n[PP] ÁRBOL SOLUCIÓN:\n")
# imprimirArbol(solucionPP)
# print(Fore.WHITE + "\n[PP] CAMINO SOLUCIÓN:\n")
# imprimirMatriz(matrizSolucionPP)
# print(Fore.WHITE + "\n[PP] MATRIZ SOLUCIÓN:\n")
# imprimirMatriz(labPP)

# PA

iterPA, visitadosPA, pendientesPA = recorrerLabPA(laberinto)
arbolPA = crearArbolExpansion(visitadosPA, pendientesPA)
# matrizPA = getMatrizRecorrida(arbolPA, filas, columnas)
# solucionPP = getCaminoSolucion(arbolPA)
# matrizSolucionPA = getMatrizRecorrida(solucionPP, filas, columnas)
labPA = marcarCaminoSolucion(laberinto, arbolPA)

# print("\n" + Fore.WHITE + "[PA] VISITADOS")
# for x in visitadosPA:
#     print(x)
# print("\n" + Fore.WHITE + "[PA] PENDIENTES")
# for x in pendientesPA:
#     print(x)
# print(Fore.WHITE + "\n[PA] ARBOL DE EXPANSIÓN:\n")
# imprimirArbol(arbolPA)
# print(Fore.WHITE + "\n[PA] MATRIZ RECORRIDA:\n")
# imprimirMatriz(matrizPA)
# print(Fore.WHITE + "\n[PA] ÁRBOL SOLUCIÓN:\n")
# imprimirArbol(solucionPA)
# print(Fore.WHITE + "\n[PA] CAMINO SOLUCIÓN:\n")
# imprimirMatriz(matrizSolucionPA)
# print(Fore.WHITE + "\n[PA] MATRIZ SOLUCIÓN:\n")
# imprimirMatriz(labPA)

# Crear PNGs necesarios

laberintoAPng(laberinto, filas, columnas, "lab.png")

arbolAPng(arbolPP, "PP-arbol-exp.png")
# laberintoAPng(matrizPP, filas, columnas, "img/labPP.png")
laberintoAPng(labPP, filas, columnas, "PP-lab-solucion.png")
iteracionesAPng(iterPP, "PP-tabla-iteraciones.png")

arbolAPng(arbolPA, "PA-arbol-exp.png")
# laberintoAPng(matrizPA, filas, columnas, "img/labPA.png")
laberintoAPng(labPA, filas, columnas, "PA-lab-solucion.png")
iteracionesAPng(iterPA, "PA-tabla-iteraciones.png")

# ventanaPP = crearVentanaArbol("expPP.png", "PP")
# ventanaPA = crearVentanaArbol("expPA.png", "PA")

# while True:
#     ventana, evento, valor = sg.read_all_windows()
#     if evento == sg.WIN_CLOSED:
#         if ventana == ventanaPP:
#             ventanaPP.close()
#             ventanaPP = None
#             if ventanaPA == None:
#                 break
#         elif ventana == ventanaPA:
#             ventanaPA.close()
#             ventanaPA = None
#             if ventanaPP == None:
#                 break