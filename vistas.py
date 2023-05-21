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
    window0= sg.Window('Laberinto', layout, element_justification='c')
    window  = [window0, None, None, None, None, None, None]
    active  = [True, False, False, False, False, False, False]
    event   = [None, None, None, None, None, None, None]
    values  = [None, None, None, None, None, None, None]
    #0=ventana laberinto, 1=PPArbol, 2=PAArbol, 3=IterPP, 4=IterPA, 5=LabSol
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
                            sg.Popup('Por favor espere hasta que se termine de generar la imagen.', title='Advertencia')
                            generarIteraciones('PP', iterPP)
                            im = Image.open('PP-tabla-iteraciones.png')
                            imgAncho, imgAlto = im.size
                            imgAncho = imgAncho    
                            if(imgAncho>srcAncho):
                                ancho = srcAncho 
                            else:
                                ancho = imgAncho
                            alto= srcAlto - 75     
                            active[3] = True                             
                            window[3] = sg.Window("Iteraciones PP", layoutIteracion('PP'), size=(ancho, alto),
                            finalize=True, resizable=False, margins=(0,0), location=(int((srcAncho-ancho)/2),0),  element_justification='c')  
                    if i == 2:
                        if not active[4]:
                            sg.Popup('Por favor espere hasta que se termine de generar la imagen.', title='Advertencia')
                            generarIteraciones('PA', iterPA)
                            active[4] = True 
                            im = Image.open('PA-tabla-iteraciones.png')
                            imgAncho, imgAlto = im.size
                            imgAncho = imgAncho  
                            if(imgAncho>srcAncho):
                                ancho = srcAncho 
                            else:
                                ancho = imgAncho
                            alto= srcAlto - 75                                 
                            window[4] = sg.Window("Iteraciones PA", layoutIteracion('PA'), size=(ancho, alto),
                                finalize=True, resizable=False, margins=(0,0), location=(int((srcAncho-ancho)/2),0),  element_justification='c')  
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
    imgAncho = imgAncho
    srcAncho, srcAlto = getScreenSize()
    if(imgAncho>srcAncho):
        ancho = srcAncho - 15
    else:
        ancho = imgAncho
    alto= srcAlto - 75
    layout = [
    [sg.Text(text='Iteraciones ', font=('Calibri', 30), 
                size= 30, 
                expand_x= True,
                justification= 'center')],
    [sg.Column(column, scrollable=True, size=(ancho, alto), key='itercol')]
    ]
    return layout

def layoutLaberinto(tipo):
    layout = [
    [sg.Text(text='Laberinto Recorrido', font=('Calibri', 30), 
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