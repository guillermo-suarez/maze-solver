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
          [sg.Text(' ')],  
          [sg.Text(text = 'Algoritmos de búsqueda', 
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
          [sg.Text(' ')],  
          [sg.Text(text = 'Malazotto, Soledad - Mezio, Santiago - Suárez, Guillermo',
                   font=('Calibri', 10),
                   size= 10, 
                   expand_x= True,
                   justification= 'center')]]
    return sg.Window('maze-solver', layout, size=(715,300), element_justification='c')      
    
def make_windowLaberinto(iterPP, iterPA):    
    srcAncho, srcAlto = getScreenSize()   
    layout = [[sg.Text(text ='Laberinto',
                font=('Calibri', 30),
                size= 30, 
                expand_x= True,
                justification= 'center')],
                [sg.Image('lab.png', expand_x=True, expand_y=True, key = '-IMAGE-')],
                [sg.Text(text='Referencias', font=('Calibri', 20), 
                size= 30, 
                expand_x= True,
                justification= 'center')],
                [sg.Image('refLab.png', expand_x=True, expand_y=True, key = '-IMAGE-')],
                [sg.Text(' ')],
                [sg.Button(button_text='Resolver por PP',
                size=(15,2), font=('Calibri')), 
                sg.Button(button_text='Resolver por PA', 
                        size=(15,2), font=('Calibri'))],
                [sg.Button(button_text='Generar nuevo laberinto', size=(32,2), font=('Calibri'))]                
              ]
    im = Image.open('lab.png')
    imAncho, imAlto = im.size    
    print(imAlto)
    im2 =  Image.open('refLab.png')
    im2Ancho, im2Alto = im2.size  
    print(im2Alto)
    altoAux = srcAlto - (imAlto + im2Alto)  
    print (altoAux)
    alto = int(imAlto + im2Alto + (altoAux/2))
    print(alto)
    window0= sg.Window('Laberinto', layout, element_justification='c', size=(imAncho+35,alto))
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
                elif event[i] == 'Resolver por PP' and not active[1]:      
                    im = Image.open('PP-arbol-exp.png')
                    imgAncho, imgAlto = im.size
                    imgAncho = imgAncho+35         
                    if(imgAncho>srcAncho):
                        ancho = srcAncho - 15
                    else:
                        ancho = imgAncho
                    alto= srcAlto - 75     
                    window[1] = sg.Window("Árbol PP", layoutArbol('PP'),
                             finalize=True, location=(int((srcAncho-ancho)/2),0), size=(ancho, alto),  element_justification='c')                    
                    active[1] = True
                elif event[i] == 'Resolver por PA' and not active[2]:
                    im = Image.open('PA-arbol-exp.png')
                    imgAncho, imgAlto = im.size
                    imgAncho = imgAncho+35         
                    if(imgAncho>srcAncho):
                        ancho = srcAncho - 15
                    else:
                        ancho = imgAncho
                    alto= srcAlto - 75     
                    window[2] = sg.Window("Árbol PA", layoutArbol('PA'), size=(ancho, alto),
                    finalize=True, location=(int((srcAncho-ancho)/2),0),  element_justification='c')
                    active[2] = True
                elif event[i] == 'Ver laberinto recorrido':                    
                    if i == 1 and not active[5]:
                        active[5] = True
                        window[5] = sg.Window("Laberinto solución PP", layoutLaberinto('PP'),
                             finalize=True, location=(0,0),  element_justification='c')
                    if i == 2 and not active[6]:
                        active[6] = True
                        window[6] = sg.Window("Laberinto solución PA", layoutLaberinto('PA'),
                             finalize=True, location=(0,0),  element_justification='c')    
                elif event[i] == 'Ver iteraciones':
                    if i == 1:
                        if not active[3]:    
                            active[3] = True
                            window[3] = sg.Window("Iteraciones PP", layoutIteracion(iterPP, 'PP'),
                                finalize=True, resizable=False, margins=(0,0), location=(7,0),  element_justification='c', size=(srcAncho - 15, srcAlto - 75))  
                    if i == 2:
                        if not active[4]:
                            active[4] = True
                            window[4] = sg.Window("Iteraciones PA", layoutIteracion(iterPA, 'PA'),
                                finalize=True, resizable=False, margins=(0,0), location=(7,0),  element_justification='c', size=(srcAncho - 15, srcAlto - 75))  
                elif event[i] == 'Generar nuevo laberinto':  
                    for j in range (1, 7):
                        if active[j]:
                            window[j].close()
                            active[j] = False
                    generarLaberintoYArboles()
                    window[0]['-IMAGE-'].update('lab.png')
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
        
    layout = [[sg.Text(text='Iteraciones ' + tipo, font=('Calibri', 30), 
                size= 30,
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
    layout = [
    [sg.Text(text='Laberinto Recorrido ' + tipo, font=('Calibri', 30), 
                size= 30, 
                expand_x= True,
                justification= 'center')],    
    [sg.Image(filename=tipo+'-lab-solucion.png', key='Image')],
    [sg.Text(text='Referencias', font=('Calibri', 20), 
                size= 20, 
                expand_x= True,
                justification= 'center')],
    [sg.Image('refLabComp.png', expand_x=True, expand_y=True, key = '-IMAGE-')]              
    ]
    return layout

def layoutArbol(tipo):
    path=tipo+'-arbol-exp.png'
    column = [[sg.Image(filename=path, key='Image')]]
    im = Image.open(path)
    imgAncho, imgAlto = im.size
    imgAncho = imgAncho+35
    srcAncho, srcAlto = getScreenSize()
    if(imgAncho>srcAncho):
        ancho = srcAncho - 15
    else:
        ancho = imgAncho
    alto= srcAlto - 75
    layout = [
        [[sg.Text(text='Árbol de expansión ' + tipo, font=('Calibri', 30), 
                size= 30, 
                expand_x= True,
                justification= 'center')], sg.Button(button_text= 'Ver laberinto recorrido',
                size=(15,2), font=('Calibri'), enable_events=True), 
                sg.Button(button_text= 'Ver iteraciones',
                size=(15,2), font=('Calibri'), enable_events=True)],
        [sg.Column(column, scrollable=True, key='Column', size=(ancho, alto))]
    ]
    return layout
