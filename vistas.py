import PySimpleGUI as sg
from generador import generarLaberintoYArboles
from PIL import Image
import pyautogui

def getScreenSize():
     width, height= pyautogui.size()
     return width, height

def call_vistas():
    sg.theme('DarkGrey2')
    sg.set_options(font=("Calibri", 14))
    window = make_main()
    while True:              
        event, values = window.read() 
        if event == sg.WIN_CLOSED or event == 'Salir':
            break      
        if event == 'Generar laberinto':
            window.close()
            iterPP, iterPA = generarLaberintoYArboles()
            make_windowLaberinto(iterPP, iterPA)
        window.close()

def make_main():    
    layout = [[sg.Text(text = 'Trabajo Práctico Integrador',
                   font=('Calibri', 30),
                   size= 30, 
                   expand_x= True,
                   justification= 'center')],     
            [sg.Text(text = 'Universidad Gastón Dachary - Inteligencia Artificial I - 2023', 
                    font=('Calibri', 15),
                    size= 15, 
                    expand_x= True,
                    justification= 'center')], 
            [sg.Text(' ')],  
            [sg.Text(text = 'Algoritmos de Búsqueda Sistemática', 
                    font=('Calibri', 20),
                    size= 20, 
                    expand_x= True,
                    justification= 'center')], 
            [sg.Text(' ')],  
            [sg.Button(button_text='Generar laberinto',
                        size=(15,2), font=('Calibri')), 
                        sg.Button(button_text='Salir',
                                size=(15,2), font=('Calibri'))],
            [sg.Text(' ')],  
            [sg.Text(text = 'Malazotto, Soledad - Mezio, Santiago - Suárez, Guillermo',
                    font=('Calibri', 10),
                    size= 10, 
                    expand_x= True,
                    justification= 'center')]]
    return sg.Window('TPI Inteligencia Artificial I', layout, element_justification='c')      
    
def make_windowLaberinto(iterPP, iterPA):    
    srcAncho, srcAlto = getScreenSize()   
    layout = [[sg.Text(text ='Laberinto Generado',
                font=('Calibri', 30),
                size= 30, 
                justification= 'center')],
                [sg.Image('IMG-laberinto.png', expand_y=True, key = '-IMAGE-'), sg.Image('IMG-referencias-laberinto.png', expand_y=True, key = '-IMAGE-')],
                [sg.Text(' ')],
                [sg.Text('Recorrer el laberinto mediante el algoritmo:')],
                [sg.Button(button_text='Primero en Profundidad',
                size=(20,2), font=('Calibri')), 
                sg.Button(button_text='Primero en Amplitud', 
                        size=(20,2), font=('Calibri'))],
                [sg.Button(button_text='Generar nuevo laberinto', size=(42,2), font=('Calibri'))]
              ]
    window0 = sg.Window('Laberinto Generado', layout, element_justification='c')
    window  = [window0, None, None, None, None, None, None]
    active  = [True, False, False, False, False, False, False]
    event   = [None, None, None, None, None, None, None]
    values  = [None, None, None, None, None, None, None]
    #0=ventana laberinto, 1=PPArbol, 2=PAArbol, 3=IterPP, 4=IterPA, 5=LabSolPP, 6=LabSolPA
    while True:
        for i in range(7):            
            if active[i] and window[i] != None:
                event[i], values[i] = window[i].read(timeout=50)
                if event[i] == sg.WIN_CLOSED or event == 'Salir':
                    if i == 0:
                        active[i] = False
                        window[i].close()
                        break
                    else:
                        if i == 1:
                            if active[3]:
                                active[3] = False
                                window[3].close()
                            if active[5]:
                                active[5] = False
                                window[5].close()
                        if i == 2:
                            if active[4]:
                                active[4] = False
                                window[4].close()
                            if active[6]:
                                active[6] = False
                                window[6].close()
                        active[i] = False
                        window[i].close()
                elif event[i] == 'Primero en Profundidad' and not active[1]:      
                    im = Image.open('IMG-PP-arbol-expansion.png')
                    imgAncho, imgAlto = im.size
                    ancho, alto = imgAncho, imgAlto
                    if(imgAncho > srcAncho):
                        ancho = srcAncho - 15
                        alto = alto + 55
                    if(imgAlto > srcAlto):
                        alto = srcAlto - 75
                        ancho = ancho + 55    
                    window[1] = sg.Window("Árbol de expansión", layoutArbol('PP'),
                             finalize=True, location=(int((srcAncho-ancho)/2),0), size=(ancho, alto),  element_justification='c')                    
                    active[1] = True
                elif event[i] == 'Primero en Amplitud' and not active[2]:
                    im = Image.open('IMG-PA-arbol-expansion.png')
                    imgAncho, imgAlto = im.size
                    ancho, alto = imgAncho, imgAlto
                    if(imgAncho > srcAncho):
                        ancho = srcAncho - 15
                        alto = alto + 55
                    if(imgAlto > srcAlto):
                        alto = srcAlto - 75
                        ancho = ancho + 55
                    window[2] = sg.Window("Árbol de expansión", layoutArbol('PA'), size=(ancho, alto),
                    finalize=True, location=(int((srcAncho-ancho)/2),0),  element_justification='c')
                    active[2] = True
                elif event[i] == 'Ver laberinto recorrido':                    
                    if i == 1 and not active[5]:
                        active[5] = True
                        window[5] = sg.Window("Laberinto recorrido", layoutLaberinto('PP'),
                             finalize=True, location=(0,0),  element_justification='c')
                    if i == 2 and not active[6]:
                        active[6] = True
                        window[6] = sg.Window("Laberinto recorrido", layoutLaberinto('PA'),
                             finalize=True, location=(0,0),  element_justification='c')    
                elif event[i] == 'Ver iteraciones':
                    if i == 1:
                        if not active[3]:    
                            active[3] = True
                            window[3] = sg.Window("Iteraciones", layoutIteracion(iterPP, 'PP'),
                                finalize=True, resizable=False, margins=(0,0), location=(7,0),  element_justification='c', size=(srcAncho - 15, srcAlto - 75))  
                    if i == 2:
                        if not active[4]:
                            active[4] = True
                            window[4] = sg.Window("Iteraciones", layoutIteracion(iterPA, 'PA'),
                                finalize=True, resizable=False, margins=(0,0), location=(7,0),  element_justification='c', size=(srcAncho - 15, srcAlto - 75))  
                elif event[i] == 'Generar nuevo laberinto':  
                    for j in range (1, 7):
                        if active[j]:
                            window[j].close()
                            active[j] = False
                    generarLaberintoYArboles()
                    window[0]['-IMAGE-'].update('IMG-laberinto.png')
                if i == 0 and active[i] == 0:
                    break
        if i == 0 and active[i] == 0:
            break
    window0.close()

def layoutIteracion(iteraciones, tipo):

    superscript = str.maketrans("()0123456789", "⁽⁾⁰¹²³⁴⁵⁶⁷⁸⁹")
    subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

    filas = len(iteraciones)
    columnas = 0

    cabeceras = []

    for iter in iteraciones:
        if len(iter) > columnas:
            columnas = len(iter)

    cabeceras.append('t')
    for i in range(0, columnas):
        cabeceras.append(str(i))

    valores = []
    i = 0
    for iter in iteraciones:
        fila = []
        fila.append("t" + str(i).translate(subscript))
        i = i + 1
        for est in iter:
            if est.padre:
                fila.append("(" + str(est.x) + ", " + str(est.y) + ") "  + "(".translate(superscript) + str(est.padre.x).translate(superscript) + "⋅ " + str(est.padre.y).translate(superscript) + ")".translate(superscript))
            else:
                fila.append("(" + str(est.x) + ", " + str(est.y) + ")")
        valores.append(list(fila))
    txt = ''    
    if tipo == 'PP':
        txt = 'Realizadas en el algoritmo Primero en Profundidad'
    else:
        txt = 'Realizadas en el algoritmo Primero en Amplitud'
    layout = [[sg.Text(text='Iteraciones', font=('Calibri', 30), 
                justification= 'center')],
                [sg.Text(text=txt, font=('Calibri', 20), 
                justification= 'center')],
                [sg.Table(values = valores, 
                          headings = cabeceras,
                          vertical_scroll_only = False,
                          enable_events = False,
                          expand_x=True,
                          expand_y=True,
                          justification= 'center',
                          auto_size_columns=True,
                          col_widths=6)]]
    return layout

def layoutLaberinto(tipo):
    if tipo == 'PP':
        txt = 'Aplicando Primero en Profundidad'
    else:
        txt = 'Aplicando Primero en Amplitud'
    layout = [[sg.Text(text='Laberinto Recorrido', font=('Calibri', 25), expand_x= True, justification= 'center')],   
              [sg.Text(text=txt, font=('Calibri', 20), expand_x= True, justification= 'center')],  
            [sg.Image(filename = 'IMG-' + tipo + '-laberinto-solucion.png', key='Image'), sg.Image('IMG-referencias-laberinto-completo.png', expand_y=True, key = '-IMAGE-')]]
    return layout

def layoutArbol(tipo):
    path = 'IMG-' + tipo + '-arbol-expansion.png'
    column = [[sg.Image(filename=path, key='Image')]]
    im = Image.open(path)
    imgAncho, imgAlto = im.size
    srcAncho, srcAlto = getScreenSize()
    scrollVertical = False
    scrollHorizontal = False
    if(imgAncho > srcAncho):
        scrollHorizontal = True
    if(imgAlto > srcAlto):
        scrollVertical = True
    if tipo == 'PP':
        txt = 'Expandido mediante el algoritmo de Primero en Profundidad'
    else:
        txt = 'Expandido mediante el algoritmo de Primero en Amplitud'
    layout = [[sg.Text(text='Árbol de expansión', font=('Calibri', 30), expand_x= True, justification= 'center')],
              [sg.Text(text=txt, font=('Calibri', 20), expand_x= True, justification= 'center')],
              [sg.Button(button_text= 'Ver laberinto recorrido', size=(15,2), font=('Calibri'), enable_events=True), sg.Button(button_text= 'Ver iteraciones', size=(15,2), font=('Calibri'), enable_events=True)],
              [sg.Column(column, scrollable = (scrollVertical or scrollHorizontal), vertical_scroll_only = not scrollHorizontal, key='Column')]]
    return layout
