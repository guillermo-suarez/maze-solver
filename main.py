from genlab import getMaze
from colorama import Fore
from funciones import imprimirMatriz, crearArbolExpansion, imprimirArbol, getMatrizRecorrida, getCaminoSolucion, arbolAPng
from pp import recorrerLabPP
from pa import recorrerLabPA
import PySimpleGUI as sg

filas = 10
columnas = 10

laberinto = getMaze(filas, columnas)

print("\n" + Fore.WHITE + "LABERINTO A RECORRER:\n")
imprimirMatriz(laberinto)

# PP

visitadosPP, pendientesPP = recorrerLabPP(laberinto)

print("\n" + Fore.WHITE + "[PP] VISITADOS")
for x in visitadosPP:
    print(x)
print("\n" + Fore.WHITE + "[PP] PENDIENTES")
for x in pendientesPP:
    print(x)

arbolPP = crearArbolExpansion(visitadosPP, pendientesPP)
print(Fore.WHITE + "[PP] ÁRBOL DE EXPANSIÓN:\n")
imprimirArbol(arbolPP)

matrizPP = getMatrizRecorrida(arbolPP, filas, columnas)
print(Fore.WHITE + "\n[PP] MATRIZ RECORRIDA:\n")
imprimirMatriz(matrizPP)

solucionPP = getCaminoSolucion(arbolPP)
print(Fore.WHITE + "\n[PP] ÁRBOL SOLUCIÓN:\n")
imprimirArbol(solucionPP)

matrizSolucionPP = getMatrizRecorrida(solucionPP, filas, columnas)
print(Fore.WHITE + "\n[PP] CAMINO SOLUCIÓN:\n")
imprimirMatriz(matrizSolucionPP)

# PA

visitadosPA, pendientesPA = recorrerLabPA(laberinto)

print("\n" + Fore.WHITE + "[PA] VISITADOS")
for x in visitadosPA:
    print(x)
print("\n" + Fore.WHITE + "[PA] PENDIENTES")
for x in pendientesPA:
    print(x)

arbolPA = crearArbolExpansion(visitadosPA, pendientesPA)
print(Fore.WHITE + "\n[PA] ARBOL DE EXPANSIÓN:\n")
imprimirArbol(arbolPA)

matrizPA = getMatrizRecorrida(arbolPA, filas, columnas)
print(Fore.WHITE + "\n[PA] MATRIZ RECORRIDA:\n")
imprimirMatriz(matrizPA)

solucionPA = getCaminoSolucion(arbolPA)
print(Fore.WHITE + "\n[PA] ÁRBOL SOLUCIÓN:\n")
imprimirArbol(solucionPA)

matrizSolucionPA = getMatrizRecorrida(solucionPA, filas, columnas)
print(Fore.WHITE + "\n[PA] CAMINO SOLUCIÓN:\n")
imprimirMatriz(matrizSolucionPA)

arbolAPng(arbolPP, "expPP.png")
arbolAPng(arbolPA, "expPA.png")

sg.theme("DarkAmber")

sg.set_options(window_location = (0,0))

img1 = [[sg.Image(source = "expPP.png")]]
layout1 = [[sg.Text("HOLA", background_color = "white")], [sg.Column(img1, scrollable = True)]]
ventana1 = sg.Window("Árbol de expansión PP", layout1, size = (int(0.9 * 1920), int(0.9 * 1080)), margins = (0, 0), finalize = True)
ventana1.maximize()

# img2 = [[sg.Image(source = "expPA.png")]]
# layout2 = [[sg.Column(img2, size = (1920, 1080), scrollable = True)]]
# ventana2 = sg.Window("Árbol PA", layout2, finalize = True)

while True:
    ventana, evento, valores = sg.read_all_windows()
    if ventana == sg.WIN_CLOSED:
        break
    if evento == sg.WIN_CLOSED:
        ventana.close()

# ventana1.close()
# ventana2.close()