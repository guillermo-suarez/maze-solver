import PySimpleGUI as sg
from genlab import getMaze
from funciones import arbolAPng, laberintoAPng, crearArbolExpansion, getMatrizRecorrida, getCaminoSolucion
from pp import recorrerLabPP
from pa import recorrerLabPA

def generarLaberintoYArbol():
    filas = 10
    columnas = 10
    laberinto = getMaze(filas, columnas)
    # PP
    laberintoAPng(laberinto, filas, columnas, "lab.png")
    visitadosPP, pendientesPP = recorrerLabPP(laberinto)
    arbolPP = crearArbolExpansion(visitadosPP, pendientesPP)
    matrizPP = getMatrizRecorrida(arbolPP, filas, columnas)
    solucionPP = getCaminoSolucion(arbolPP)
    matrizSolucionPP = getMatrizRecorrida(solucionPP, filas, columnas)
    # PA
    visitadosPA, pendientesPA = recorrerLabPA(laberinto)
    arbolPA = crearArbolExpansion(visitadosPA, pendientesPA)
    matrizPA = getMatrizRecorrida(arbolPA, filas, columnas)
    solucionPA = getCaminoSolucion(arbolPA)
    matrizSolucionPA = getMatrizRecorrida(solucionPA, filas, columnas)
    arbolAPng(arbolPP, "expPP.png")
    arbolAPng(arbolPA, "expPA.png")

def make_windowIteraciones(tipo):
    layout = [
        [sg.Text(text='Iteraciones: ')]
        ]
    window = sg.Window('Iteraciones ' + tipo, layout, modal=True, element_justification='c')
    while True:
        event, values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break

def make_windowLaberintoRecorrido(tipo):
    layout = [
        [sg.Text(text='Laberinto Recorrido: ')]
        ]
    window = sg.Window('Laberinto Recorrido ' + tipo, layout, modal=True, element_justification='c')
    while True:
        event, values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break

def make_windowArbol(tipo):    
    if tipo == 'PP':
        img = 'expPP.png'
    else:
        img = 'expPA.png'
    column = [[sg.Image(filename=img, key='Image')]]
    layout = [
        [sg.Button(button_text= 'Ver en forma de laberinto',
                size=(15,2)), 
                sg.Button(button_text= 'Ver iteraciones',
                size=(15,2))],
        [sg.Column(column, size=(1500, 2000), scrollable=True, key='Column')],
        [sg.FileBrowse('Load', enable_events=True)]
    ]
    window = sg.Window('Arbol ' + tipo, layout, modal=True, element_justification='c', resizable=True)
    while True:
        event, values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
        elif event == 'Load':
            filename = values['Load']
            if filename:
                window['Image'].Update(filename=filename)
                # Refresh the update
                window.refresh()
                # Update for scroll area of Column element
                window['Column'].contents_changed()   
        elif event == 'Ver en forma de laberinto':
            make_windowLaberintoRecorrido(tipo)
        elif event == 'Ver iteraciones':
            make_windowIteraciones(tipo)     

def make_windowLaberinto():
    toprow = ['Referencias']
    rows = [
        ['Celda bloqueada'],
        ['Celda libre'],
        ['Inicio y Fin'],
    ]
    layout = [[sg.Text(text ='Laberinto:',
                font=('Times New Roman', 30),
                size= 30, 
                expand_x= True,
                justification= 'center')],
                [sg.Image('lab.png', expand_x=True, expand_y=True, key = '-IMAGE-')],
                [sg.Table(values=rows, 
                headings=toprow,
                auto_size_columns=True,
                display_row_numbers=False,
                num_rows=3,
                row_colors=((0,'white', 'red'),(1,'white', 'green'), (2,'white', 'blue')),
                alternating_row_color='black')],
                [sg.Text(' ')],
                [sg.Button(button_text='Resolver por PP',
                size=(15,2)), 
                sg.Button(button_text='Resolver por PA', 
                        size=(15,2))],
                [sg.Button(button_text='Generar nuevo laberinto', size=(32,2))]                
              ]
    window= sg.Window('Laberinto', layout, modal=True, element_justification='c')
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Salir':
            break
        elif event == 'Resolver por PP':
            make_windowArbol('PP')            
        elif event == 'Resolver por PA':
            make_windowArbol('PA')
        elif event == 'Generar nuevo laberinto':
            generarLaberintoYArbol()
            window['-IMAGE-'].update('lab.png')


sg.theme('DarkGrey2')
layout = [[sg.Text(text = 'Trabajo Práctico Integrador',
                   font=('Times New Roman', 30),
                   size= 30, 
                   expand_x= True,
                   justification= 'center')],     
          [sg.Text(' ')],  
          [sg.Text(text = 'Algoritmos de búsqueda', 
                   font=('Times New Roman', 20),
                   size= 20, 
                   expand_x= True,
                   justification= 'center')], 
          [sg.Text(' ')],  
          [sg.Button(button_text='Generar laberinto',
                     size=(15,2)), 
                    sg.Button(button_text='Salir',
                              size=(15,2))],
          [sg.Text(' ')],  
          [sg.Text(' ')],  
          [sg.Text(text = 'Malazotto, Soledad - Mezio, Santiago - Suárez, Guillermo',
                   font=('Times New Roman', 10),
                   size= 10, 
                   expand_x= True,
                   justification= 'center')]]

window = sg.Window('maze-solver', layout, size=(715,300), element_justification='c')      

while True:                             # The Event Loop
    event, values = window.read() 
    print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Salir':
        break      
    if event == 'Generar laberinto':
        window.close()
        generarLaberintoYArbol()
        make_windowLaberinto()
window.close()