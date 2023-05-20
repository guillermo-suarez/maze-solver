from genlab import getMaze
from colorama import Fore
from funciones import imprimirMatriz, crearArbolExpansion, imprimirArbol, getMatrizRecorrida, getCaminoSolucion, arbolAPng, laberintoAPng, marcarCaminoSolucion
from pp import recorrerLabPP
from pa import recorrerLabPA
from ventanas import crearVentanaArbol

import PySimpleGUI as sg

filas = 10
columnas = 10

laberinto = getMaze(filas, columnas)

# Al descomentar esta línea nos aseguramos que el laberinto no tenga solución
# laberinto[0][1] = 'X'

print("\n" + Fore.WHITE + "LABERINTO A RECORRER:\n")
imprimirMatriz(laberinto)

# PP

visitadosPP, pendientesPP = recorrerLabPP(laberinto)

# print("\n" + Fore.WHITE + "[PP] VISITADOS")
# for x in visitadosPP:
#     print(x)
# print("\n" + Fore.WHITE + "[PP] PENDIENTES")
# for x in pendientesPP:
#     print(x)

arbolPP = crearArbolExpansion(visitadosPP, pendientesPP)
print(Fore.WHITE + "[PP] ÁRBOL DE EXPANSIÓN:\n")
imprimirArbol(arbolPP)

getCaminoSolucion(arbolPP)

matrizPP = getMatrizRecorrida(arbolPP, filas, columnas)
print(Fore.WHITE + "\n[PP] MATRIZ RECORRIDA:\n")
imprimirMatriz(matrizPP)

labPP = marcarCaminoSolucion(laberinto, arbolPP)
print(Fore.WHITE + "\n[PP] MATRIZ SOLUCIÓN:\n")
imprimirMatriz(labPP)

# PA

print("\n" + Fore.WHITE + "LABERINTO A RECORRER:\n")
imprimirMatriz(laberinto)

visitadosPA, pendientesPA = recorrerLabPA(laberinto)

# print("\n" + Fore.WHITE + "[PA] VISITADOS")
# for x in visitadosPA:
#     print(x)
# print("\n" + Fore.WHITE + "[PA] PENDIENTES")
# for x in pendientesPA:
#     print(x)

arbolPA = crearArbolExpansion(visitadosPA, pendientesPA)
print(Fore.WHITE + "\n[PA] ARBOL DE EXPANSIÓN:\n")
imprimirArbol(arbolPA)

getCaminoSolucion(arbolPA)

matrizPA = getMatrizRecorrida(arbolPA, filas, columnas)
print(Fore.WHITE + "\n[PA] MATRIZ RECORRIDA:\n")
imprimirMatriz(matrizPA)

labPA = marcarCaminoSolucion(laberinto, arbolPA)
print(Fore.WHITE + "\n[PA] MATRIZ SOLUCIÓN:\n")
imprimirMatriz(labPA)

# Crear PNGs necesarios

laberintoAPng(laberinto, filas, columnas, "lab.png")

arbolAPng(arbolPP, "expPP.png")
laberintoAPng(matrizPP, filas, columnas, "labPP.png")
laberintoAPng(labPP, filas, columnas, "labPPSolucion.png")

arbolAPng(arbolPA, "expPA.png")
laberintoAPng(matrizPA, filas, columnas, "labPA.png")
laberintoAPng(labPA, filas, columnas, "labPASolucion.png")

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