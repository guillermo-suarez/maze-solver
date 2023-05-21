import PySimpleGUI as sg
from generador import generarLaberintoYArboles, generarIteraciones
import pyautogui
from PIL import Image

def getScreenSize():
     width, height= pyautogui.size()
     return width, height

def call_vistas():
    iterPP, iterPA = generarLaberintoYArboles()
    window = make_main()
    while True:                             # The Event Loop
        event, values = window.read() 
        print(event, values)       
        if event == sg.WIN_CLOSED or event == 'Salir':
            break      
        if event == 'Generar laberinto':
            window.close()
            make_windowLaberinto(iterPP, iterPA )
        window.close()

def make_main():
    sg.theme('DarkGrey2')
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
                [sg.Image('refLab.png', expand_x=True, expand_y=True, key = '-IMAGE-')],
                [sg.Text(' ')],
                [sg.Button(button_text='Resolver por PP',
                size=(15,2), font=('Calibri')), 
                sg.Button(button_text='Resolver por PA', 
                        size=(15,2), font=('Calibri'))],
                [sg.Button(button_text='Generar nuevo laberinto', size=(32,2), font=('Calibri'))]                
              ]
    window0= sg.Window('Laberinto', layout, element_justification='c')
    window  = [window0, None, None, None, None, None, None]
    active  = [True, False, False, False, False, False, False]
    event   = [None, None, None, None, None, None, None]
    values  = [None, None, None, None, None, None, None]
    #0=ventana laberinto, 1=PPArbol, 2=PAArbol, 3=IterPP, 4=IterPA, 5=LabSol
    while True:
        for i in range(7):            
            if active[i] and window[i] != None:
                print(i)
                event[i], values[i] = window[i].read(timeout=50)
                if event[i] != sg.TIMEOUT_KEY:
                    print(f'Window {i} event:{event[i]}, values:{values[i]}')
                if event[i] == sg.WIN_CLOSED or event == 'Salir':
                    if i == 0:
                        active[i] = False
                        window[i].close()
                        break
                    else:
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
                             finalize=True, location=(0,0), size=(ancho, alto))                    
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
                    finalize=True, location=(0,0))
                    active[2] = True
                elif event[i] == 'Ver laberinto solución':                    
                    if i == 1 and not active[5]:
                        active[5] = True
                        window[5] = sg.Window("Laberinto solución PP", layoutLaberinto('PP'),
                             finalize=True, location=(0,0))
                    if i == 2 and not active[6]:
                        active[6] = True
                        window[6] = sg.Window("Laberinto solución PA", layoutLaberinto('PA'),
                             finalize=True, location=(0,0))    
                elif event[i] == 'Ver iteraciones':
                    if i == 1:
                        if not active[3]:
                            im = Image.open('PP-tabla-iteraciones.png')
                            imgAncho, imgAlto = im.size
                            imgAncho = imgAncho+35         
                            if(imgAncho>srcAncho):
                                ancho = srcAncho - 15
                            else:
                                ancho = imgAncho
                            alto= srcAlto - 75     
                            active[3] = True 
                            generarIteraciones('PP', iterPP)
                            window[3] = sg.Window("Iteraciones PP", layoutIteracion('PP'), size=(ancho, alto),
                            finalize=True, resizable=False, margins=(0,0), location=(0, 0))  
                    if i == 2:
                        if not active[4]:
                            active[4] = True 
                            im = Image.open('PA-tabla-iteraciones.png')
                            imgAncho, imgAlto = im.size
                            imgAncho = imgAncho+35         
                            if(imgAncho>srcAncho):
                                ancho = srcAncho - 15
                            else:
                                ancho = imgAncho
                            alto= srcAlto - 75     
                            generarIteraciones('PA', iterPA)
                            window[4] = sg.Window("Iteraciones PA", layoutIteracion('PA'), size=(ancho, alto),
                                finalize=True, resizable=False, margins=(0,0), location=(0, 0))  
                elif event[i] == 'Generar nuevo laberinto':
                    generarLaberintoYArboles()
                    window[0]['-IMAGE-'].update('lab.png')
                if i == 0 and active[i] == 0:
                    break
        if i == 0 and active[i] == 0:
            break
    window0.close()

def layoutIteracion(tipo):
    path = tipo + '-tabla-iteraciones.png'
    column = [[sg.Image(filename=path, key='iterimg')]]
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
    [sg.Text(text='Iteraciones ', font=('Calibri'))],
    [sg.Column(column, scrollable=True, size=(ancho, alto), key='itercol')]
    ]
    return layout

def layoutLaberinto(tipo):
    layout = [
    [sg.Text(text='Laberinto Recorrido', font=('Calibri'))],    
    [sg.Image(filename=tipo+'-lab-solucion.png', key='Image')],
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
        [sg.Button(button_text= 'Ver laberinto solución',
                size=(15,2), font=('Calibri'), enable_events=True), 
                sg.Button(button_text= 'Ver iteraciones',
                size=(15,2), font=('Calibri'), enable_events=True)],
        [sg.Column(column, scrollable=True, key='Column', size=(ancho, alto))]
    ]
    return layout

def make_windowArbol(tipo, iter):   
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
        [sg.Button(button_text= 'Ver laberinto solución',
                size=(15,2), font=('Calibri'), enable_events=True), 
                sg.Button(button_text= 'Ver iteraciones',
                size=(15,2), font=('Calibri'), enable_events=True)],
        [sg.Column(column, scrollable=True, key='Column', size=(ancho, alto))]
    ]    

    return sg.Window('Árbol ' + tipo, layout, element_justification='c', resizable=False, margins = (0, 0), location=(int((srcAncho - ancho)/2), 0), size=(int(ancho), int(alto)), finalize=True)
